from dataclasses import dataclass, field
from typing import Dict, List

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
SOURCES = ["Happ", "Haf", "Hpro"]


@dataclass
class WeeklyHours:
    data: Dict[str, Dict[str, float]] = field(default_factory=lambda: {
        source: {day: 0.0 for day in DAYS} for source in SOURCES
    })

    def input_hours(self, source: str):
        print(f"\nEnter hours for {source}:")
        for day in DAYS:
            while True:
                try:
                    hours = float(input(f"{day}: "))
                    if hours < 0:
                        raise ValueError("Hours cannot be negative.")
                    self.data[source][day] = hours
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def generate_checklist(self, source: str) -> List[str]:
        checklist = []
        for day in DAYS:
            hours = self.data[source][day]
            checklist.append(
                f"[ ] {day}: {hours} hours → copy to other systems"
            )
        return checklist

    def weekly_total(self, source: str) -> float:
        return sum(self.data[source].values())

    def display_summary(self, source: str):
        print(f"\nSummary for {source}:")
        for day, hours in self.data[source].items():
            print(f"{day}: {hours} hours")

        total = self.weekly_total(source)
        print(f"Total hours for the week: {total}")


def main():
    tracker = WeeklyHours()

    print("Available sources:", ", ".join(SOURCES))
    source = input("Select source to input (Happ/Haf/Hpro): ").strip()

    if source not in SOURCES:
        print("Invalid source selected.")
        return

    # Input hours
    tracker.input_hours(source)

    # Show checklist
    print("\nChecklist to sync with other systems:")
    checklist = tracker.generate_checklist(source)
    for item in checklist:
        print(item)

    # Show summary
    tracker.display_summary(source)


if __name__ == "__main__":
    main()