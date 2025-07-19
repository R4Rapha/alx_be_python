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

# Customized message logic
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

# Final print statement
print(f"\n{reminder}")