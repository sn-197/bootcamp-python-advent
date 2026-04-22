import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date, timedelta
from tkinter import filedialog
from uuid import uuid4
import tkinter.font as tkfont

# --- helpers ---
def get_dagnaam(d=None):
    dagen = {
        0: "maandag",
        1: "dinsdag",
        2: "woensdag",
        3: "donderdag",
        4: "vrijdag",
        5: "zaterdag",
        6: "zondag"
    }
    if d is None:
        d = date.today()
    return dagen[d.weekday()]

def bereken_herinnering(start_dt, keuze):
    mapping = {
        "Geen": None,
        "5 minuten vooraf": timedelta(minutes=5),
        "15 minuten vooraf": timedelta(minutes=15),
        "1 uur vooraf": timedelta(hours=1),
        "1 dag vooraf": timedelta(days=1)
    }
    delta = mapping.get(keuze)
    return None if delta is None else start_dt - delta

def maak_agenda_item_tekst(titel, start_dt, eind_dt, herinnering_keuze):
    if eind_dt <= start_dt:
        raise ValueError("Eindtijd moet na starttijd liggen")
    
    dagnaam = get_dagnaam(start_dt)
    herinnering_dt = bereken_herinnering(start_dt, herinnering_keuze)
    
    tekst = (
        f"{dagnaam} {start_dt.strftime('%d-%m-%Y')} "
        f"{start_dt.strftime('%H:%M')} - {eind_dt.strftime('%H:%M')} | {titel}"
    )
    
    if herinnering_dt:
        tekst += f"\nHerinnering: {herinnering_dt.strftime('%d-%m-%Y %H:%M')}"
    
    return tekst

def maak_ics_bestand(titel, start_dt, eind_dt, herinnering_keuze, pad):
    uid = str(uuid4())
    dtstamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    alarm_mapping = {
        "5 minuten vooraf": "-PT5M",
        "15 minuten vooraf": "-PT15M",
        "1 uur vooraf": "-PT1H",
        "1 dag vooraf": "-P1D"
    }

    alarm_blok = ""
    if herinnering_keuze in alarm_mapping:
        trigger = alarm_mapping[herinnering_keuze]
        alarm_blok = f"""
BEGIN:VALARM
TRIGGER:{trigger}
ACTION:DISPLAY
DESCRIPTION:Herinnering: {titel}
END:VALARM
"""

    inhoud = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Agenda App//NL
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{dtstamp}
DTSTART:{start_dt.strftime("%Y%m%dT%H%M%S")}
DTEND:{eind_dt.strftime("%Y%m%dT%H%M%S")}
SUMMARY:{titel}{alarm_blok}
END:VEVENT
END:VCALENDAR
"""

    with open(pad, "w", encoding="utf-8") as f:
        f.write(inhoud)


def veilige_bestandsnaam(tekst):
    invalid_chars = '<>:"/\\|?*'
    veilige = "".join(ch if ch not in invalid_chars else "_" for ch in tekst)
    veilige = veilige.strip().replace(" ", "_")
    return veilige[:100] if len(veilige) > 100 else veilige

# --- UI actie ---
def maak_item():
    try:
        titel = entry_titel.get()
        start = entry_start.get()
        eind = entry_eind.get()
        herinnering = reminder_var.get()

        start_dt = datetime.strptime(start, "%d-%m-%y %H:%M")
        eind_dt = datetime.strptime(eind, "%d-%m-%y %H:%M")

        resultaat = maak_agenda_item_tekst(titel, start_dt, eind_dt, herinnering)
        label_resultaat.config(text=resultaat)

    except Exception as e:
        messagebox.showerror("Fout", str(e))

def opslaan_als_ics():
    try:
        titel = entry_titel.get()
        herinnering = reminder_var.get()

        start_dt = datetime.strptime(entry_start.get(), "%d-%m-%y %H:%M")
        eind_dt = datetime.strptime(entry_eind.get(), "%d-%m-%y %H:%M")

        if eind_dt <= start_dt:
            raise ValueError("Eindtijd moet na starttijd liggen")

        veilige_titel = veilige_bestandsnaam(titel)
        datum_str = start_dt.strftime("%Y-%m-%d")

        standaard_naam = f"{datum_str}_{veilige_titel}.ics" if veilige_titel else "afspraak.ics"

        pad = filedialog.asksaveasfilename(
            defaultextension=".ics",
            filetypes=[("Agenda bestand", "*.ics")],
            initialfile=standaard_naam,
            title="Sla agenda-afspraak op"
        )

        if not pad:
            return  # gebruiker annuleert

        maak_ics_bestand(
            titel,
            start_dt,
            eind_dt,
            herinnering,
            pad
        )

        messagebox.showinfo(
            "Succes",
            "De afspraak is opgeslagen als .ics bestand."
        )

    except Exception as e:
        messagebox.showerror("Fout", str(e))

# --- UI bouwen ---
root = tk.Tk()
root.title("Agenda Item Maker")

# 🔹 jouw welkomsttekst in UI
vandaag = date.today()
dagnaam = get_dagnaam(vandaag)

nu = datetime.now()
converted_date = nu.strftime("%d-%m-%Y %H:%M:%S")

welkomsttekst = (
    "👑👑👑\n"
    "\n"
    "Maak hier je Koningsnach Date #savethedate \n"
    "Of één van je andere afspraken :D\n"
    "\n"
    "Sla je #savethedate op als .ics 👑 👑 👑 \n" 
    "\n"
    "en neem de afspraak op in je koninklijke agenda!\n" 
    "\n"
    "👑\n"
    "\n"
    f"Vandaag is het {dagnaam}\n"
    f"Dit is nu de datum en tijd: {converted_date}"
)


welkomst_font = tkfont.Font(
    family="Helvetica",
    size=10,
    slant="italic"
)


tk.Label(
    root,
    text=welkomsttekst,
    justify="left",
    fg="#ff7a00",          # fel oranje
    font=welkomst_font
).grid(
    row=0, column=0,
    columnspan=2,
    pady=10
)


# --- invoervelden ---
tk.Label(root, text="Titel:").grid(row=1, column=0)
entry_titel = tk.Entry(root, width=30)
entry_titel.grid(row=1, column=1)
entry_titel.insert(0, "Koningsnach")

tk.Label(root, text="Begin (DD-MM-JJ UU:MM):").grid(row=2, column=0)
entry_start = tk.Entry(root, width=30)
entry_start.grid(row=2, column=1)
entry_start.insert(0, "26-04-26 22:22")


tk.Label(root, text="Eind (DD-MM-JJ UU:MM):").grid(row=3, column=0)
entry_eind = tk.Entry(root, width=30)
entry_eind.grid(row=3, column=1)
entry_eind.insert(0, "27-04-26 04:40")

# 🔔 reminder dropdown
tk.Label(root, text="Herinnering:  🔔 ").grid(row=4, column=0)

reminder_var = tk.StringVar(root)
reminder_var.set("Geen")

opties = [
    "Geen",
    "5 minuten vooraf",
    "15 minuten vooraf",
    "1 uur vooraf",
    "1 dag vooraf"
]

tk.OptionMenu(root, reminder_var, *opties).grid(row=4, column=1)

tk.Button(root, text="Maak agenda item", command=maak_item)\
    .grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(
    root,
    text="Opslaan als .ics",
    command=opslaan_als_ics
).grid(row=6, column=0, columnspan=2, pady=5)

label_resultaat = tk.Label(root, text="", fg="orange", justify="left")
label_resultaat.grid(row=7, column=0, columnspan=2)

root.mainloop()