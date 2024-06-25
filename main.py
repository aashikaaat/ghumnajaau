# Importing Libraries
from tkinter import *
import customtkinter
from PIL import Image, ImageTk

def resize_image(image_path, new_width, new_height):
    img = Image.open(image_path)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

customtkinter.set_appearance_mode("dark")

# create CTK window like you do with the Tk window 
root = customtkinter.CTk()

# Setting Widow width and Height
screenwidth= root.winfo_screenwidth()
screenheight= root.winfo_screenheight()

root.geometry(f'{screenwidth}x{screenheight}+0+0')

# Add image file 
image_path = "pro.png"
img = Image.open(image_path)
img = img.resize((2152,909))
bg = ImageTk.PhotoImage(img)


# Show image using label 
label1 = Label(root,compound = 'bottom', image = bg, bg = "#222222") 
# label1.place(x = 90, y = 210) 
label1.pack(fill='both',expand = True)


# Running the app 
root.mainloop()