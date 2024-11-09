import argparse
import json
import datetime

def parse_command(command_str):
    parser = argparse.ArgumentParser(description="Task Tracker Tool")
    parser.add_argument("task-cli", type=str, help="Activate Task Tracker Tool")
    parser.add_argument("action", type=str, choices=["add", "delete", "update", "list", "mark-done", "mark-in-progress"], help="Action to perform")
    parser.add_argument("id", nargs="?", help="A unique identifier for the task")
    parser.add_argument("description", nargs="*", help="A short description of task")
    
 
    command_args = command_str.split()

    args = parser.parse_args(command_args)
    args.description = " ".join(args.description) 
    return args

def main():
    print("Welcome to Task Tracker CLI tool!!!")
    print("Type 'exit' to end session")
    
    db = []

    current_datetime = datetime.datetime.now()

    while True:
        command = input(""+"\n")
        data = {}

        if command.strip().lower == 'exit':
            print("Goodbye!!!")
            break
        
        try:
            args = parse_command(command)
            if args.action == 'add':
                data["description"] = args.id + ' ' + args.description
                data["status"] = "todo"
                data["createdAt"] = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                data["updatedAt"] = None

                try:
                    with open('db.json', "r") as file:
                        taskfiles = json.load(file)
                    data["id"] = len(taskfiles) + 1
                    taskfiles.append(data)
                    with open("db.json", "w") as file:
                        json.dump(taskfiles, file, indent=4)
                    print(f"Task added successfully (ID: {data['id']})")

                except (FileNotFoundError, json.JSONDecodeError):
                    data["id"] = 1
                    db.append(data)
                    with open("db.json", "w") as file:
                        json.dump(db, file, indent=4)
                    print(f"Task added successfully (ID: {data['id']})")

            elif args.action == 'delete':
                try:
                    with open('db.json', "r") as file:
                        taskfiles = json.load(file)

                    id = int(args.id)

                    for task in taskfiles:
                        if task['id'] == id:
                            taskfiles.remove(task)
                            with open('db.json', 'w') as file:
                                json.dump(taskfiles, file, indent=4)
                            print("Task deleted successfully")
                            break
                    else:
                        print("Task ID not found")

                except ValueError:
                    print('Invalid Id')
                    
                except (FileNotFoundError, json.JSONDecodeError):
                    print("Database NOT Found\n Add some tasks!!!")

            elif args.action == 'update':
                try:
                    with open('db.json', "r") as file:
                        taskfiles = json.load(file)

                    id = int(args.id)

                    for task in taskfiles:
                        if task['id'] == id:
                            task["description"] = args.description
                            task["updatedAt"] = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            with open('db.json', 'w') as file:
                                json.dump(taskfiles, file, indent=4)
                            print("Task updated successfully")
                            break
                    else:
                        print("Task ID not found")

                except (FileNotFoundError, json.JSONDecodeError):
                    print("Database NOT Found\n Add some tasks!!")
                except ValueError:
                    print("Invalid Id")

            elif args.action == 'list':
                try:
                    with open('db.json', "r") as file:
                        taskfiles = json.load(file)
                    alltasks = []

                    if args.id == None:
                        if taskfiles:
                            [print(task) for task in taskfiles]
                        else:
                            print('DB is empty add tasks')

                    elif args.id == "done":
                        for taskss in taskfiles:
                            if taskss['status'] == 'done':
                                alltasks.append(taskss)    
                        if alltasks:
                            [print(alltask) for alltask in alltasks]
                        else:
                            print("NOT FOUND")

                    elif args.id == "in-progress":
                        for taskss in taskfiles:
                            if taskss['status'] == 'in-progress':
                                alltasks.append(taskss)
                        if alltasks:
                            [print(alltask) for alltask in alltasks]
                        else:
                            print("NOT FOUND")

                    elif args.id == "todo":
                        for taskss in taskfiles:
                            if taskss['status'] == 'todo':
                                alltasks.append(taskss)
                        if alltasks:
                            [print(alltask) for alltask in alltasks]
                        else:
                            print("NOT FOUND")

                except (FileNotFoundError, json.JSONDecodeError):
                    print("Database NOT found\n Add some Tasks!!!")

            elif args.action == 'mark-done':
                try:
                    with open('db.json', "r") as file:
                        taskfiles = json.load(file)
                    id = int(args.id)

                    for task in taskfiles:
                        if task['id'] == id:
                            task["status"] = "done"
                            with open('db.json', 'w') as file:
                                json.dump(taskfiles, file, indent=4)
                            print("Task status updated successfully => Done")
                            break
                    else:
                        print("Task ID not found")

                except (FileNotFoundError, json.JSONDecodeError):
                    print("Database NOT found\nAdd some tasks!!")
                except ValueError:
                    print("Invalid Id")

            elif args.action == 'mark-in-progress':
                try:
                    with open('db.json', "r") as file:
                        taskfiles = json.load(file)
                    id = int(args.id)

                    for task in taskfiles:
                        if task['id'] == id:
                            task["status"] = "in-progress"
                            with open('db.json', 'w') as file:
                                json.dump(taskfiles, file, indent=4)
                            print("Task status updated successfully => In Progress")
                            break
                    else:
                        print("Task ID not found")

                except ValueError:
                    print("Invalid Id")
                except (FileNotFoundError, json.JSONDecodeError):
                    print("Database NOT found\n Add some Tasks!!!")

            else:
                print("Invalid action. Try 'add', 'delete', 'update', 'list', 'mark-done', or 'mark-in-progress'.")

    

        except SystemExit:
            print("invalid command")


if __name__ == "__main__":
    main()
