# To-doList
This is a simple To-Do List application implemented in Python using the Tkinter library for the graphical user interface. The application allows users to add, delete, load, and save tasks. It also provides the functionality to mark tasks as done or undone. Additionally, the application supports switching between a detailed task view and a grouped view based on level of importance of each task.


# Files and Modules
## Main.py
This file serves as the main entry point for the application. It initializes the Tkinter window, sets up the UI components, and defines the main event loop.    

## dialogs.py
This module contains the **"TimeframeDialog"** class, a custom dialog for capturing task timeframes and importance. 

## task_functions.py
This module contains various functions related to task management, including adding and deleting tasks, loading and saving tasks from/to CSV files, toggling task completion status, and updating the grouped view. 


# How to use
1. Run Main.py to start the To-Do List application.     

2. Use the buttons to add, delete, load and save tasks.    

3. Double-click on a task in the list to mark it as done or undone.     

4. Switch between the detailed and grouped view using the "Switch Table" button.    

**Note: Make sure to have the required libraries (tkinter, ttkthemes, pandas) installed before running the application.**   

Or you can install the libraries by (Recommended)     
```python
pip install -r requirements.txt
```

Or  
```python
pip install ttkthemes pandas tkcalendar
```


# License
This project is licensed under the MIT - see the LICENSE.md file for details.
