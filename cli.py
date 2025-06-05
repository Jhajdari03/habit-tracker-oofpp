# Command Line Interface (CLI) tool
from habit_tracker import HabitTracker
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak,
    get_streak_for_habit
)
import json

def load_habits_raw():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def cli():
    """
    Command-line interface for interacting with the HabitTracker and analytics.
    """
    tracker = HabitTracker()
    tracker.load_from_file('habits.json')

    while True:
        print("\nHabit Tracker CLI")
        print("1. Add Habit")
        print("2. Complete Habit")
        print("3. Show Longest Streak (OOP)")
        print("4. Show All Habits (OOP)")
        print("5. Show Habits by Periodicity (OOP)")
        print("6. Delete Habit")
        print("7. View Completion History")
        print("8. Save and Exit")
        print("9. ANALYTICS: Show All Habit Names (FP)")
        print("10. ANALYTICS: Filter by Periodicity (FP)")
        print("11. ANALYTICS: Longest Overall Streak (FP)")
        print("12. ANALYTICS: Streak for Specific Habit (FP)")

        choice = input("Enter your choice: ").strip().lower()

        try:
            if choice == '1':
                name = input("Enter habit name: ").strip()
                periodicity = input("Enter habit periodicity (daily/weekly): ").strip().lower()
                tracker.add_habit(name, periodicity)
                print(f"Habit '{name}' added with '{periodicity}' periodicity.")
            elif choice == '2':
                name = input("Enter habit name to complete: ").strip()
                tracker.complete_habit(name)
                print(f"Habit '{name}' marked as completed.")
            elif choice == '3':
                print(f"Longest streak: {tracker.get_longest_streak()}")
            elif choice == '4':
                habits = tracker.get_habits()
                for habit in habits:
                    print(f"Habit: {habit.name}, Periodicity: {habit.periodicity}, Streak: {habit.get_streak()}")
            elif choice == '5':
                periodicity = input("Enter periodicity (daily/weekly): ").strip().lower()
                habits = tracker.get_habits_by_periodicity(periodicity)
                for habit in habits:
                    print(f"Habit: {habit.name}, Streak: {habit.get_streak()}")
            elif choice == '6':
                name = input("Enter habit name to delete: ").strip()
                tracker.delete_habit(name)
            elif choice == '7':
                name = input("Enter habit name to view history: ").strip()
                habit = tracker.get_habit(name)
                if habit:
                    history = habit.get_completion_history()
                    if history:
                        print(f"Completion history for '{name}':")
                        for completion in history:
                            print(f"- {completion}")
                    else:
                        print(f"No completions recorded for '{name}'.")
                else:
                    print(f"Habit '{name}' not found.")
            elif choice == '8':
                tracker.save_to_file('habits.json')
                print("Habits saved. Exiting...")
                break

            # === Functional Analytics ===
            elif choice == '9':
                habits = load_habits_raw()
                names = get_all_habits(habits)
                print("All Habit Names:")
                for n in names:
                    print(f"- {n}")
            elif choice == '10':
                period = input("Enter periodicity (daily/weekly): ").strip().lower()
                habits = load_habits_raw()
                filtered = get_habits_by_periodicity(habits, period)
                print(f"{period.capitalize()} Habits:")
                for h in filtered:
                    print(f"- {h['name']}")
            elif choice == '11':
                habits = load_habits_raw()
                longest = get_longest_streak(habits)
                print(f"Longest streak (FP): {longest}")
            elif choice == '12':
                name = input("Enter habit name: ").strip()
                habits = load_habits_raw()
                streak = get_streak_for_habit(habits, name)
                print(f"Streak for '{name}' (FP): {streak}")
            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    cli()
