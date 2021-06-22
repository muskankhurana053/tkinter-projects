import tkinter as tk
import datetime
import winsound
import time
import pyttsx3
from threading import *
def Threading():
    t1=Thread(target=alarm1)
    t1.start()

def alarm1():
    
    while True:
        

        set_alarm_timer = f"{hrvalue.get()}:{minvalue.get()}:{secvalue.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        
        if now == set_alarm_timer:
            print("Time to Wake up")
            engine = pyttsx3.init()
            engine.say(name.get())
            engine.say(name.get())
            engine.say(name.get())
            engine.say(name.get())
            engine.runAndWait()
            break

def back():
    alarm.destroy()
    import digclk
    

    


alarm=tk.Tk()
alarm.geometry('400x300')
alarm.config(bg='light blue')
alarm.iconbitmap('img/icon.ico')
alarm.title('REMINDER')
#alarm.resizable(0,0)
name=tk.StringVar(alarm)
    




label=tk.Label(alarm,text='       HOURS                MINUTES                SECONDS   ',bg='blue',fg='white')
label.place(x=20,y=10)
hroption=[]
hrvalue=tk.IntVar()
hrvalue.set('select hours')
for i in range(1,25):
    hroption.append(i)
hrs = tk.OptionMenu(alarm,hrvalue,*hroption)
hrs.config(bg='green',fg='white')
hrs.place(x=0,y=60)

minoption=[]
minvalue=tk.StringVar()
minvalue.set('select Minutes')
for j in range(1,61):
    strj=str(j)
    if len(strj)==1:
            #int(f"0{strj}")
        minoption.append(f'0{strj}')
            #print(f'0{strj}')
    else:
        minoption.append(j)
min = tk.OptionMenu(alarm,minvalue,*minoption)
min.config(bg='green',fg='white')
min.place(x=130,y=60)

secoption=[]
secvalue=tk.StringVar()
secvalue.set('select sec')
for k in range(1,61):
    strk=str(k)
    if len(strk)==1:

        secoption.append(f'0{strk}')
    else:
        secoption.append(k)
sec = tk.OptionMenu(alarm,secvalue,*secoption)
sec.config(bg='green',fg='white')
sec.place(x=280,y=60)


label2=tk.Label(alarm,text='Reminder Name',bg='blue',fg='white')
label2.place(x=20,y=120)

remname=tk.Entry(alarm,textvariable=name,bg='blue',fg='white')
remname.place(x=160,y=120)

set=tk.Button(alarm,text='SET ALARM',command=alarm1,bg='navy blue',fg='white')
set.place(x=140,y=150)


quit=tk.Button(alarm,text='Quit',command=quit,bg='navy blue',fg='white')
quit.place(x=350,y=260)

back=tk.Button(alarm,text='Back',command=back,bg='navy blue',fg='white')
back.place(x=10,y=260)




alarm.mainloop()




