import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
import datetime as dt
import time as t
import tkcalendar as tkc

class TimeframeDialog(tk.simpledialog.Dialog):
    def body(self, master):
        ttk.Label(master, text="Enter the end date for the task:").grid(row=0, column=0)
        today_time = t.localtime()
        self.time_entry = tkc.DateEntry(master)
        self.time_entry.grid(row=0, column=1)

        ttk.Label(master, text="Select the importance of the task:").grid(row=1)
        self.importance_entry = ttk.Combobox(master, values=["Extreme", "High", "Medium", "Low", "Idle"])
        self.importance_entry.grid(row=2)
        return self.time_entry


    def apply(self):
        self.time_result:dt.date = self.time_entry.get_date()
        self.importance_result = self.importance_entry.get()
