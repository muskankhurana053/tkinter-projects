from tkinter import *
import datetime
import winsound
import time
root=Tk()
root.wm_geometry('400x300')
root.config(bg='light blue')
#pic=PhotoImage(file='img/icon.ico')
root.iconbitmap('img/icon.ico')
root.title('CLOCK')
def new_frame():
    
    
    root.destroy()
    import remclk

def show_time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=t)
    clock_label.after(1000,show_time)


date_display=Label(root,text=datetime.datetime.now().strftime("%d/%m/%Y"),bg='blue',fg='white',font = ("Times", 30))

date_display.place(x=20,y=10,height=100,width=360)
    
    
alarm_button=Button(root,text='SET REMINDER',command=new_frame,bg="navy blue",fg='white',font = ("Times", 15))
alarm_button.place(y=200,x=110,height=50)

clock_label=Label(root,bg="green", fg="white", font = ("Times", 30), relief='flat')
clock_label.place(x=20,y=100,width=360,height=100)
show_time()



quit=Button(root,text='Quit',command=quit,bg='navy blue',fg='white')
quit.place(x=350,y=260)
root.mainloop()