import time
import tkinter as tk
import ttkbootstrap as ttk
from time import strftime


def update_time():
        string_time = strftime('%H:%M:%S %p')
        time_label.config(text = string_time)
        time_label.after(1000, update_time)    

def display_timer():
        alt_entry.pack() 
        timer_state_button.pack()
        

def set_timer():
        alt_entry.pack_forget()
        timer_state_button.pack_forget()
        alt_entry_text = alt_entry.get()    
        alt_entry['text'] = alt_entry_text
        print(alt_entry_text)
        timer_label.pack()
        timer_label.config(text = alt_entry_text)
        
       


# create window
window = ttk.Window(themename = 'darkly')
window.title('Alarm Clock')
window.geometry('750x450')

# main 
time_frame = ttk.Frame(window)
time_label = ttk.Label(time_frame, font=("Arial", 48), anchor="center", foreground = 'red')
alt_entry = ttk.Entry(time_frame)

# timer button
timer_frame = ttk.Frame(window)
timer_button = ttk.Button(timer_frame, text = 'timer', command = display_timer)
timer_state_button = ttk.Button(time_frame, text = 'start', command = set_timer)
timer_label = ttk.Label(time_frame)


# grid  
window.columnconfigure(0, weight= 1)
window.columnconfigure(1, weight= 1)
window.columnconfigure(2, weight= 1)
window.columnconfigure(3, weight= 1)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)

# main pack
time_frame.grid(row =1, column = 1, columnspan = 2, sticky = 'nsew')
time_label.pack( fill = 'both')
alt_entry.pack_forget()

# timer pack
timer_frame.grid(row = 0, column = 0, sticky = 'nsew')
timer_button.pack(expand = 'true', fill = 'both')
timer_state_button.pack_forget()
timer_label.pack_forget()


# run

update_time()
window.mainloop()  