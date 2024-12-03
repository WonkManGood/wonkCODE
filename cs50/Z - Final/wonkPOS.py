import csv
import datetime
import pathlib
import tkinter
from tkinter import ttk
from ttkbootstrap import Style

### /// WIDGETS & MAIN APPLICATION ///
class wonkPOS_window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("wonkPOS - v0.01")
        self.style = Style('darkly')
        self.window = ttk.Frame(self)

    # /// TABS ///
        self.tabs = ttk.Notebook(padding=5)
        self.tabs.pack(fill='both', expand='yes', padx=5, pady=5)
        

        self.tabs.add(wonkPOS_WelcomeTab(), text="Welcome!")
        self.tabs.add(wonkPOS_SafeTab(), text="   Safe   ")
        self.tabs.add(wonkPOS_TillsTab(), text="   Tills   ")
        self.tabs.add(wonkPOS_BanksTab(), text="   Banks   ")
        self.tabs.add(wonkPOS_DepositsTab(), text="Deposits")

class wonkPOS_WelcomeTab(ttk.Frame):
    def __init__(self, *args):
        super().__init__(*args)

        column_1 = ttk.Frame(self, padding=10) 
        column_1.grid(row=0, column=0, sticky="news")
        column1_display = ttk.LabelFrame(column_1, text="Welcome", padding=10)
        column1_display.pack(side="top", fill="both", expand='yes')
        # /// CONTENT ///

        testbox = ttk.Checkbutton(column1_display, text='ass', variable="testbox")
        testbox.pack(fill='x', pady=4)

class wonkPOS_SafeTab(ttk.Frame):
    def __init__(self, *args):
        super().__init__(*args)

        # /// CONTENT ///

class wonkPOS_TillsTab(ttk.Frame):
    def __init__(self, *args):
        super().__init__(*args)

        # /// CONTENT ///

class wonkPOS_BanksTab(ttk.Frame):
    def __init__(self, *args):
        super().__init__(*args)

        # /// CONTENT ///

class wonkPOS_DepositsTab(ttk.Frame):
    def __init__(self, *args):
        super().__init__(*args)

        # /// CONTENT ///


# ///

# ///


# STARTS APP
if __name__ == '__main__':
    wonkPOS_window().mainloop()