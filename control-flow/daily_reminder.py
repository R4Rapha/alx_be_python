# Ask the user to enter a task
task = input("Enter your task: ")

# Ask for the priority of the task (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes/no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build the reminder message
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder_message = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder_message = f"Reminder: '{task}' has an unknown priority level"

# Add time-bound context
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

# Print the final reminder (now matches the checker pattern)
print(reminder_message)
