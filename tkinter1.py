import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
def helloCallBack1():
   msg.showinfo( "belajar GUI", "assalamualaikum semangat ahmi!!")
w=tk.Button(top, text="Klik Saya", command=helloCallBack1)
w.pack()
w2=tk.Button(top, text="Klik saya untuk keluar", command=top.destroy)
w2.pack()
top.mainloop()