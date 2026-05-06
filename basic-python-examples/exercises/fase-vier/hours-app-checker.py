from dataclasses import dataclass, field
from typing import Dict

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
SOURCES = ["Happ", "Haf", "Hpro"]


@dataclass
class WeeklyHours:
    week_number: int
    data: Dict[str, Dict[str, float]] = field(default_factory=dict)

    def __post_init__(self):
        for source in SOURCES:
            self.data[source] = {day: None for day in DAYS}

    def input_primary_hours(self, source: str):
        print(f"\nEnter hours for {source} (Week {self.week_number}):")
        for day in DAYS:
            while True:
                try:
                    hours = float(input(f"{day}: "))
                    if hours < 0:
                        raise ValueError
                    self.data[source][day] = hours
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def generate_checklist(self, source: str):
        print("\nChecklist to copy to other systems:")
        for day in DAYS:
            hours = self.data[source][day]
            print(f"[ ] Week {self.week_number} - {day}: {hours} hours")

    def verify_other_sources(self, primary_source: str):
        print("\nVerification against other sources:")

        for source in SOURCES:
            if source == primary_source:
                continue

            print(f"\nChecking against {source}:")

            for day in DAYS:
                expected = self.data[primary_source][day]

                while True:
                    try:
                        actual = float(
                            input(f"{day} (expected {expected}): ")
                        )
                        if actual < 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                if actual == expected:
                    print(f"  ✅ Match")
                else:
                    print(f"  ❌ Mismatch (got {actual}, expected {expected})")

    def weekly_total(self, source: str):
        return sum(self.data[source].values())

    def display_summary(self, source: str):
        print(f"\nSummary for {source} (Week {self.week_number}):")
        total = self.weekly_total(source)
        print(f"Total hours: {total}")


def get_week_number():
    while True:
        try:
            week = int(input("Enter week number (1-53): "))
            if 1 <= week <= 53:
                return week
        except ValueError:
            pass
        print("Invalid week number.")


def main():
    week_number = get_week_number()
    tracker = WeeklyHours(week_number)

    print("Available sources:", ", ".join(SOURCES))
    primary_source = input("Select primary source: ").strip()

    if primary_source not in SOURCES:
        print("Invalid source.")
        return

    # Step 1: Input main source
    tracker.input_primary_hours(primary_source)

    # Step 2: Checklist
    tracker.generate_checklist(primary_source)

    # Step 3: Verify others (lightweight)
    tracker.verify_other_sources(primary_source)

    # Step 4: Summary
    tracker.display_summary(primary_source)


if __name__ == "__main__":
    main()