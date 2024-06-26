from tabulate import tabulate


def main():
    #print to-do list application with underline format
    print("\n\033[4mTo-Do List Application\033[0m")
    print()
    #create task_list list and total tasks number
    task_list = []
    total_tasks = 0

    while True:
        request = get_input()

        if request == "A":
            task_list, total_tasks = add(task_list, total_tasks)

        elif request == "D":
            task_list = delete(task_list)

        elif request == "E":
            task_list = edit(task_list)

        elif request == "V":
            view(task_list)

        else:
            break

def get_input():
    #create legend for keys and corresponding actions
    legend = [
        {"Key": "A", "Request": "Add a Task"},
        {"Key": "D", "Request": "Delete a Task"},
        {"Key": "E", "Request": "Edit a Task"},
        {"Key": "V", "Request": "View Task List"},
        {"Key": "Q", "Request": "Quit"}
    ]

    while True:
        #print legend in a table format using tabulate
        print(tabulate(legend, headers="keys", tablefmt="presto"))
        print()
        #get user input for the request
        request = input("What would you like to do? ").upper()
        print()

        #if the request matches a letter in the key list, return the request. if not, prompt for another try
        if request in ["A", "D", "E", "V", "Q"]:
            return request
        else:
            print("Invalid input. Please try again.")


#print the current table of tasks using tabulate
def view(todos):
    print(tabulate(todos, headers="keys", tablefmt="presto"))
    print()

#add a task to the todo list
def add(todos, n):
    #get user input for taskt to add
    task = input("Task: ")
    print()
    #use variable to count number for task
    n += 1
    #add the task to todos list
    todos.append({"#": n, "Task": task})
    return todos, n

#delete a task in the list
def delete(todos):
    task_numbers = list(task["#"] for task in todos)

    while True:
        #view the current list
        view(todos)
        #try to match the number of task to a task in the list
        try:
            #get input from user
            task_number = int(input("Which task would you like to delete? "))
            print()
            #if number is in list, break from loop, if not print error message
            if task_number in task_numbers:
                break
            else:
                print("Invalid task #. Please try again.")
                print()
        #if invalid input and value error, print error message
        except ValueError:
            print("Invalid input. Please enter the task #.")
            print()

    #check the range of numbers in the list
    for num in range(len(todos)):
        #remove the list item that matches the number input by user
        if todos[num]["#"] == task_number:
            todos.remove(todos[num])
            break

    return todos

#edit a task in the list
def edit(todos):
    task_numbers = list(task["#"] for task in todos)

    while True:
        view(todos)
        #try to read user input for task number, if value error print error message
        try:
            #get user input
            task_number = int(input("Which task would you like to edit? "))
            #if the number is in the task list, break out of loop, if not print error message
            if task_number in task_numbers:
                break
            else:
                print("Invalid task #. Please try again.")
                print()

        except ValueError:
            print("Invalid input. Please enter the task #.")
            print()

    #get user input for new task edit
    new_task = input("New task: ")
    print()
    #find task associated with task number and put new task in the place of old one
    for task in todos:
        if task["#"] == task_number:
            task["Task"] = new_task

    return todos


if __name__ == "__main__":
    main()
