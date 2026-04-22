# Deze opdracht bevat een programma om bestandstatistieken van tekstbestandenin te berekenen met Python.

from pathlib import Path

def bereken_statistieken(file_path: str) -> dict:
      
    try:
        aantal_regels = 0
        aantal_woorden = 0
        aantal_letters = 0

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                aantal_regels += 1
                aantal_woorden += len(line.split())
                aantal_letters += sum(1 for c in line if c.isalpha())

        return {
            "# regels": aantal_regels,
            "# woorden": aantal_woorden,
            "# letters": aantal_letters
        }

    except FileNotFoundError:
        print(f"Error: File '{file_path}' niet gevonden.")
        return {}
    except Exception as e:
        print(f"Oeps: {e}")
        return {}

base_dir = Path(__file__).parent

filename = input("Voer de bestandsnaam in: ")

file_path = base_dir / "txt-files" / filename

stats = bereken_statistieken(file_path)

print("\nFile Statistics:")
print(f"Totaal aantal regels: {stats['# regels']}")
print(f"Totaal aantal woorden: {stats['# woorden']}")
print(f"Totaal aantal letters: {stats['# letters']}")