import unittest
from analytics import get_longest_streak, get_streak_for_habit
import json

with open('habits.json') as f:
    habits = json.load(f)

class TestAnalytics(unittest.TestCase):
    def test_get_longest_streak(self):
        longest = get_longest_streak(habits)
        self.assertIsInstance(longest, int)

    def test_get_habit_streak(self):
        streak = get_streak_for_habit(habits, "Exercise")
        self.assertIsInstance(streak, int)

if __name__ == "__main__":
    unittest.main()
