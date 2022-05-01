# Import module
from tkinter import *
import tkinter as tk
from tkinter import Tk, ttk
from turtle import color
import encryptalgo
# Create object
root = Tk()

# Adjust size
root.geometry( "750x440" )
root.title('Encrypt-It')
root.iconbitmap(r'D:\\encryptit\icon\icon1.ico')
root.resizable(False, False)

background_image1 = PhotoImage(file = "image/new3.png")
# Define the style for combobox widget
style= ttk.Style()
style.theme_use('alt')
style.configure("TCombobox", fieldbackground= "black", background= "silver")

background_label = Label( root, image = background_image1)
background_label.place(x = -60, y = -50)

# text = Label(root)
# text.place(x = 270,y=120)
def click(event):
   textbox.configure(state=NORMAL)
   textbox.delete(1.0, END)
   textbox.unbind('<Button-1>', clicked)
global textbox
textbox = Text(root, height = 8, width = 48,bg="black",fg="white")
textbox.insert(INSERT,"Enter text here")
textbox.place(x = 180,y=130)
ttk.Label(root, text = "Select Algorithm :", 
        font = ("Times New Roman", 15),background="black",foreground="silver").place(x=200, y = 90)
global algo  
algo = tk.StringVar()
algochoosen = ttk.Combobox(root, width = 18, 
                            textvariable = algo,font = ("Times New Roman", 14),foreground="white")
# Adding combobox drop down list
algochoosen['values'] = (' Caesar Cipher - ROT13', 
                          ' Simple AES',
                          ' MD5',
                          ' SHA 1',
                          ' SHA 224',
                          ' SHA 256',
                          ' SHA 384',
                          ' SHA 512',
                          ' Shake Algorithm', 
                          ' RIPEMD160', 
                          ' Transposition Cipher')
  
algochoosen.place(x = 350,y=90)
  
# Shows february as a default value
algochoosen.current(0) 

def encryptbutton():
        import encryptalgo
        encryptalgo.etc(algo.get(),textbox.get(1.0,END))
def decryptbutton():
        import decryptalgo
        decryptalgo.etc(algo.get(),textbox.get(1.0,END))
        
# Create button, it will change label text
button = Button( root , text = "Encrypt-It" , command = encryptbutton,padx=30 ,font = ("Times New Roman", 13))
button.place(x=230,y=270)
button = Button( root , text = "Decrypt-It" , command = decryptbutton,padx=30 ,font = ("Times New Roman", 13))
button.place(x=375,y=270)

# Create Label
label = Label( root , text = " " )
label.grid(row=10,column=10)
clicked = textbox.bind('<Button-1>', click)
# Execute tkinter
root.mainloop()
