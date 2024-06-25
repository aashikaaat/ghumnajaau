import tkinter as tk
from tkinter import ttk 

# Function to apply dark mode
def apply_dark_mode(root):
    style = ttk.Style()

    # Set the theme to 'clam' to allow custom styling
    style.theme_use('clam')

    # Configure the style for various widgets
    style.configure('TFrame', background='#2e2e2e')
    style.configure('TLabel', background='#2e2e2e', foreground='#ffffff')
    style.configure('TButton', background='#444444', foreground='#ffffff')
    style.map('TButton', background=[('active', '#666666')])

    # Configure the main window
    root.configure(bg='#2e2e2e')

# Create the main window
root = tk.Tk()
root.title("Tkinter Dark Mode")
root.geometry("1920x1080")

# Apply dark mode
apply_dark_mode(root)



root = tk.Tk() #TK le window peoject open garcha
root.minsize(width = 500, height = 620)
root.maxsize(width = 1920, height = 1080)
root.iconbitmap('a logo.ico')
label = tk.Label (root, text = "Window")
label.pack()

bgimg= tk.PhotoImage(file = "login page photo.png" )
#Specify the file name present in the same directory or else
#specify the proper path for etrieving the image to set it as background image.


limg= tk.Label(root.master, i=bgimg)
limg.pack()


username = tk.Label (root, text = "username").place(x = 30, y = 50)
password = tk.Label (root, text = "password").place(x = 30, y = 90)
e1 = tk.Entry(root).place(x = 100, y = 50)
e2 = tk.Entry(root).place(x = 100, y = 90)

submit = tk.Button(root, text = "Submit").place(x = 160, y = 120)


root.mainloop ()
