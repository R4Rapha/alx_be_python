# Ask the user to enter a task
task = input("Enter your task: ")

# Ask for the priority of the task (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes/no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# We'll build the first part of the reminder message here
match priority:
    case "high":
        # High priority: Urgent tone
        reminder_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        # Medium priority: Still important, but not urgent
        reminder_message = f"Note: '{task}' is a medium priority task"
    case "low":
        # Low priority: Not urgent, can be deferred
        reminder_message = f"Note: '{task}' is a low priority task"
    case _:
        # Catch-all for any invalid priority input
        reminder_message = f"Note: '{task}' has an unknown priority level"
# Check if task is marked as time-bound
if time_bound == "yes":
    # Append urgent action requirement
    reminder_message += " that requires immediate attention today!"
else:
    # Add a gentle suggestion
    reminder_message += ". Consider completing it when you have free time."
# Step 5: Print the final customized reminder
print("\nReminder:", reminder_message)

