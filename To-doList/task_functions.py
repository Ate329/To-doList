import pandas as pd
import csv
from tkinter import filedialog, ttk, messagebox
import tkinter as tk
from dialogs import TimeframeDialog
import os

path = ""

def add_task(task_entry: tk.Entry, treeview: ttk.Treeview, root):
    task = task_entry.get()
    if task != "":
        dialog = TimeframeDialog(root)
        timeframe = dialog.time_result.ctime()
        importance = dialog.importance_result
        if timeframe and importance:
            treeview.insert('', 'end', values=(task, timeframe, importance), tags=("undone",))
    task_entry.delete(0, tk.END)


def delete_task(treeview: ttk.Treeview):
    try:
        selected_item = treeview.selection()[0]
        treeview.delete(selected_item)
    except:
        pass


def startup_load_tasks(event, treeview: ttk.Treeview):
    global path
    if os.path.exists('path.txt'):
        with open('path.txt', 'r') as file:
            path = file.read()

        if path:
            try:
                treeview.delete(*treeview.get_children())
                with open(path, 'r', newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        task, timeframe, importance, *status = row
                        status = tuple(status)
                        treeview.insert('', 'end', values=(task, timeframe, importance), tags=status)
            except:
                pass


def load_tasks(treeview: ttk.Treeview):
    global path
    path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Load Tasks")

    '''
    uneccesary weird code
    with open('path.txt', 'w'):
        pass
    '''
    
    with open('path.txt', 'w') as file:
        file.write(path)
        file.close()

    # print(path) use for debug
    if path:
        try:
            treeview.delete(*treeview.get_children())
            with open(path, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    task, timeframe, importance, *status = row
                    status = tuple(status)
                    treeview.insert('', 'end', values=(task, timeframe, importance), tags=status)
        except Exception as exception:
            messagebox.showerror(f"Exception encountered!", f"Exception encountered in Python program when loading tasks from CSV file.")
    else:
        print("Failed to determine loading path!")
        messagebox.showerror("Error", "Loading failed.")


def save_tasks(treeview: ttk.Treeview):
    path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                        filetypes=[("CSV files", "*.csv")], 
                                        title="Save Tasks", 
                                        initialfile='TodoList.csv')
    if path:
        tasks = treeview.get_children()
        tasks_to_save = [(treeview.item(task)['values'], treeview.item(task, "tags")) for task in tasks]
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            for task in tasks_to_save:
                writer.writerow(task[0] + list(task[1]))


def toggle_task_done(event, treeview: ttk.Treeview):
    try:
        selected_item = treeview.selection()[0] # Add currently selected (highlighted) item
        task, timeframe, importance = treeview.item(selected_item)['values']
        if treeview.item(selected_item, "tags") == ("done",):
            treeview.item(selected_item, tags=("undone",))
        else:
            treeview.item(selected_item, tags=("done",))
    except:
        pass

def update_grouped_table(grouped_treeview) -> bool:
    print(f"Set path: {path}")
    for i in grouped_treeview.get_children():
        grouped_treeview.delete(i)
    if not path:
        messagebox.showerror("ERROR", "Path of CSV file not set!\nRun Load Tasks button first to select a filepath!")
        return False # Path error -> halt execution
    df = pd.read_csv(path, header=None, names=["Task", "Timeframe", "Importance", "tags"])
    grouped = df.groupby("Importance")["Task"].apply(list)
    tasks_by_importance = {"Extreme": [], "High": [], "Medium": [], "Low": [], "Idle": []}

    for importance, tasks in grouped.items():
        tasks_by_importance[importance] = tasks

    max_tasks = max(len(tasks) for tasks in tasks_by_importance.values())

    for i in range(max_tasks):
        row = []
        for importance in ["Extreme", "High", "Medium", "Low", "Idle"]:
            if i < len(tasks_by_importance[importance]):
                row.append(tasks_by_importance[importance][i])
            else:
                row.append("")
        grouped_treeview.insert('', 'end', values=row)
    return True # Successfully updated grouped_treeview -> switch_table procedure can proceed

def switch_table(treeview, grouped_treeview: ttk.Treeview):
    if treeview.winfo_viewable():
        # How did you update grouped_treeview from within the inner function??
        success = update_grouped_table(grouped_treeview)
        if not success: 
            return # Early return if not success aka. Path not set 
        treeview.grid_remove()
        grouped_treeview.grid()
    else:
        grouped_treeview.grid_remove()
        treeview.grid()


