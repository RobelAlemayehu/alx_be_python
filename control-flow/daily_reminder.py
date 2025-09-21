task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: {task} is a HIGH priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a HIGH priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: {task} is a MEDIUM priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a MEDIUM priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: {task} is a LOW priority task that requires attention today!")
        else:
            print(f"Note: {task} is a LOW priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")
