# maak een rekenmachine die de gebruiker vraagt om 2 getallen en een operator (+, -, *, /) en het resultaat teruggeeft
# geef ook complexe berekeningen als wortel en machtsverheffen 
# maak er een UI bij waar de gebruiker de getallen en operator kan invoeren en het resultaat kan zien

import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Geavanceerde Rekenmachine")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")
        
        # Display voor het resultaat
        self.result_var = tk.StringVar(value="0")
        self.create_display()
        
        # Invoervelden
        self.create_input_fields()
        
        # Buttons voor operators
        self.create_operator_buttons()
        
        # Display voor berekeningshistorie
        self.create_history_display()
        
    def create_display(self):
        """Maak het resultaat display"""
        display_frame = tk.Frame(self.root, bg="#f0f0f0")
        display_frame.pack(pady=10, padx=10, fill=tk.X)
        
        tk.Label(display_frame, text="Resultaat:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor=tk.W)
        
        display = tk.Entry(
            display_frame,
            textvariable=self.result_var,
            font=("Arial", 20, "bold"),
            justify=tk.RIGHT,
            state=tk.DISABLED,
            bg="#ffffff",
            fg="#000000"
        )
        display.pack(fill=tk.X, ipady=10)
        
    def create_input_fields(self):
        """Maak invoervelden voor getallen en operator"""
        input_frame = tk.LabelFrame(self.root, text="Invoer", font=("Arial", 11, "bold"), bg="#f0f0f0", padx=10, pady=10)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Eerste getal
        tk.Label(input_frame, text="Eerste getal:", bg="#f0f0f0").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num1_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
        self.num1_entry.grid(row=0, column=1, sticky=tk.EW, padx=5)
        
        # Operator
        tk.Label(input_frame, text="Operator:", bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.operator_var = tk.StringVar(value="+")
        
        operator_frame = tk.Frame(input_frame, bg="#f0f0f0")
        operator_frame.grid(row=1, column=1, sticky=tk.EW, padx=5)
        
        operators = ["+", "-", "*", "/", "√ (wortel)", "^(macht)"]
        for op in operators:
            tk.Radiobutton(operator_frame, text=op, variable=self.operator_var, value=op, bg="#f0f0f0").pack(anchor=tk.W)
        
        # Tweede getal
        tk.Label(input_frame, text="Tweede getal:", bg="#f0f0f0").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.num2_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
        self.num2_entry.grid(row=2, column=1, sticky=tk.EW, padx=5)
        
        input_frame.columnconfigure(1, weight=1)
        
    def create_operator_buttons(self):
        """Maak knoppen voor berekening en andere functies"""
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="Berekenen", command=self.calculate, font=("Arial", 12, "bold"), 
                  bg="#4CAF50", fg="white", padx=20, pady=10).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Wissen", command=self.clear, font=("Arial", 12), 
                  bg="#f44336", fg="white", padx=20, pady=10).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Geschiedenis", command=self.show_history, font=("Arial", 12), 
                  bg="#2196F3", fg="white", padx=20, pady=10).pack(side=tk.LEFT, padx=5)
        
    def create_history_display(self):
        """Maak een display voor berekeningshistorie"""
        history_frame = tk.LabelFrame(self.root, text="Berekeningshistorie", font=("Arial", 11, "bold"), bg="#f0f0f0", padx=10, pady=10)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.history_text = tk.Text(history_frame, height=8, font=("Arial", 10), yscrollcommand=scrollbar.set)
        self.history_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.history_text.yview)
        
        self.history = []
        
    def calculate(self):
        """Voer de berekening uit"""
        try:
            num1_str = self.num1_entry.get().strip()
            num2_str = self.num2_entry.get().strip()
            operator = self.operator_var.get()
            
            if not num1_str:
                messagebox.showerror("Fout", "Voer alstublieft het eerste getal in")
                return
            
            num1 = float(num1_str)
            
            # Berekening voor wortels (alleen 1 getal nodig)
            if operator == "√ (wortel)":
                if num1 < 0:
                    messagebox.showerror("Fout", "De wortel van een negatief getal kan niet berekend worden")
                    return
                result = math.sqrt(num1)
                calculation = f"√{num1} = {result}"
                self.history.append(calculation)
            
            # Berekening voor macht (2 getallen nodig)
            elif operator == "^(macht)":
                if not num2_str:
                    messagebox.showerror("Fout", "Voer alstublieft het tweede getal in")
                    return
                num2 = float(num2_str)
                try:
                    result = num1 ** num2
                    if result > 1.7976931348623157e+308:
                        messagebox.showerror("Fout", f"Resultaat te groot! Maximum: 1.8 × 10^308")
                        return
                except OverflowError:
                    messagebox.showerror("Fout", f"Berekening te groot! Maximum waarde: 1.8 × 10^308\nProbeer kleinere getallen of exponent.")
                    return
                calculation = f"{num1} ^ {num2} = {result}"
                self.history.append(calculation)
            
            # Normale berekeningen
            else:
                if not num2_str:
                    messagebox.showerror("Fout", "Voer alstublieft het tweede getal in")
                    return
                
                num2 = float(num2_str)
                
                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        messagebox.showerror("Fout", "Kan niet door nul delen")
                        return
                    result = num1 / num2
                
                calculation = f"{num1} {operator} {num2} = {result}"
                self.history.append(calculation)
            
            # Toon het resultaat
            self.result_var.set(str(round(result, 10)))
            
            # Update geschiedenis
            self.update_history_display()
            
        except ValueError:
            messagebox.showerror("Fout", "Voer alstublieft geldige getallen in")
    
    def update_history_display(self):
        """Update de geschiedenis tekst"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        for item in self.history[-10:]:  # Toon de laatste 10 berekeningen
            self.history_text.insert(tk.END, item + "\n")
        self.history_text.config(state=tk.DISABLED)
    
    def clear(self):
        """Wis alle invoervelden"""
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_var.set("0")
        self.num1_entry.focus()
    
    def show_history(self):
        """Toon volledige geschiedenis in messagebox"""
        if not self.history:
            messagebox.showinfo("Geschiedenis", "Nog geen berekeningen gemaakt")
        else:
            history_text = "\n".join(self.history)
            messagebox.showinfo("Volledige Geschiedenis", history_text)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
