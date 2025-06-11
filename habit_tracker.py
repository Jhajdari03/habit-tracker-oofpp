import json
from datetime import datetime, timedelta

class Habit:
    """
    Represents a habit with a name, periodicity (daily/weekly),
    a creation date, and a list of completion timestamps.
    """

    def __init__(self, name, periodicity):
        """
        Initializes a new Habit.
        
        Args:
            name (str): The name of the habit.
            periodicity (str): The periodicity of the habit ('daily' or 'weekly').
        """
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.now()
        self.completions = []

    def complete_task(self):
        """Marks the habit as completed by adding the current timestamp to completions."""
        self.completions.append(datetime.now())

    def get_streak(self):
        """
        Calculates the longest streak of consecutive habit completions.

        Returns:
            int: The number of consecutive completions.
        """
        if not self.completions:
            return 0

        sorted_completions = sorted(self.completions)
        streak = 1
        last_completion = sorted_completions[0]

        for completion in sorted_completions[1:]:
            if completion - last_completion <= self._get_period_delta():
                streak += 1
            else:
                break
            last_completion = completion

        return streak

    def _get_period_delta(self):
        """
        Determines the time delta between expected completions based on periodicity.
        
        Returns:
            timedelta: The time delta for the habit based on its periodicity.
        """
        if self.periodicity == 'daily':
            return timedelta(days=1)
        elif self.periodicity == 'weekly':
            return timedelta(weeks=1)
        else:
            raise ValueError('Unsupported periodicity')
    
    def get_completion_history(self):
        """
        Returns the history of completion timestamps.
        
        Returns:
            list: A list of completion timestamps.
        """
        return self.completions
        


class HabitTracker:
    """
    Manages a collection of habits, including adding, completing,
    deleting, and retrieving habit information.
    """
    def __init__(self):
        """Initializes an empty HabitTracker."""
        self.habits = []

    def add_habit(self, name, periodicity):
        """
        Adds a new habit to the tracker.

        Args:
            name (str): The name of the habit.
            periodicity (str): The periodicity of the habit ('daily' or 'weekly').
        
        Raises:
            ValueError: If name or periodicity is invalid.
        """
        if not name or not periodicity:
            raise ValueError("Name and periodicity must be provided")
        if periodicity not in ['daily', 'weekly']:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        new_habit = Habit(name, periodicity)
        self.habits.append(new_habit)

    def complete_habit(self, name):
        """
        Marks a habit as completed.
        
        Args:
            name (str): The name of the habit to complete.
        
        Raises:
            ValueError: If the habit with the given name is not found.
        """
        for habit in self.habits:
            if habit.name == name:
                habit.complete_task()
                break
        else:
            raise ValueError(f"Habit with name '{name}' not found")

    def delete_habit(self, name):
        """
        Deletes a habit from the tracker.
        
        Args:
            name (str): The name of the habit to delete.
        
        Raises:
            ValueError: If the habit with the given name is not found.
        """
        for habit in self.habits:
            if habit.name == name:
                self.habits.remove(habit)
                print(f"Habit '{name}' has been deleted.")
                break
        else:
            raise ValueError(f"Habit with name '{name}' not found")


    def get_longest_streak(self):
        """
        Finds the longest streak across all habits.
        
        Returns:
            int: The longest streak among all habits.
        """
        if not self.habits:
            return 0
        return max(habit.get_streak() for habit in self.habits)

    def get_habits(self):
        """
        Returns all habits currently being tracked.
        
        Returns:
            list: A list of habits.
        """
        return self.habits

    def get_habits_by_periodicity(self, periodicity):
        """
        Retrieves habits by their periodicity (daily or weekly).
        
        Args:
            periodicity (str): The periodicity to filter by ('daily' or 'weekly').
        
        Returns:
            list: A list of habits matching the given periodicity.
        
        Raises:
            ValueError: If the periodicity is invalid.
        """
        if periodicity not in ['daily', 'weekly']:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        return [habit for habit in self.habits if habit.periodicity == periodicity]

    def get_habit(self, name):
        """
        Retrieves a habit by name.
        
        Args:
            name (str): The name of the habit to retrieve.
        
        Returns:
            Habit: The habit with the given name, or None if not found.
        """
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def save_to_file(self, file_path):
        """
        Saves the current state of the habit tracker to a file.
        
        Args:
            file_path (str): The file path where the data should be saved.
        """
        data = [{
            'name': habit.name,
            'periodicity': habit.periodicity,
            'creation_date': habit.creation_date.isoformat(),
            'completions': [dt.isoformat() for dt in habit.completions]
        } for habit in self.habits]

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, file_path):
        """
        Loads the habit tracker data from a file.
        
        Args:
            file_path (str): The file path from which to load the data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

            self.habits = []
            for habit_data in data:
                # Ensure all data fields are loaded correctly
                habit = Habit(habit_data['name'], habit_data['periodicity'])
                habit.creation_date = datetime.fromisoformat(habit_data['creation_date'])
                habit.completions = [datetime.fromisoformat(dt) for dt in habit_data['completions']]
                self.habits.append(habit)

        except FileNotFoundError:
            print(f"No existing data file found at '{file_path}'. Starting with an empty tracker.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the data file at '{file_path}'. Starting with an empty tracker.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Starting with an empty tracker.")

