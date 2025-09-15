task = input("Enter your task:")
priority = input("Priority (high/medium/low):").strip().lower()
time_bound = input("Is it time-bound? (yes/no):").strip().lower()

if priority == 'high' and time_bound == 'yes':
    print(f"Reminder: {task} is a high priority task and requires immediate attention today!")
elif priority == 'low' and time_bound == 'no':
    print(f"{task} is a low priority task. Consider completing it when you have a free time.")
