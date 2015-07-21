##HELP ME GUYS
'''
Created on 20 Tem 2015

@author: ahmet
'''
from tkinter import *
from signal import alarm
import time
from datetime import date, datetime
from time import sleep
from threading import Thread
from test.support import args_from_interpreter_flags




kapalimi=1
pencere = Tk()   #pencereyi oluştur
pencere.title("Alarm") #başlığı Alarm yap
pencere.tk_setPalette("black")
pencere.overrideredirect(0)
##pencere.resizable(False,False) # kücültme büyültmeyi kapat 
pencere.geometry("250x200+1050+50") # boyutu belirle ve konumunu
dakika=Label(text="Dakika: ",justify="left",fg="Blue",bd=50)
dakika.pack()
dakika.place(x=0,y=50,width=53,height=30)
saatGirisi=Entry()
saatGirisi.pack()   
saatGirisi.place(x=50,y=5)

dakikaGirisi=Entry()
dakikaGirisi.pack()   
dakikaGirisi.place(x=50,y=55)
def alarmCal(alarmiminDakikasi,alarmiminSaati):
    
    while True:
        print("Alarmaaaaa")
        print(alarmiminDakikasi)
        sleep(3)
        if alarmiminSaati == time.strftime("%H"):
                print("ALARM")
    

        
    

def kur():
    saatStr=saatGirisi.get()
    dakikaStr=dakikaGirisi.get()
    alarmSaati=int(saatStr)
    alarmDakikasi=int(dakikaStr)
    a=Thread(target=alarmCal,args =(alarmSaati, alarmSaati))
    a.start()
def kapat():
    kapalimi=0


alarmKur=Button(text="Kur"
                ,command=kur
                ,relief="flat"
                ,fg="firebrick"
                ,bg="white"
                ,cursor="hand2")
alarmKur.pack()
alarmKur.place(x=15,y=150)
saat=Label(text="Saat: ",fg="white",bd=50)
saat.pack()
saat.place(x=0,y=0,width=40,height=30)
kapat=Button(text="Kapat"
                ,command=kapat
                ,relief="flat"
                ,fg="firebrick"
                ,bg="white"
                ,cursor="hand2")
kapat.pack(padx=50,pady=50)
kapat.place(x=60,y=150)





pencere.mainloop()

