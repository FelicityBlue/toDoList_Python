import toDoList

user_choice = ''
taskList = []


# print all the choices user can make
def print_action():
    print("1. add item to the list")
    print("2. check off the item")
    print("3. Display the list")
    print("4. exit the program")

while user_choice != str(4):
    print_action()
    user_choice = input("Enter the index of the action :: ")
    while not user_choice.isdigit():
        print("Enter an integer.")
        user_choice = input("Enter the index of the action :: ")

    if user_choice == str(1):
        choice = 'y'
        while choice == "y":
            # ask for the name of the task
            itemName = input("Enter the task name:: ")
            taskList.append(toDoList.add(itemName))

            # ask if the user want to add another item
            choice = input("Do you want to add an another item (y/n)? ")
            choice.replace(" ", "")

            # If the input is not valid then ask for it again
            while choice != 'y' and choice != "n":
                print("Enter a valid answer.")
                choice = input("Do you want to add an another item (y/n)? ")
                choice.replace(" ", "")
        print()

    elif user_choice == str(2):
        toDoList.check_off(taskList)

    elif user_choice == str(3):

        toDoList.display_list(taskList)

    elif user_choice != str(4):
        print("Enter a valid choice.\n")

print("Thank you for using the program\nHave a great day!")
