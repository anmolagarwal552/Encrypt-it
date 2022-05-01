# Import Module
import imp
from operator import imod
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, color
from tkhtmlview import HTMLLabel
from time import sleep, time
import webbrowser

# Create Object
root = Tk()
# Set Geometry
root.geometry("750x440")
root.title('Encrypt-It')
root.iconbitmap(r'D:\\encryptit\icon\icon1.ico')

# Imaages Edit
background_image1 = PhotoImage(file = "image/new3.png")
button_module0 = PhotoImage(file = "image/b1.png")
button_module2 = PhotoImage(file = "image/b2.png")
button_module3 = PhotoImage(file = "image/b3.png")

#functions for 3 buttons
def open_webbrowser():
	webbrowser.open("https://jlu03447.wixsite.com/website")

def open_encrypt():
    root.destroy()
    import encrypt
def pop():
        messagebox.showinfo("About us", '''
Encrypt-It is an encryption tool that will be available for Windows Vista and higher versions. It will not encrypt individual files and folders, but it will encrypt entire texts that has been provided to it. This not only includes drives on your computer.
Here in Encrypt-It we have provided a good number of encryption algorithms and hashes that one individual can use to encrypt his text along with their respected modules in order to learn about the specific the algorithm or hash that has been used.
Encrypt-It not only encrypts the given the texts but it also decrypts it.
Encrypt-It is an endeavor to improve the pre existing tools of encryption through a quick encryption and the availability of learning modules.
Through our project we (Anmol and Kaustubh) aim to impart some basic working methodology of encryption on to our users.
Thank You.
ⒸEncrypt-It''')		

#open multiple weblinks to do
import webbrowser
def CaesarCipherROT13():
    webbrowser.open("https://jlu03447.wixsite.com/website/algorithm-to-study-copy")
def SimpleAES():
    webbrowser.open("https://jlu03447.wixsite.com/website/caesar-cipher-rot13-copy")
def MD5():
    webbrowser.open("https://jlu03447.wixsite.com/website/caesar-cipher-rot13-copy-1")
def SHA1():
    webbrowser.open("https://jlu03447.wixsite.com/website/md5-copy")
def SHA224():
    webbrowser.open("https://jlu03447.wixsite.com/website/sha1-copy")
def SHA256():
    webbrowser.open("https://jlu03447.wixsite.com/website/sha224-copy")
def SHA384():
    webbrowser.open("https://jlu03447.wixsite.com/website/sha256-copy")
def SHA512():
    webbrowser.open("https://jlu03447.wixsite.com/website/sha384-copy")
def ShakeAlgorithm():
    webbrowser.open("https://jlu03447.wixsite.com/website/sha-512-copy")
def RIPEMD160():
    webbrowser.open("https://jlu03447.wixsite.com/website/shake-algorithm-copy")
def TranspositionCipher():
    webbrowser.open("https://jlu03447.wixsite.com/website/ripemd160-copy")
def PrivateKeyandPublicKeyEncryption():
    webbrowser.open("https://jlu03447.wixsite.com/website/transportation-cipher-copy")

#create new function for next window
def nextpage():
	background_label.config(image = background_image1)
	menubar = Menu(root)
	menubar.config(bg="black")
	# Adding File Menu and commands
	file = Menu(menubar, tearoff = 0, background='black', fg='white')

	menubar.add_cascade(label ='To do', menu = file)
	file.add_command(label ='Caesar Cipher - ROT13', command = CaesarCipherROT13)
	file.add_command(label ='Simple AES', command = SimpleAES)
	file.add_command(label ='MD5', command = MD5)
	file.add_command(label ='SHA 1', command = SHA1)
	file.add_command(label ='SHA 224', command = SHA224)
	file.add_command(label ='SHA 256', command = SHA256)
	file.add_command(label ='SHA 384', command = SHA384)
	file.add_command(label ='SHA 512', command = SHA512)
	file.add_command(label ='Shake Algorithm', command = ShakeAlgorithm)
	file.add_command(label ='RIPEMD160', command = RIPEMD160)
	file.add_command(label ='Transposition Cipher', command = TranspositionCipher)
	file.add_command(label ='Private Key and Public Key Encryption', command = PrivateKeyandPublicKeyEncryption)    
	file.add_separator()
	file.add_command(label ='Exit', command = root.destroy)
	
	# Adding Edit Menu and commands
	edit = Menu(menubar, tearoff = 0, background='black', fg='white')
	menubar.add_cascade(label ='practical', menu = edit)
	edit.add_command(label ='Caesar Cipher - ROT13', command = open_encrypt)
	edit.add_command(label ='Simple AES', command = open_encrypt)
	edit.add_command(label ='MD5', command = open_encrypt)
	edit.add_command(label ='SHA 1', command = open_encrypt)
	edit.add_command(label ='SHA 224', command = open_encrypt)
	edit.add_command(label ='SHA 256', command = open_encrypt)
	edit.add_command(label ='SHA 384', command = open_encrypt)
	edit.add_command(label ='SHA 512', command = open_encrypt)
	edit.add_command(label ='Shake Algorithm', command = open_encrypt)
	edit.add_command(label ='RIPEMD160', command = open_encrypt)
	edit.add_command(label ='Transposition Cipher', command = open_encrypt)
	edit.add_command(label ='Private Key and Public Key Encryption', command = open_encrypt)
	edit.add_separator()
	edit.add_command(label ='Exit', command = root.destroy)
	root.config(menu = menubar)
	new_page_button0 = Button(root,image=button_module0,border=0,bg="black",command=open_webbrowser)
	new_page_button1 = Button(root,image=button_module2,border=0,bg="black",command=open_encrypt)
	new_page_button2 = Button(root,image=button_module3,border=0,bg="black",command=pop)
	new_page_button0.place(x=300,y=120)
	new_page_button1.place(x=280,y=170)
	new_page_button2.place(x=305,y=220)
	new_page_button.destroy()

# background button and image setting
bg = PhotoImage(file = "image/new1.png")
bg1 = PhotoImage(file = "icon/button1.png")
background_label = Label( root, image = bg)
background_label.place(x = -60, y = -50)
new_page_button = Button(root,image=bg1,command=nextpage,border=0)
new_page_button.place(x=305,y=320)

# Execute Tkinter
root.resizable(False, False)
root.mainloop()
