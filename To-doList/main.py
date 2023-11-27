from tkinter import ttk
from ttkthemes import ThemedTk
from task_functions import add_task, delete_task, load_tasks, save_tasks, toggle_task_done, switch_table, update_grouped_table, startup_load_tasks

root = ThemedTk(theme="arc")
root.title("To-Do List")

style = ttk.Style(root)
style.configure("Treeview", rowheight=25) 

grouped_treeview = ttk.Treeview(root, columns=("Extreme", "High", "Medium", "Low", "Idle"), show="headings")
grouped_treeview.heading("Extreme", text="Extreme")
grouped_treeview.heading("High", text="High")
grouped_treeview.heading("Medium", text="Medium")
grouped_treeview.heading("Low", text="Low")
grouped_treeview.heading("Idle", text="Idle")

grouped_treeview.column("Extreme", width=120)
grouped_treeview.column("High", width=120)
grouped_treeview.column("Medium", width=120)
grouped_treeview.column("Low", width=120)
grouped_treeview.column("Idle", width=120)

grouped_treeview.grid(row=1, column=0, sticky='nsew')
grouped_treeview.grid_remove()

treeview = ttk.Treeview(root, columns=("Task", "Timeframe", "Importance"), show="headings")
treeview.heading("Task", text="Task")
treeview.heading("Timeframe", text="Deadline")
treeview.heading("Importance", text="Importance")
treeview.grid(row=1, column=0, sticky='nsew')

task_entry = ttk.Entry(root, width=50) 
task_entry.grid(row=2, column=0, sticky='nsew')

treeview.bind("<Double-1>", lambda event: toggle_task_done(event, treeview))

treeview.tag_configure("done", foreground="grey")
treeview.tag_configure("undone", foreground="black")

# Buttons & position
add_button = ttk.Button(root, text="Add Task", command=lambda: add_task(task_entry, treeview, root)) 
add_button.grid(row=3, column=0, sticky='nsew')

complete_button = ttk.Button(root, text="Complete Task (Hotkey=<Double-1>?)", command=lambda: toggle_task_done(treeview))
complete_button.grid(row=4, column=0, sticky='nsew')

delete_button = ttk.Button(root, text="Delete Task", command=lambda: delete_task(treeview)) 
delete_button.grid(row=5, column=0, sticky='nsew')

load_button = ttk.Button(root, text="Load Tasks", command=lambda: load_tasks(treeview)) 
load_button.grid(row=6, column=0, sticky='nsew')

save_button = ttk.Button(root, text="Save Tasks", command=lambda: save_tasks(treeview))
save_button.grid(row=7, column=0, sticky='nsew')

switch_button = ttk.Button(root, text="Switch View", command=lambda: switch_table(treeview, grouped_treeview))
switch_button.grid(row=8, column=0, sticky='nsew')

startup_load_tasks(None, treeview)

root.mainloop()
