# Dit is een quiz-app

# De quiz-app heeft een lijst van meerkeuzevragen en antwoorden
# Als speler krijg je een vraag te zien en kan je een punt verdienen door het juiste antwoord te geven
# Aan het einde van de quiz krijgt de speler te zien hoeveel vragen hij goed heeft beantwoord    
# De speler ziet een timer, die bijhoudt hoe lang die bezig is met quizzen
# Maak een UI waarin de speler vragen en antwoorden kan zien en kan klikken op het juiste antwoord
# Voeg ook een scorebord toe waar de speler zijn score kan zien
# Geef de speler de mogelijkheid om zijn naam in te voeren aan het einde van de quiz en sla zijn score op in een bestand
# geef de speler een optie om de quiz opnieuw te spelen 

import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import json
import os
import random


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("1000x650")
        self.root.configure(bg="#f0f0f0")

        self.leaderboard_file = os.path.join(os.path.dirname(__file__), "leaderboard.json")

        self.player_name = None
        self.score = 0
        self.current_question_index = 0
        self.start_time = None
        self.timer_running = False

        self.bonus_added = False

        self.build_questions()

        self.create_widgets()
        self.load_question()

    # -----------------------------
    # QUESTIONS
    # -----------------------------
    def build_questions(self):

        self.questions_by_category = {
            "Natuur & Wereld": [
                {
                    "question": "Wat is de grootste planeet?", 
                    "options": ["Aarde","Mars","Jupiter","Saturnus"], 
                    "answer": "Jupiter"
                },
                {
                    "question": "Hoeveel continenten zijn er?",
                    "options": ["5", "6", "7", "8"],
                    "answer": "7"
                },
                {
                    "question": "Wat is de chemische formule van water?",
                    "options": ["CO2", "H2O", "O2", "NaCl"],
                    "answer": "H2O"
                },
                {
                    "question": "Wat is de snelheid van het licht?",
                    "options": ["300.000 km/s", "150.000 km/s", "500.000 km/s", "100.000 km/s"],
                    "answer": "300.000 km/s"
                },
                {
                    "question": "Welke planeet staat bekend als de rode planeet?",
                    "options": ["Aarde", "Mars", "Jupiter", "Venus"],
                    "answer": "Mars"
                },
                {
                    "question": "Hoeveel oceanen zijn er op aarde?",
                    "options": ["5", "6", "7", "8"],
                    "answer": "5"
                },
                {
                    "question": "Wat is de chemische formule van zuurstof?",
                    "options": ["CO2", "H2", "O2", "NaCl"],
                    "answer": "O2"
                },
                {
                    "question": "Wat is het grootste zoogdier ter wereld?",
                    "options": ["Olifant", "Blauwe vinvis", "Giraf", "Nijlpaard"],
                    "answer": "Blauwe vinvis"
                },
                {
                    "question": "Welke taal wordt voornamelijk gesproken in Brazilië?",
                    "options": ["Spaans", "Portugees", "Engels", "Frans"],
                    "answer": "Portugees"
                },
                {
                    "question": "Hoeveel dagen heeft een schrikkeljaar?",
                    "options": ["365", "366", "364", "367"],
                    "answer": "366"
                },
                {
                    "question": "Hoeveel zijden heeft een tetraëder?",
                    "options": ["4", "5", "6", "7"],
                    "answer": "4"
                },
                {
                    "question": "Wat is de meest gesproken taal ter wereld?",
                    "options": ["Engels", "Spaans", "Mandarijn Chinees", "Hindi"],
                    "answer": "Mandarijn Chinees"
                }
            ],
            "Literatuur": [
                {
                    "question": "Wie schreef 'Romeo and Juliet'?", 
                    "options": ["Shakespeare","Tolstoj","Dante","Homerus"], 
                    "answer": "Shakespeare"
                },
                {
                    "question": "Wie schreef 'A Tale Of Two Cities'?",
                    "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
                    "answer": "Charles Dickens"
                },
                {
                    "question": "Wie schreef 'Don Quichot'?",
                    "options": ["Cervantes", "Homeros", "Dante", "Boccaccio"],
                    "answer": "Cervantes"
                },
                {
                    "question": "Welke schrijver schreef '1984'?",
                    "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Isaac Asimov"],
                    "answer": "George Orwell"
                },
                {
                    "question": "Wie schreef 'De Avonden'?",
                    "options": ["Harry Mulisch", "Willem Frederik Hermans", "Gerard Reve", "Hella S. Haasse"],
                    "answer": "Gerard Reve"
                }
            ],
            "AI": [
                {
                    "question": "Welk bedrijf ontwikkelde ChatGPT?",
                    "options": ["Google", "OpenAI", "Meta", "Microsoft"],
                     "answer": "OpenAI"
                },
                {
                    "question": "In welk jaar werd de eerste AI chatbot ELIZA gemaakt?",
                    "options": ["1955", "1966", "1975", "1985"],
                    "answer": "1966"
                },
                {
                    "question": "Hoe kun je machine learning het best omschrijven?",
                    "options": ["Een computer die instructies bedenkt en machinaal leert", "Een digitale leerling die patronen herkent in grote stapels informatie", "Een machine die alleen werkt als een mens de knoppen indrukt", "Een systeem dat sneller typt dan een mens"],
                    "answer": "Een digitale leerling die patronen herkent in grote stapels informatie"
                },
                {
                    "question": "Wat staat AI voor?", 
                    "options": ["Artificial Intelligence","Artificial Innovation","Applied Intelligence","Artistic Ideals"], 
                    "answer": "Artificial Intelligence"
                },
                {
                    "question": "Welke AI technologie wordt gebruikt voor gezichtsherkenning?",
                    "options": ["Database query", "Neural Networks", "Spreadsheet", "File compression"],
                    "answer": "Neural Networks"
                },
                {
                    "question": "Wie wordt beschouwd als de 'vader van AI'?",
                    "options": ["Alan Turing", "John McCarthy", "Geoffrey Hinton", "Yann LeCun"],
                    "answer": "John McCarthy"
                },
                {
                    "question": "Wat is deep learning?",
                    "options": ["Een vorm van machine learning met meerdere lagen", "Diep in je computer kijken", "Data kopiëren uit lange programmeerfiles", "In het diepe leren zwemmen",],
                    "answer": "Een vorm van machine learning met meerdere lagen"
                },
                {
                    "question": "Welke programmertaal is populair voor AI development?",
                    "options": ["JavaScript", "Python", "C++", "Java"],
                    "answer": "Python"
                }
            ],
            "Kunst": [
                {
                    "question": "Wie schilderde Mona Lisa?",
                    "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
                    "answer": "Leonardo da Vinci"
                },
                {
                    "question": "Welke kleur krijg je door rood en blauw en wit te mengen?",
                    "options": ["Paars", "Oranje", "Roze", "Lila"],
                    "answer": "Lila"
                },
                {
                    "question": "Wie was beroemd vanwege zijn grote oren?",
                    "options": ["Pablo Picasso", "Vincent van Gogh", "Caravaggio", "Rembrandt"],
                    "answer": "Vincent van Gogh"
                },
                {
                    "question": "Wie heeft het plafond van de Sixtijnse Kapel geschilderd?",
                    "options": ["Leonardo", "Raphael", "Michelangelo", "Donatello"],
                    "answer": "Michelangelo"
                }
            ],
            "Topografie & Geschiedenis": [
                {
                    "question": "Wat is de hoofdstad van Frankrijk?", 
                    "options": ["Parijs","Lyon","Nice","Marseille"], 
                    "answer": "Parijs"
                },
                {
                    "question": "In welk jaar viel de Muur van Berlijn?",
                    "options": ["1987", "1989", "1991", "1993"],
                    "answer": "1989"
                },
                {
                    "question": "Wie was de eerste president van de Verenigde Staten?",
                    "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "Benjamin Franklin"],
                    "answer": "George Washington"
                },
                {
                    "question": "Welke kleuren heeft de vlag van Chili?",
                    "options": ["Rood, Wit, Blauw", "Blauw, Wit", "Geel, Groen", "Rood, Geel, Zwart"],
                    "answer": "Rood, Wit, Blauw"
                },
                {
                    "question": "Wat is de hoofdstad van Australië?",
                    "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                    "answer": "Canberra"
                },
                {
                    "question": "Wat is de hoofdstad van Canada?",
                    "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"],
                    "answer": "Ottawa"
                }
            ],
            "Bonus": [
                {
                    "question": "Wat is het belangrijkste doel van regularization in machine learning?",
                    "options": ["Overfitting verminderen", "Data vergroten", "Training versnellen", "Model complexer maken"],
                    "answer": "Overfitting verminderen"
                },
                {
                    "question": "Wat doet een activation function in een neuraal netwerk?",
                    "options": ["Zet data om in tekst", "Introduceert niet-lineariteit", "Verhoogt dataset grootte", "Slaat gewichten op"],
                    "answer": "Introduceert niet-lineariteit"
                },
                {
                    "question": "Wat is het verschil tussen supervised en unsupervised learning?",
                    "options": ["Supervised gebruikt geen data", "Unsupervised gebruikt gelabelde data", "Supervised gebruikt gelabelde data", "Er is geen verschil"],
                    "answer": "Supervised gebruikt gelabelde data"
                },
                {
                    "question": "Wat betekent de term overfitting?",
                    "options": ["Model presteert slecht op trainingsdata", "Model leert te weinig", "Model leert trainingsdata te goed en generaliseert slecht", "Model gebruikt te weinig data"],
                    "answer": "Model leert trainingsdata te goed en generaliseert slecht"
                },
                {
                    "question": "Welke techniek wordt vaak gebruikt om tekst te verwerken in moderne AI-modellen?",
                    "options": ["Decision Trees", "Transformers", "Linear Regression", "K-Means"],
                    "answer": "Transformers"
                },
                {
                    "question": "Wat is een loss function?",
                    "options": ["Een manier om data op te slaan", "Een functie die modelprestatie meet", "Een database", "Een type neuron"],
                    "answer": "Een functie die modelprestatie meet"
                },
                {
                    "question": "Wat is gradient descent?",
                    "options": ["Een methode om data te verzamelen", "Een optimalisatie-algoritme", "Een type dataset", "Een programmeertaal"],
                    "answer": "Een optimalisatie-algoritme"
                },
                {
                    "question": "Waarom zijn transformer-modellen efficiënter dan RNN’s bij lange teksten?",
                    "options": ["Ze gebruiken minder data", "Ze verwerken woorden parallel", "Ze hebben geen training nodig", "Ze slaan alles lokaal op"],
                    "answer": "Ze verwerken woorden parallel"
                },
                {
                    "question": "Wat doet fine-tuning van een model?",
                    "options": ["Model volledig opnieuw trainen vanaf nul", "Model aanpassen met specifieke data", "Model verwijderen", "Data comprimeren"],
                    "answer": "Model aanpassen met specifieke data"
                },
                {
                    "question": "Wat is het doel van een training dataset?",
                    "options": ["Model testen", "Model trainen", "Model verwijderen", "Data visualiseren"],
                    "answer": "Model trainen"
                },
                {
                    "question": "Wat is het belangrijkste voordeel van self-attention in transformer-modellen?",
                    "options": ["Het vermindert de dataset grootte", "Het laat elk woord rekening houden met alle andere woorden in de input", "Het verwijdert de noodzaak van training", "Het maakt modellen lineair"],
                    "answer": "Het laat elk woord rekening houden met alle andere woorden in de input"
                },
                {
                    "question": "Wat beschrijft het probleem van 'vanishing gradients' in diepe neurale netwerken?",
                    "options": ["Gewichten worden te groot tijdens training", "Gradiënten worden zo klein dat het model nauwelijks nog leert", "De dataset verdwijnt tijdens training", "Het model gebruikt te veel geheugen"],
                    "answer": "Gradiënten worden zo klein dat het model nauwelijks nog leert"
                },
                {
                    "question": "Waarom gebruiken veel moderne taalmodellen positional encoding?",
                    "options": ["Om data te comprimeren", "Om woordvolgorde informatie toe te voegen aan het model", "Om training sneller te maken zonder verlies", "Om labels toe te voegen aan data"],
                    "answer": "Om woordvolgorde informatie toe te voegen aan het model"
                }
            ]    
        }

        # 1 random per categorie
        self.questions = []
        self.used_categories = list(self.questions_by_category.keys())[:-1]

        for cat in self.used_categories:
            self.questions.append(random.choice(self.questions_by_category[cat]))

        self.bonus_question = random.choice(self.questions_by_category["Bonus"])
        self.total_questions = len(self.questions)

    # -----------------------------
    # UI
    # -----------------------------
    def create_widgets(self):

        top = tk.Frame(self.root, bg="#f0f0f0")
        top.pack(fill=tk.X)

        self.info_label = tk.Label(
            top,
            text="Beantwoord 5 vragen. Heb je er 5 goed? Dan krijg je een bonusvraag!!",
            bg="#f0f0f0",
            font=("Arial", 11)
        )
        self.info_label.pack(pady=10)

        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 18),
            wraplength=800,
            bg="#f0f0f0"
        )
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.root,
                text="",
                font=("Arial", 14),
                width=50,
                height=2,
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        bottom = tk.Frame(self.root, bg="#f0f0f0")
        bottom.pack(fill=tk.X, pady=20)

        self.score_label = tk.Label(bottom, text="Score: 0", font=("Arial", 12), bg="#f0f0f0")
        self.score_label.pack(side=tk.LEFT, padx=20)

        self.timer_label = tk.Label(bottom, text="Tijd: 0s", font=("Arial", 12), bg="#f0f0f0")
        self.timer_label.pack(side=tk.LEFT)

        tk.Button(
            bottom,
            text="Leaderboard",
            command=self.show_leaderboard,
            bg="#2196F3",
            fg="white"
        ).pack(side=tk.RIGHT, padx=20)

    # -----------------------------
    # QUESTIONS FLOW
    # -----------------------------
    def load_question(self):
        if self.current_question_index == 0:
            self.start_time = time.time()
            self.update_timer()

        if self.current_question_index < len(self.questions):
            q = self.questions[self.current_question_index]

            self.question_label.config(text=q["question"])

            for i, opt in enumerate(q["options"]):
                self.option_buttons[i].config(text=opt)
        else:
            self.end_quiz()

    def check_answer(self, idx):
        q = self.questions[self.current_question_index]
        selected = q["options"][idx]

        if selected == q["answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Goed!")
        else:
            messagebox.showerror("Fout", f"Correct antwoord: {q['answer']}")

        self.score_label.config(text=f"Score: {self.score}")

        # BONUS LOGICA
        if self.score >= 5 and not self.bonus_added:
            self.questions.append(self.bonus_question)
            self.bonus_added = True
            messagebox.showinfo("Ai, ai, ai...", "Je hebt een bonusvraag vrijgespeeld!")

        self.current_question_index += 1
        self.load_question()

    # -----------------------------
    # TIMER
    # -----------------------------
    def update_timer(self):
        if self.start_time:
            elapsed = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Tijd: {elapsed}s")
            self.root.after(1000, self.update_timer)

    # -----------------------------
    # END QUIZ
    # -----------------------------
    def end_quiz(self):
        self.timer_running = False
        total_time = int(time.time() - self.start_time)

        self.player_name = simpledialog.askstring("Naam", "Wat is je naam?") or "Anoniem"

        self.save_score(total_time)

        again = messagebox.askyesno(
            "Quiz klaar!",
            f"Score: {self.score}/{len(self.questions)}\nTijd: {total_time}s\n\nOpnieuw spelen? Kies Nee als je wil stoppen. Dan sluit je de app af. \n\nWil je een nieuwe ronde met nieuwe kansen, kies dan Ja!"
        )

        if again:
            self.reset_quiz()
        else:
           # 🔴 EXPLICIET AFSLUITEN VAN DE APP
            self.cleanup_and_exit()
    
    def cleanup_and_exit(self):
        # stop alles wat nog kan lopen
        self.timer_running = False

    # optioneel: extra cleanup later uitbreidbaar
        self.root.destroy()

    # -----------------------------
    # LEADERBOARD
    # -----------------------------
    def load_leaderboard(self):
        if os.path.exists(self.leaderboard_file):
            try:
                with open(self.leaderboard_file, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_score(self, total_time):
        data = self.load_leaderboard()

        data.append({
            "name": self.player_name,
            "score": self.score,
            "time": total_time,
            "total": len(self.questions)
        })

        with open(self.leaderboard_file, "w") as f:
            json.dump(data, f, indent=2)

    def show_leaderboard(self):
        data = self.load_leaderboard()

        win = tk.Toplevel(self.root)
        win.title("Leaderboard")
        win.geometry("500x400")

        tk.Label(win, text="TOP SCORES", font=("Arial", 16)).pack(pady=10)

        frame = tk.Frame(win)
        frame.pack(fill=tk.BOTH, expand=True)

        data = sorted(data, key=lambda x: (-x.get("score", 0), x.get("time", 9999)))

        for i, entry in enumerate(data[:10], 1):
            tk.Label(
                frame,
                text=f"{i}. {entry['name']} - {entry['score']}/{entry['total']} - {entry['time']}s",
                font=("Arial", 12)
            ).pack(anchor="w", padx=20)



    # -----------------------------
    # RESET QUIZ
    # -----------------------------
    def reset_quiz(self):
        self.score = 0
        self.current_question_index = 0
        self.start_time = None
        self.timer_running = False
        self.bonus_added = False

        self.build_questions()

        self.score_label.config(text="Score: 0")
        self.timer_label.config(text="Tijd: 0s")

        self.load_question()

# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()