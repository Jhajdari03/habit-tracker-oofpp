# Habit Tracker
A simple command-line habit tracking application built in Python for the IU course **Object-Oriented and Functional Programming with Python (DLBDSOOFPP01)**.

It allows users to manage daily and weekly habits, track completions, and analyze streaks using both object-oriented and functional programming paradigms.

---

## 📦 Features 

- Add new habits with daily or weekly periodicity
- Mark habits as completed and track their history 
- View longest overall streaks and track their history
- Display all habits or filter by periodicity
- View completion history for any habit
- Delete habits
- Save/load habit data to/from a JSON file
- Modular analytics system using **pure functions**

---

## 🛠️ Project Structure 
| File | Description |
|------|-------------|
| cli.py | Command-line interface for user interaction |
| habit_tracker.py | Object-Oriented logic for managing habits |
| analytics.py | Functional Programming module for analysis|
| habits.json | Sample user data with 4+ weeks of habit tracking |
| test_analytics.py | Unit tests for core habit logic | 
| test_habit_tracker.py | Unit tests for core habit logic |
| .gitignore | Excludes unnecessary files from Github |
| README.md | This documentation file | 

---

## 🐍 Requirements 

- Python 3.x

----

## ▶️ How to Run

### Setup

1. Download or clone the repository 
2. Open terminal and navigate to the project directory: 
   ```bash
   cd /path/to/project/folder
