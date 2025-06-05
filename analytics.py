from datetime import datetime, timedelta

def get_all_habits(habits):
    return [habit['name'] for habit in habits]

def get_habits_by_periodicity(habits, period):
    return list(filter(lambda h: h['periodicity'] == period, habits))

def calculate_streak(completions, periodicity):
    if not completions:
        return 0

    completions = sorted([datetime.fromisoformat(c) for c in completions], reverse=True)
    streak = 1
    last = completions[0]

    for current in completions[1:]:
        if periodicity == "daily" and (last - current).days == 1:
            streak += 1
            last = current
        elif periodicity == "weekly" and 0 < (last - current).days <= 7:
            streak += 1
            last = current
        else:
            break

    return streak

def get_longest_streak(habits):
    return max([calculate_streak(h['completions'], h['periodicity']) for h in habits], default=0)

def get_streak_for_habit(habits, name):
    habit = next((h for h in habits if h['name'].lower() == name.lower()), None)
    if habit:
        return calculate_streak(habit['completions'], habit['periodicity'])
    return 0
