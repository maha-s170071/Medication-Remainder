import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

# Create a database connection
conn = sqlite3.connect('medications.db')
c = conn.cursor()

# Create a table for medications
c.execute('''CREATE TABLE IF NOT EXISTS medications
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             dosage TEXT,
             frequency INTEGER,
             next_dose TEXT)''')

# Function to add a new medication
def add_medication():
    name = name_entry.get()
    dosage = dosage_entry.get()
    frequency = frequency_entry.get()

    # Calculate the next dose time
    current_time = datetime.datetime.now()
    next_dose = current_time + datetime.timedelta(hours=int(frequency))

    # Insert the medication into the database
    c.execute("INSERT INTO medications (name, dosage, frequency, next_dose) VALUES (?, ?, ?, ?)",
              (name, dosage, frequency, next_dose))
    conn.commit()

    # Clear the input fields
    name_entry.delete(0, tk.END)
    dosage_entry.delete(0, tk.END)
    frequency_entry.delete(0, tk.END)

    messagebox.showinfo("Medication Reminder", "Medication added successfully!")

# Function to display the medication schedule
def show_schedule():
    schedule = ""
    c.execute("SELECT name, dosage, next_dose FROM medications")
    medications = c.fetchall()
    for medication in medications:
        name, dosage, next_dose = medication
        schedule += f"Name: {name}, Dosage: {dosage}, Next Dose: {next_dose}\n"
    messagebox.showinfo("Medication Schedule", schedule)

# Create the main window
window = tk.Tk()
window.title("Medication Reminder")

# Create labels and entry fields
name_label = tk.Label(window, text="Medication Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

dosage_label = tk.Label(window, text="Dosage:")
dosage_label.pack()
dosage_entry = tk.Entry(window)
dosage_entry.pack()

frequency_label = tk.Label(window, text="Frequency (in hours):")
frequency_label.pack()
frequency_entry = tk.Entry(window)
frequency_entry.pack()

# Create buttons
add_button = tk.Button(window, text="Add Medication", command=add_medication)
add_button.pack()

schedule_button = tk.Button(window, text="View Schedule", command=show_schedule)
schedule_button.pack()

# Start the main event loop
window.mainloop()

# Close the database connection
conn.close()
