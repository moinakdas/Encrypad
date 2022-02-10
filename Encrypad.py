# The following is the first iteration of Encrypad, a .txt file encryption program
# Features in 1.0
#   Create .txt files
#   delete .txt files
#   open .txt files
#   view files in .txt directory
#   Normal/Encrypted entries
#   Save View Delete and Open files


import tkinter as tk
import random
import os


# ============================= FUNCTIONALITY ===================================================================
x = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?"
y = "<NCE._#IbVW1BsGT|$&-JiA9ypwhH!nPx{}D=5/4jK~>YmXq*lUF%;reL:+7tv2u3M]gSzo?`R[Qa),6@Ocd0'f8(k^Z"

chars = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y',
         'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x',
         'c', 'v', 'b', 'n', 'm', ',', '.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
         '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F',
         'G', 'H', 'J', 'K', 'L', ':', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']

#master encryption dictionary
encrypt = {'`': '<',
           '1': 'N',
           '2': 'C',
           '3': 'E',
           '4': '.',
           '5': '_',
           '6': '#',
           '7': 'I',
           '8': 'b',
           '9': 'V',
           '0': 'W',
           '-': '1',
           '=': 'B',
           'q': 's',
           'w': 'G',
           'e': 'T',
           'r': '|',
           't': '$',
           'y': '&',
           'u': '-',
           'i': 'J',
           'o': 'i',
           'p': 'A',
           '[': '9',
           ']': 'y',
           'a': 'p',
           's': 'w',
           'd': 'h',
           'f': 'H',
           'g': '!',
           'h': 'n',
           'j': 'P',
           'k': 'x',
           'l': '{',
           ';': '}',
           "'": 'D',
           'z': '=',
           'x': '5',
           'c': '/',
           'v': '4',
           'b': 'j',
           'n': 'K',
           'm': '~',
           ',': '>',
           '.': 'Y',
           '/': 'm',
           '~': 'X',
           '!': 'q',
           '@': '*',
           '#': 'l',
           '$': 'U',
           '%': 'F',
           '^': '%',
           '&': ';',
           '*': 'r',
           '(': 'e',
           ')': 'L',
           '_': ':',
           '+': '+',
           'Q': '7',
           'W': 't',
           'E': 'v',
           'R': '2',
           'T': 'u',
           'Y': '3',
           'U': 'M',
           'I': ']',
           'O': 'g',
           'P': 'S',
           '{': 'z',
           '}': 'o',
           '|': '?',
           'A': '`',
           'S': 'R',
           'D': '[',
           'F': 'Q',
           'G': 'a',
           'H': ')',
           'J': ',',
           'K': '6',
           'L': '@',
           ':': 'O',
           'Z': '\n',
           'X': 'd',
           'C': '0',
           'V': "'",
           'B': 'f',
           'N': '8',
           'M': '(',
           ' ': 'k',
           '>': '^',
           '?': '\t',
           '<': ' ',
           '"': "Z",
           '\n':'c',
           "\t":'"'}

#reverses keys and values of encrypt dictionary, create decrypt dictionary
decrypt = dict([[v,k] for k,v in encrypt.items()])

#encrypts once by dictionary
def enc0(text):
    """Assumes text is a string
       Returns encrypted string"""
    ans = ""
    for letter in str(text):
        ans += encrypt[letter]
    return ans

#decrypts once by dictionary
def dec0(text):
    """Assumes text is a string
       Returns decrypted string"""
    ans = ""
    for letter in str(text):
        ans += decrypt[letter]
    return ans

#=========================================================================

#encrypt
def enc(text):
    """Assumes text is a string
       Returns encrypted string"""
    nums = [1,2,3,4,5,6,7,8,9,10]
    numIter = random.choice(nums) #determines how many times enc0 will be called
    addchar = random.randrange(40) #determines dummy chars after encrypted message
    beginchar = random.randrange(40) # determines dummy chars before encrypted message

    
    if len(str(addchar)) == 1:
        addnums = "0" + str(addchar)
    else:
        addnums = str(addchar)

    if len(str(beginchar)) == 1:
        beforenums = "0" + str(beginchar)
    else:
        beforenums = str(beginchar)
    
    #create dummy characters after
    addon = ""
    for i in range(addchar):
        addon += random.choice(chars)

    #create dummy characters before
    beforeon = ""
    for i in range(beginchar):
        beforeon += random.choice(chars)
        

    if numIter == 1:
        ans = "002!" + str(enc0(text))
    elif numIter == 2:
        ans = "+$a!" + str(enc0(enc0(text)))
    elif numIter == 3:
        ans = "~!Y#" + str(enc0(enc0(enc0(text))))
    elif numIter == 4:
        ans = "]_[}" + str(enc0(enc0(enc0(enc0(text)))))
    elif numIter == 5:
        ans = "2$%+" + str(enc0(enc0(enc0(enc0(enc0(text))))))
    elif numIter == 6:
        ans = "!$@2" + str(enc0(enc0(enc0(enc0(enc0(enc0(text)))))))
    elif numIter == 7:
        ans = "q+=!" + str(enc0(enc0(enc0(enc0(enc0(enc0(enc0(text))))))))
    elif numIter == 8:
        ans = "^!#@" + str(enc0(enc0(enc0(enc0(enc0(enc0(enc0(enc0(text)))))))))
    elif numIter == 9:
        ans = "6t+-" + str(enc0(enc0(enc0(enc0(enc0(enc0(enc0(enc0(enc0(text))))))))))
    elif numIter == 10:
        ans = "&^4%" + str(enc0(enc0(enc0(enc0(enc0(enc0(enc0(enc0(enc0(enc0(text)))))))))))

    ans = beforeon + ans + addon + enc0(addnums) + enc0(beforenums)
    return ans

def dec(text):
    """Assumes text is a string
       Returns decrypted string"""
    buffers = text[:-4]
    info = text[-4:]
    numbefore = int(dec0(info[-2:]))
    numafter = int(dec0(info[-4:-2])) * -1
    almost = buffers[numbefore:numafter] # marker,ans
    eng = almost[4:]
    marker = almost[:4]
    
    if marker == "002!":
        ans = dec0(eng)
    elif marker == "+$a!":
        ans = dec0(dec0(eng))
    elif marker == "~!Y#":
        ans = dec0(dec0(dec0(eng)))
    elif marker == "]_[}":
        ans = dec0(dec0(dec0(dec0(eng))))
    elif marker == "2$%+":
        ans = dec0(dec0(dec0(dec0(dec0(eng)))))
    elif marker == "!$@2":
        ans = dec0(dec0(dec0(dec0(dec0(dec0(eng))))))
    elif marker == "q+=!":
        ans = dec0(dec0(dec0(dec0(dec0(dec0(dec0(eng)))))))
    elif marker == "^!#@":
        ans = dec0(dec0(dec0(dec0(dec0(dec0(dec0(dec0(eng))))))))
    elif marker == "6t+-":
        ans = dec0(dec0(dec0(dec0(dec0(dec0(dec0(dec0(dec0(eng)))))))))
    elif marker == "&^4%":
        ans = dec0(dec0(dec0(dec0(dec0(dec0(dec0(dec0(dec0(dec0(eng))))))))))
    else:
        ans = "Error: File corrupted \n \nWhy did this happen? \n \nWhen saving your encrypted file, please be sure that you do not edit the text file in any way. Doing so may result in file corruption & data loss."
    return ans

#S)XuV/R8R*z[7^!#@=jLLQ!kQ~LzU[}DX{<NSK>LXO-vge#p`Qk(_Jh&FjnOECNE

#define functions =================================================================================================


#keep relief flat 
def keep_flat(event):       # on click,
    if event.widget is Head or event.widget is labelenc or event.widget is SaveEncFile or event.widget is OpenFile or event.widget is Thirdfunc or event.widget is labelnor: # if the click came from the button
        event.widget.config(relief="flat") # enforce an option

    msg = filename.get()
    if (event.widget is filename and msg == "Enter the filename") or (event.widget is filename and msg == "Must be a .txt file") or (event.widget is filename and msg == "Filepath Error") or (event.widget is filename and msg == "File does not exist") or (event.widget is filename and msg == "File deleted") or (event.widget is filename and msg == "Enter filename"):
        filename.delete(0,"end")
        filename.config(fg = "white")

#output encrypted thing
def do_stuff(event):
    text = normal.get('1.0','end-1c')
    if text.replace(" ","") == "":
        encrypted.delete('1.0','end')
    else:
        newText = enc(str(text))
        encrypted.delete('1.0','end')
        encrypted.insert('1.0',newText)

def clear_all():
    encrypted.delete('1.0','end')
    normal.delete('1.0','end')
    filename.delete(0,"end")

def do_things():
    text = encrypted.get('1.0','end')
    if text.replace(" ","") != "":
        do_stuff("not an event")


def saveFile():
    fileName = filename.get()   
    if fileName.replace(" ","") == "" or fileName == "Enter filename":
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"Enter the filename")
    elif fileName[-4:] != ".txt":
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"Must be a .txt file")
    else:
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "Encryption.io"
        filepath = os.path.join(here, subdir, fileName)

        try:
            f = open(filepath, 'w+')
            text = encrypted.get('1.0','end-1c')
            f.write(text)
            f.close()
        except IOError:
            filename.config(fg = labels)
            filename.insert(0,"Filepath Error")

def saveFile2():
    save = tk.Toplevel()
    save.title("Save files")
    save.wm_iconbitmap('encpad_icon.ico')

    canvas = tk.Canvas(save, height=200, width=500)
    canvas.pack()

    frame = tk.Frame(save, bg=background)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(save, text= "What would you like to save this file as?" , bg="#1cc92b",fg="white",font=("Courier",15),activebackground="#1cc9a4",
                     relief = "flat")
    label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)

    saveName = tk.Entry(save, bg = background, relief = "flat", fg = "white", font=("Courier",15))
    saveName.place(relx = 0.02, rely = 0.21, relheight = 0.3, relwidth = 0.96)

    saveB = tk.Button(save, text="Save", bg = "#f2a200", relief = "flat", fg = "white", font=("Courier",15),
                       activebackground="#1cc9a4", activeforeground = "white")
    saveB.place(relx = 0.01, rely = 0.7, relheight = 0.2, relwidth = 0.98)
    

def readFile():
    fileName = filename.get()

    directory = os.listdir("Encryption.io")
    textFiles = []
    for file in directory:
        if file[-4:] == ".txt":
            textFiles.append(file)
    if fileName.replace(" ","") == "" or fileName == "Enter filename":
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"Enter the filename")
    elif fileName[-4:] != ".txt":
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"Must be a .txt file")
    elif not(fileName in textFiles):
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"File does not exist")
    else:
        path = "Encryption.io\\" + fileName
        openfile = open(path,"r")
        text = openfile.read()
        encrypted.delete('1.0','end')
        encrypted.insert('1.0',text)
        decryp = dec(text)
        normal.delete('1.0','end')
        normal.insert('1.0',decryp)

def theme():
    top = tk.Toplevel()
    top.title("View files")
    top.wm_iconbitmap('encpad_icon.ico')

    canvas = tk.Canvas(top, height=400, width=400)
    canvas.pack()

    frame = tk.Frame(top, bg=background)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(top, text= "Encrypted File Viewer" , bg="#1cc92b",fg="white",font=("Courier",15),activebackground="#1cc9a4",
                     relief = "flat")
    label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.06)

    message = tk.Text(top, bg = background, relief = "flat", fg = "white", font=("Courier",15))
    message.place(relx = 0.02, rely = 0.08, relheight = 0.8, relwidth = 0.96)

    button3 = tk.Button(top, text="Dismiss", command=top.destroy, bg = "#f2a200", relief = "flat", fg = "white", font=("Courier",15),
                       activebackground="#1cc9a4", activeforeground = "white")
    
    button3.place(relx = 0.01, rely = 0.89, relheight = 0.1, relwidth = 0.98)

    findFile(message)

def findFile(message):
    directory = os.listdir("Encryption.io")
    textFiles = []
    for file in directory:
        if file[-4:] == ".txt":
            textFiles.append(file)

    ans = ""
    for i in textFiles:
        ans += i + "\n"
        
    message.insert("1.0",ans)

def deletion():
    fileName = filename.get()
    directory = os.listdir("Encryption.io")
    textFiles = []
    
    for file in directory:
        if file[-4:] == ".txt":
            textFiles.append(file)
            
    if fileName.replace(" ","") == "" or fileName == "Enter filename":
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"Enter the filename")
    elif fileName[-4:] != ".txt":
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"Must be a .txt file")
    elif not(fileName in textFiles):
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"File does not exist")
    else:
        path = "Encryption.io\\" + fileName
        os.remove(path)
        filename.delete(0,"end")
        filename.config(fg = labels)
        filename.insert(0,"File deleted")

def ghostText(filename):

    filename.delete(0,"end")
    filename.config(fg = "#605e6b")
    filename.insert(0,"Enter filename")

def winNor():
    top = tk.Toplevel()
    top.title("Normal")
    top.wm_iconbitmap('encpad_icon.ico')

    canvas = tk.Canvas(top, height=650, width=580)
    canvas.pack()

    frame = tk.Frame(top, bg=background)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(top, text= "Normal" , bg="#1cc92b",fg="white",font=("Courier",15),
                     activebackground="#1cc9a4",relief = "flat")
    label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.06)

    message = tk.Text(top, bg = entries, relief = "flat", fg = "white", font=("Courier",15))
    message.place(relx = 0, rely = 0.06, relheight = 0.94, relwidth = 1)

##    button3 = tk.Button(top, text="Dismiss", command=top.destroy, bg = "#f2a200", relief = "flat",
##                        fg = "white", font=("Courier",10),
##                       activebackground="#1cc9a4", activeforeground = "white")
##    button3.place(relx = 0, rely = 0.96, relheight = 0.4, relwidth = 1)
    
        
#Define colors
mode = "A"
background = "#1f1d2b"
accent = "#1cc92b"
active = "#1cc9a4"
text = "white"
textl = "white"
entries = "#35324a"
labels = "#f2a200"

#tkinter window
root = tk.Tk()
root.title("Encrypad BETA 1.0")
root.wm_iconbitmap('encpad_icon.ico')

canvas = tk.Canvas(root, height=650, width=580)
canvas.pack()

frame = tk.Frame(root, bg=background)
frame.place(relwidth=1, relheight=1)

Head = tk.Button(frame, text="Encrypad", bg=accent, fg=text,font=("Courier",30),
                 activebackground=active,activeforeground="white",overrelief="flat",relief="flat", command = clear_all)
Head.place(relx = 0.0, rely = 0, relwidth=1, relheight = 0.08)

#Entry pallets
normal = tk.Text(frame, bg=entries,fg=text,font=("Courier",12),relief = "flat",insertbackground="white")
normal.place(relx=0.01, rely= 0.14, relwidth=0.98, relheight=0.3)
normal.focus()

encrypted = tk.Text(frame,bg=entries,fg="#00ffea",font=("Courier",12),relief = "flat",insertbackground="white")
encrypted.place(relx = 0.01, rely = 0.5, relwidth = 0.98, relheight = 0.3)

#Labels for entry pallets
labelnor = tk.Button(frame, text="Normal",bg=labels,fg=textl,font=("Courier",20),
                     relief = "flat", activeforeground="white",activebackground=active,
                     command = winNor)
labelnor.place(relx = 0.01, rely = 0.09, relwidth=0.98, relheight = 0.05)

labelenc = tk.Button(frame, text="Encrypted",bg=labels,fg=textl,font=("Courier",20),activebackground=active,
                     command = do_things, relief = "flat", activeforeground="white")
labelenc.place(relx = 0.01, rely = 0.45, relwidth=0.98, relheight = 0.05)

#Tail buttons
SaveEncFile = tk.Button(frame, text="Save", bg=labels, fg=textl,font=("Courier",20),
                 activebackground=active,activeforeground="white",overrelief="flat",relief="flat",
                 command = saveFile)
SaveEncFile.place(relx = 0.01, rely = 0.81, relwidth = 0.2, relheight = 0.08)

OpenFile = tk.Button(frame, text="Open", bg=labels, fg=textl,font=("Courier",20),
                 activebackground=active,activeforeground="white",overrelief="flat",relief="flat",
                 command = readFile)
OpenFile.place(relx = 0.79, rely = 0.81, relwidth = 0.2, relheight = 0.08)

Thirdfunc = tk.Button(frame, text="View", bg=labels, fg=textl,font=("Courier",20),
                 activebackground=active,activeforeground="white",overrelief="flat",relief="flat", command = theme)
Thirdfunc.place(relx = 0.22, rely = 0.81, relwidth = 0.18, relheight = 0.08)

Delete = tk.Button(frame, text="Delete File", bg=labels, fg=textl,font=("Courier",20),
                 activebackground=active,activeforeground="white",overrelief="flat",relief="flat", command = deletion)
Delete.place(relx = 0.41, rely = 0.81, relwidth = 0.37, relheight = 0.08)

#Final Entry

filename = tk.Entry(frame, bg = entries, fg = text,font=("Courier",20), relief = "flat",
                        insertbackground=text, justify = "center")
filename.place(relx = 0.01, rely = 0.9, relwidth = 0.98, relheight = 0.088)

ghostText(filename)
#root binds and mainloop
root.bind('<Button-1>', keep_flat)
root.bind('<Key>', do_stuff)
root.bind('<Control_L>',lambda e: "break")
root.mainloop()
