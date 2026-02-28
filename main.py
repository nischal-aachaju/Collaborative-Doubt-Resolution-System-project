from tkinter import *
import sqlite3
from PIL import Image, ImageTk
# from tkinter import messagebox
# import hashlib
#----------database-----------------
conn=sqlite3.connect("cdrs.db")
cur=conn.cursor()

root =Tk()
root.geometry("800x600")
root.resizable(0,0)
root.iconbitmap('assects/logo.ico')

image_bg = Image.open("assects/dashboard.jpg")
resize_bg =image_bg.resize((800, 600))
final_bg = ImageTk.PhotoImage(resize_bg)

lbl = Label(root, image=final_bg)
lbl.image = final_bg 
lbl.pack()

button = Label(root,
                    text="Login",
                    fg="white",bg="#72dae4", cursor="hand2",font=("Arial",16,"bold"))
button.place(x=370,y=390)
# button.bind("<Button-1>", lambda e: login_page())

root.mainloop()
