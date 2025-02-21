import os
import tkinter as tk
from tkinter import Label, Button

# Create an instance of tkinter frame or window
window = tk.Tk()

# Set the size of the tkinter window
window.geometry("800x400")
window.title("Shutdown, Restart & Logout")  # Set the title of the window

# Create a label
head = Label(window, text="Shutdown, Restart and Logout Using PC", font=('Calibri', 20, 'bold'))
head.pack(pady=30)

# Define functions for shutdown, restart, and logout
def shutdown():
    os.system("shutdown /s /t 0")

def restart():
    os.system("shutdown /r /t 0")

def logout():
    os.system("shutdown /l")

# Create buttons with appropriate colors and larger text
Button(window, text='Shutdown', command=shutdown, font=('normal', 14), bg='red', fg='white').pack(pady=15)
Button(window, text='Restart', command=restart, font=('normal', 14), bg='blue', fg='white').pack(pady=15)
Button(window, text='Logout', command=logout, font=('normal', 14), bg='green', fg='white').pack(pady=15)

# Run the main loop
window.mainloop()