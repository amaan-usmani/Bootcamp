import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Revision")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a text widget
text = tk.Text(root)
text.pack()

# Run the Tkinter event loop
root.mainloop()
