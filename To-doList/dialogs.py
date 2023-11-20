import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk


class TimeframeDialog(tk.simpledialog.Dialog):
    def body(self, master):
        ttk.Label(master, text="Enter the time for the task:").grid(row=0)
        self.time_entry = ttk.Entry(master)
        self.time_entry.grid(row=1)

        ttk.Label(master, text="Select the importance of the task:").grid(row=2)
        self.importance_entry = ttk.Combobox(master, values=["Extreme", "High", "Medium", "Low", "Idle"])
        self.importance_entry.grid(row=3)
        return self.time_entry


    def apply(self):
        self.time_result = self.time_entry.get()
        self.importance_result = self.importance_entry.get()
