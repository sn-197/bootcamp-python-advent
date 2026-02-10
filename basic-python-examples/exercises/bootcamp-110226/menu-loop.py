# Dit is een simpel menu-systeem met while-loops

while True:
    print("Welkom bij het menu!")
    print("1. Som")
    print("2. Verschil")
    print("3. Product")
    print("4. Quotient")
    print("5. Afsluiten")

    keuze = input("Maak een keuze (1-5): ")

    if keuze == "1":
        num1 = float(input("Voer het eerste getal in: "))
        num2 = float(input("Voer het tweede getal in: "))
        resultaat = num1 + num2
        print(f"Het resultaat van {num1} + {num2} is {resultaat}")
    elif keuze == "2":
        num1 = float(input("Voer het eerste getal in: "))
        num2 = float(input("Voer het tweede getal in: "))
        resultaat = num1 - num2
        print(f"Het resultaat van {num1} - {num2} is {resultaat}")
    elif keuze == "3":
        num1 = float(input("Voer het eerste getal in: "))
        num2 = float(input("Voer het tweede getal in: "))
        resultaat = num1 * num2
        print(f"Het resultaat van {num1} * {num2} is {resultaat}")
    elif keuze == "4":
        num1 = float(input("Voer het eerste getal in: "))
        num2 = float(input("Voer het tweede getal in: "))
        if num2 != 0:
            resultaat = num1 / num2
            print(f"Het resultaat van {num1} / {num2} is {resultaat}")
        else:
            print("Delen door nul is niet toegestaan.")
    elif keuze == "5":
        print("Bedankt voor het gebruiken van het menu. Tot ziens!")
        break
    else:
        print("Ongeldige keuze, probeer het opnieuw.")