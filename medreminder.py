import tkinter as tk
from tkinter import messagebox
import time
import threading

def set_reminder():
    med_name = med_entry.get()
    reminder_time = time_entry.get()
    
    if not med_name or not reminder_time:
        messagebox.showerror("Error", "Please enter medication name and time.")
        return
    
    messagebox.showinfo("Reminder Set", f"Reminder set for {med_name} at {reminder_time}")
    
    def reminder():
        while True:
            current_time = time.strftime('%H:%M')
            if current_time == reminder_time:
                messagebox.showinfo("Medication Reminder", f"Time to take your {med_name}!")
                break
            time.sleep(30)  # Check time every 30 seconds
    
    threading.Thread(target=reminder, daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("Medication Reminder")
root.geometry("300x200")

tk.Label(root, text="Medication Name:").pack()
med_entry = tk.Entry(root)
med_entry.pack()

tk.Label(root, text="Reminder Time (HH:MM, 24-hour format):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Button(root, text="Set Reminder", command=set_reminder).pack()

root.mainloop()

