# Ask the user for the task
task = input("Enter your task: ")

# Ask the user for the priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to customize the message based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task"
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority"

# Use if to check if task is time-sensitive and adjust the reminder
if time_bound == "yes":
    reminder += " and it requires immediate action!"
else:
    reminder += " and can be done at your convenience."

# Final print statement
print(f"\n{reminder}")