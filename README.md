

---

<div align="center">
    
  # Task Tracker CLI

</div>
  
---

## Overview

Task tracker is a project used to track and manage your tasks. With this project, you can track what you need to do, what you have done, and what you are currently working on. It stores tasks in JSON file for data preservation. This project will helps you keep up with all of your activites
## Features

- **Task Handling**: Add, update, and delete tasks using unique ID.
- **Task Status**: Mark tasks as `todo`, `in-progress`, or `done`.
- **Task Listing**: List all tasks or filter them by their status (`todo`, `in-progress`, `done`).
- **Task Storage**: Tasks are stored in a JSON file, ensuring data is well preserved.

###  Installation
  Ensure you have **Python** Installed
  
  Clone the repository:

   ```bash
   git clone https://github.com/Omarko65/TaskTrackerCLI
   cd TaskTrackerCLI
   ```

##  Usage

- **Start by running the app**:

  ```bash
  python main.py
  # Output: Welcome to Task Tracker CLI tool!!!
  #         Type 'exit' to end session
  ```

- **Add a task**:

  ```bash
  task-cli add "Visit Sam"
  # Output: Task Task added successfully (ID: 1)
  ```

- **Update a task**:

  ```bash
  task-cli update 1 "Go to the mall"
  # Output: Task updated successfully!
  ```

- **Mark progress of tasks**:

  ```bash
  task-cli mark-done 1
  # Ouput: Task status updated successfully => Done
  task-cli mark-in-progress 1
  # Output: Task status updated successfully => In Progress
  ```

- **Listing tasks by status**:

```bash
 task-cli list done
 task-cli list todo
 task-cli list in-progress
 ```

- **Deleting a task**:

  ```bash
  task-cli delete 1
  # Output: Task deleted successfully
  ```

  - **Exiting**:
  ```bash
  exit
  # Output: Goodbye!!!
  ```


## CC
https://roadmap.sh/projects/task-tracker
