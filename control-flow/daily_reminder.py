
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()


while time_bound not in ["yes", "no"]:
    print("Invalid input. Please enter yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a HIGH priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a HIGH priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a MEDIUM priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a MEDIUM priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a LOW priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a LOW priority task. Consider completing it when you have free time.")
    case _:  
        print("Unexpected priority value entered.")
