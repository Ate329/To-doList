# To-doList
This is a simple To-Do List application implemented in Python using the Tkinter library for the graphical user interface. The application allows users to add, delete, load, and save tasks. It also provides the functionality to mark tasks as done or undone. Additionally, the application supports switching between a detailed task view and a grouped view based on level of importance of each task.


# Files and Modules
## Main.py
This file serves as the main entry point for the application. It initializes the Tkinter window, sets up the UI components, and defines the main event loop.    

## dialogs.py
This module contains the **"TimeframeDialog"** class, a custom dialog for capturing task timeframes and importance. 

## task_functions.py
This module contains various functions related to task management, including adding and deleting tasks, loading and saving tasks from/to CSV files, toggling task completion status, and updating the grouped view. 

## Pictures
![Screenshot 2023-11-23 123442](https://github.com/Ateee329/To-doList/assets/74974216/c0843791-e28e-4a19-adf4-48d5648bca5e)
![Screenshot 2023-11-23 123527](https://github.com/Ateee329/To-doList/assets/74974216/f00d655c-caa6-4486-93a1-161f081bc3de)


# How to use
1. Run Main.py to start the To-Do List application.     

2. Use the buttons to add, delete, load and save tasks.    

3. Double-click on a task in the list to mark it as done or undone.     

4. Switch between the detailed and grouped view using the "Switch Table" button.    

**Note: Make sure to have the required libraries (tkinter, ttkthemes, pandas) installed before running the application.**   

Or you can install the libraries by     
```python
pip install requirements.txt
```

Or  
```python
pip install ttkthemes pandas
```


# License
This project is licensed under the MIT - see the LICENSE.md file for details.
