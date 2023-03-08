# add items to the list
def add(task_name):
    # add item to the list
    # assign false as task done by default
    return [task_name, False]


def check_off(task_list):
    display_list(task_list)
    taskIndex = int(input("Enter the index of the item to check off:: "))
    # if they choose the item that is already checked
    if task_list[taskIndex - 1][1]:
        print("It was already checkoff.")
    else:
        print("Item #" + str(taskIndex) + " checkoff.")
        task_list[taskIndex - 1][1] = True

    userChoice = input("Do you want to input another index (y/n)? ")
    while userChoice != 'y' and userChoice != "n":
        print("Enter a valid answer.")
        userChoice = input("Do you want to input another index (y/n)? ")

    if userChoice == 'y':
        check_off(task_list)


def display_list(task_list):
    print("-To Do List-")
    if len(task_list) == 0:
        print("There is no task in the list.")
    else:

        for i in range(len(task_list)):
            if task_list[i][1]:
                print(str(i + 1) + ". [X] ", end='')
            else:
                print(str(i + 1) + '. [ ] ', end='')
            print(task_list[i][0])
    print()