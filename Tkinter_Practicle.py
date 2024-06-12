#1 Create clickable buttons to trigger actions
import tkinter as tk

# Function to be called when the button is clicked
def on_button_click():
    print("Button was clicked!")

def on_another_button_click():
    print("Another button was clicked!")

# Create the main application window
root = tk.Tk()
root.title("Button Click Example")
root.geometry("300x200")

# Create a button and assign the on_button_click function to be called when the button is clicked
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=20)

# Create another button with a different action
another_button = tk.Button(root, text="Click Me Too!", command=on_another_button_click)
another_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

#2 Display dialog boxes for messages, warning etc.

import tkinter as tk
from tkinter import messagebox

# Function to display an information dialog
def show_info():
    messagebox.showinfo("Information", "This is an information dialog")

# Function to display a warning dialog
def show_warning():
    messagebox.showwarning("Warning", "This is a warning dialog")

# Function to display an error dialog
def show_error():
    messagebox.showerror("Error", "This is an error dialog")

# Function to display a confirmation dialog
def ask_question():
    result = messagebox.askquestion("Question", "Do you want to proceed?")
    if result == 'yes':
        messagebox.showinfo("Response", "You chose to proceed")
    else:
        messagebox.showinfo("Response", "You chose not to proceed")

# Create the main application window
root = tk.Tk()
root.title("Dialog Box Example")
root.geometry("300x200")

# Create buttons to trigger the dialog boxes
info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.pack(pady=10)

warning_button = tk.Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=10)

error_button = tk.Button(root, text="Show Error", command=show_error)
error_button.pack(pady=10)

question_button = tk.Button(root, text="Ask Question", command=ask_question)
question_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()



