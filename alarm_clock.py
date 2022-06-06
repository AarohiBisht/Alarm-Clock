from tkinter import*
from tkinter.ttk import Combobox
from tkinter.messagebox import*
import datetime

from playsound import playsound

root=Tk()

def alarm():
    hour=int(c.get())
    minute=int(c1.get())
    
    showinfo("alarm notication","alarm has been set")
    print(datetime.datetime.now())
    while True:
        if hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute:
                playsound('https://d6cp9b00-a.akamaihd.net/downloads/ringtones/files/dl/mp3/baby2-4841-49732-53211-2-54250.mp3')
                break
root.title(" my alaram clock")

l1=Label(root,text="set alarm hour")
l1.grid(row=0,column=0)
hour=list(range(1,25))
c=Combobox(root,values=hour)
c.grid(row=0,column=1) 
 

l2=Label(root,text="set alarm minute")
l2.grid(row=1,column=0)
minute=list(range(1,61))
c1=Combobox(root,values=minute)
c1.grid(row=1,column=1 )


btn=Button(root,text="set alarm",command=alarm)
btn.grid(row=2,column=2)
root.mainloop()
