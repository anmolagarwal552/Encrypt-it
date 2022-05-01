import pyaes, pbkdf2, binascii, os, secrets
from hashlib import md5
import hashlib
from tkinter import messagebox
global etc
def etc(algorithm,textboxmessage):
    textboxmessage=textboxmessage.strip()
    if algorithm == " Caesar Cipher - ROT13":
            # Dictionary to lookup the index of alphabets
        dict1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
                'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
                'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
                'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
                'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
        # Dictionary to lookup alphabets
        # corresponding to the index after shift
        dict2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
                6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
                11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
                16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
                21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'}
        # Function to encrypt the string
        # according to the shift provided
        def encrypt(message, shift):
            cipher = ''
            for letter in message:
                # checking for space
                if(letter != ' '):
                    # looks up the dictionary and
                    # adds the shift to the index
                    num = ( dict1[letter] + shift ) % 26
                    # looks up the second dictionary for
                    # the shifted alphabets and adds them
                    cipher += dict2[num]
                else:
                    # adds space
                    cipher += ' '
            return cipher
        # use 'upper()' function to convert any lowercase characters to uppercase
        shift = 13
        result = "Encrypted Text : "+encrypt(textboxmessage.upper(), shift)
        print (result.lower())
        messagebox.showinfo("Caesar Cipher - ROT13",result.lower())
    elif algorithm == " Simple AES": 
        # Derive a 256-bit AES encryption key from the password
        password = "python"
        passwordSalt = os.urandom(16)
        key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
        iv = secrets.randbits(256)
        plaintext = textboxmessage
        aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
        ciphertext = aes.encrypt(plaintext)
        print('Encrypted:', binascii.hexlify(ciphertext))
        messagebox.showinfo("Simple AES",f"Encrypted text : {binascii.hexlify(ciphertext)}")
    elif algorithm == " MD5":
        class MD5:
            def __init__(self, data = textboxmessage):
                self.data = data
            def encrypt(self):
                self.data = md5(self.data.encode()).hexdigest()
                return self.data
        crypt = MD5()
        print(crypt.encrypt()) # Encrypt
        messagebox.showinfo("MD5        ",f"Encrypted text : {crypt.encrypt()}")
    elif algorithm == " SHA 1":
        result = hashlib.sha1(textboxmessage.encode())
        messagebox.showinfo("SHA1        ",f"Encrypted text : {result.hexdigest()}")
    elif algorithm == " SHA 224":
        result = hashlib.sha224(textboxmessage.encode())
        messagebox.showinfo("SHA224        ",f"Encrypted text : {result.hexdigest()}")
    elif algorithm == " SHA 256":
        result = hashlib.sha256(textboxmessage.encode())
        messagebox.showinfo("SHA256        ",f"Encrypted text : {result.hexdigest()}")
    elif algorithm == " SHA 384":
        result = hashlib.sha384(textboxmessage.encode())
        messagebox.showinfo("SHA384        ",f"Encrypted text : {result.hexdigest()}")
    elif algorithm == " SHA 512":
        result = hashlib.sha512(textboxmessage.encode())
        messagebox.showinfo("SHA512        ",f"Encrypted text : {result.hexdigest()}")
    elif algorithm == " Shake Algorithm":
        m = hashlib.shake_256()
        m.update(bytes(textboxmessage, "utf-8"))
        print("Digest Value : " ,m.digest(200))
        messagebox.showinfo("Shake Algorithm",f"Encrypted text : {m.digest(200)}")
    elif algorithm == " RIPEMD160":
        x = hashlib.new('ripemd160')
        x.update(bytes(textboxmessage, "utf-8"))
        print("Digest Value : " ,x.digest())
        messagebox.showinfo("Shake Algorithm",f"Encrypted text : {x.digest()}")
    elif algorithm == " Transposition Cipher":
        def split_len(seq, length):
            return [seq[i:i + length] for i in range(0, len(seq), length)]
        def encode(key, plaintext):
            order = {
                int(val): num for num, val in enumerate(key)
            }
            ciphertext = ''

            for index in sorted(order.keys()):
                for part in split_len(plaintext, len(key)):
                    try:ciphertext += part[order[index]]
                    except IndexError:
                        continue
            return ciphertext
        print()

        messagebox.showinfo("Transposition Cipher",f"Encrypted text : {encode('3214', textboxmessage)}")