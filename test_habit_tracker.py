import unittest
from habit_tracker import Habit, HabitTracker

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = HabitTracker()

    def test_add_and_get_habit(self):
        self.tracker.add_habit("Read", "daily")
        habit = self.tracker.get_habit("Read")
        self.assertEqual(habit.name, "Read")
        self.assertEqual(habit.periodicity, "daily")

    def test_delete_habit(self):
        self.tracker.add_habit("Read", "daily")
        self.tracker.delete_habit("Read")
        self.assertIsNone(self.tracker.get_habit("Read"))

if __name__ == "__main__":
    unittest.main()
