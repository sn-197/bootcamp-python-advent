from datetime import datetime, date

print("Welkom! Hier is je agenda! Je kan hier je afspraken toevoegen met een herinnering.")

vandaag = date.today()

dagnummer = vandaag.weekday()

dagen = {
    0: "maandag",
    1: "dinsdag",
    2: "woensdag",
    3: "donderdag",
    4: "vrijdag",
    5: "zaterdag",
    6: "zondag"
}

dagnaam = dagen[dagnummer]

print(f"Vandaag is het {dagnaam}")

vandaag = datetime.now()
converted_date = vandaag.strftime("%d-%m-%Y %H:%M:%S")
print(f"Dit is nu de datum en tijd: {converted_date}")



def get_dagnaam(d=None):
    dagen = [
        "maandag", "dinsdag", "woensdag",
        "donderdag", "vrijdag", "zaterdag", "zondag"
    ]
    
    if d is None:
        d = date.today()
    
    return dagen[d.weekday()]


def maak_agenda_item_tekst(titel, start_dt, eind_dt):
    if eind_dt <= start_dt:
        raise ValueError("Eindtijd moet na starttijd liggen")
    
    dagnaam = get_dagnaam(start_dt)
    
    return (
        f"{dagnaam} {start_dt.strftime('%d-%m-%Y')} "
        f"{start_dt.strftime('%H:%M')} - {eind_dt.strftime('%H:%M')} | {titel}")

print(maak_agenda_item_tekst(
    "Team meeting",
    datetime(2026, 4, 22, 14, 30),
    datetime(2026, 4, 22, 15, 30)
))