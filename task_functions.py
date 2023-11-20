import pandas as pd
import csv
from tkinter import filedialog
import tkinter as tk
from dialogs import TimeframeDialog

path = ""

def add_task(task_entry, treeview, root):
    task = task_entry.get()
    if task != "":
        dialog = TimeframeDialog(root)
        timeframe = dialog.time_result
        importance = dialog.importance_result
        if timeframe and importance:
            treeview.insert('', 'end', values=(task, timeframe, importance), tags=("undone",))
    task_entry.delete(0, tk.END)


def delete_task(treeview):
    try:
        selected_item = treeview.selection()[0]
        treeview.delete(selected_item)
    except:
        pass


def load_tasks(treeview):
    global path
    path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Load Tasks")
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
        except:
            pass


def save_tasks(treeview):
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


def toggle_task_done(event, treeview):
    try:
        selected_item = treeview.selection()[0]
        task, timeframe, importance = treeview.item(selected_item)['values']
        if treeview.item(selected_item, "tags") == ("done",):
            treeview.item(selected_item, tags=("undone",))
        else:
            treeview.item(selected_item, tags=("done",))
    except:
        pass


def switch_table(treeview, grouped_treeview):
    if treeview.winfo_viewable():
        treeview.grid_remove()
        update_grouped_table(grouped_treeview)
        grouped_treeview.grid()
    else:
        grouped_treeview.grid_remove()
        treeview.grid()


def update_grouped_table(grouped_treeview):
    for i in grouped_treeview.get_children():
        grouped_treeview.delete(i)

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
