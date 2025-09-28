def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("5. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to your list")
        elif choice == "2":
            item = input("Enter the item to be remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has removed from your list")
            else:
                print(f"{item} not found in the list")
        elif choice == "3":
            if shopping_list:
                for i in range(len(shopping_list)):
                    print(f"{i}, {shopping_list[i]}")
            else:
                print("Your list is empty")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()