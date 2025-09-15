task = input("Enter your task:")
priority = input("Priority (high/medium/low):").strip().lower()
time_bound = input("Is it time-bound (yes/no):").strip().lower()
match (priority, time_bound):
    case ('high', 'yes'):
        print(f"Reminder: {task} is a high priority task and requires immediate attention today!")
    case ('low', 'no'):
        print(f"{task} is a low priority task. Consider completing it when you have a free time.")
