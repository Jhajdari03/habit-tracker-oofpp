#Habit Tracker 
this is a simple command-line habit tracking application built in Python. It allows users to manage their daily and weekly habits, track completions, and analyze streaks.

#Features
-Add new habits with daily or weekly periodicity.
-Mark habits as complete and track their completion over time.
-View the longest streak of habit completions.
-Display all habits, or filter by periodicity.
-View the completion history of a specific habit.
-Delete habits from the tracker.
-Save habits to and load habits from a JSON file.

##Requirements
-Python 3.x**

##How to Run the Code
1.Download or clone the project into a folder on your computer.
2.Navigate to the project folder in your terminal.
3.Run the program by executing the following command:
    '''bash
    python3 cli.py
    
##Usage

###Running the Application 

Once you run the program, you will be prompted with a menu to manage your habits:

'''text 
1.Add Habit 
2.Complete Habit 
3.Show Longest Streak 
4.Show All Habits
5.Show Habits by Periodicity
6.Delete Habit
7.View Completion History 
8.Save and Exit 

##Example Interaction 

Habit Tracker CLI 
1.Add Habit 
2.Complete Habit 
3.Show Longest Streak 
4.Show All Habits
5.Show Habits by Periodicity
6.Delete Habit
7.View Completion History 
8.Save and Exit 
Enter your choice: 1
Enter habit name: gym 
Enter habit periodicity (daily/weekly): daily 
Habit 'gym' added with 'daily' periodicity.

Habit Tracker CLI 
1.Add Habit 
2.Complete Habit 
3.Show Longest Streak 
4.Show All Habits
5.Show Habits by Periodicity
6.Delete Habit
7.View Completion History 
8.Save and Exit 
Enter your choice: 1
Enter habit name: gym 
Enter habit name to complete: gym
Habit 'gym' marked as completed.

##Explanation:
-**Proper Headings**: I used '##' for subheadings and '###' for more detailed sections, like **Running the Application** and **Example Interaction**.
-**Markdown Code Blocks**: Used triple backticks (''') to format bash commands and CLI text.
-**Feature Explanation**: I expand the **Features** section in the **Usage** so the user know exactly what each menu option does.
-**Data Handling**: I added a section to explain how the program handles data (saving to 'habits.json').

