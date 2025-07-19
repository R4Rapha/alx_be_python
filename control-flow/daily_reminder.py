# Ask the user to enter a task
task = input("Enter your task: ")

# Ask for the priority of the task (high/medium/low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes/no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Print a reminder message based on the priority and time-bound status
if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
elif priority == "medium":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
elif priority == "low":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
else:
    if time_bound == "yes":
        print(f"Reminder: '{task}' has an unknown priority level that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' has an unknown priority level. Consider completing it when you have free time.")
