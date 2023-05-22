# Medication-Remainder
The Medication Reminder Prototype is a simple application designed to help users keep track of their medications and receive reminders for taking them on time.

User Interface:

The prototype uses the Tkinter library to create a graphical user interface (GUI) for the application.
The interface consists of input fields and buttons to add medications and view the medication schedule.

Database Connection:

The prototype utilizes SQLite, a lightweight database, to store medication information.
It establishes a connection to the database using the sqlite3 library in Python.
The medication details are stored in a table called "medications" with columns for id, name, dosage, frequency, and next_dose.

Adding Medications:

Users can enter the name, dosage, and frequency of their medications in the corresponding input fields.
When the "Add Medication" button is clicked, the application retrieves the entered information.
It calculates the next dose time by adding the frequency (in hours) to the current time using the datetime library in Python.
The medication details are then inserted into the "medications" table in the database.

Viewing the Medication Schedule:

Clicking the "View Schedule" button triggers the show_schedule() function.
The function retrieves the medication data from the database using a SELECT query.
It iterates over the retrieved rows and constructs a string representation of the medication schedule.
The schedule is displayed in a messagebox using the tkinter.messagebox library.

GUI Interaction:

The GUI elements, such as labels, entry fields, and buttons, are created and placed in the application window using Tkinter.
Users can enter medication details in the corresponding entry fields.
The "Add Medication" button triggers the add_medication() function to add the medication to the database and clear the entry fields.
The "View Schedule" button triggers the show_schedule() function to display the medication schedule in a messagebox.

Closing the Application:

The main event loop is started using the window.mainloop() function, which keeps the application window open until it is closed.
When the application window is closed, the connection to the database is closed using conn.close().



# Features
1 Add medications with their name, dosage, and frequency.

2 Calculate and display the next dose time based on the medication frequency.

3 View the medication schedule.

# Prerequisites
Python 3.x

Tkinter library

SQLite library

# Installation
Clone the repository or download the source code.

Navigate to the project directory.

cd medication-reminder

Install the required dependencies.

pip install tkinter
# Usage
1.Run the application by executing the following command:
python medication_reminder.py

2.The application window will appear.

3.To add a medication:

Enter the medication name, dosage, and frequency in the respective fields.

Click the "Add Medication" button.

A messagebox will indicate that the medication has been added successfully.
To view the medication schedule:

4.Click the "View Schedule" button.
 A messagebox will display the current medication schedule.
 Repeat steps 3 and 4 as needed to manage medications and view the schedule.

To exit the application, simply close the application window.
# Acknowledgments

The Medication Reminder Prototype was developed using Python and the Tkinter library.

The SQLite library was used for data storage.
