import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
def helloCallBack():
    msg.showinfo("belajar GUI", "assalamualaikum semangat ahmi!!")
CheckVar1 = tk.IntVar()
C=tk.Checkbutton(top, text="Coba check", variable=
                 CheckVar1, onvalue="Mr.", offvalue="Ms.", height=5)
C.pack()
L1=tk.Label(top, text="Nama : ")
L1.pack()
E1=tk.Entry(top, bd=5)
E1.pack()

def helloCallBack1():
   msg.showinfo( "belajar GUI", "assalamualaikum semangat ahmi!!" + CheckVar1.get() + E1.get())
w1=tk.Button(top, text="Klik Saya", command=helloCallBack1)
w1.pack()
top.mainloop()
