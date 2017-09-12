from Labs import Logic
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile as fo
d= 'Stock.jpg'
def printer (event):
    print ("hello world")
def cvtotk(a):
    alo = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    alo = Image.fromarray(alo)
    alo = ImageTk.PhotoImage(alo)
    return alo
def selectimage(event):
    global d
    global acv
    z = fo()
    if z!=None:
        d = z.name
    print(d)
    acv = cv2.imread(d)
    a= cvtotk(cv2.resize(acv, (400, 400)))
    leftwindow.create_image(0, 0, image=a, anchor="nw")
    leftwindow.pack(side="left")
    root.mainloop()
def creategird(event):
    print (wid.get())
    global acv
    acv = Logic.Logic.creategrid(cv2.imread(d), wid.get(), count.get()+1, color =(blue.get()
                                                                                  ,green.get(),
                                                                                  red.get()))
    a = acv
    a = cv2.resize(a, (400, 400))
    a= cvtotk(a)
    leftwindow.create_image(0, 0, image=a, anchor="nw")
    leftwindow.pack(side="left")
    root.mainloop()
    print("Решетка")
def findgird(event):
#    cv2.imshow('234', acv)
#    cv2.waitKey(0)
    global acv
##    a = Logic.Logic.findgrid(cv2.resize(acv, (0,0), fx=1.7, fy=1.7))
    a = Logic.Logic.findgrid(cv2.resize(acv, (1000,1000)))
    a = cv2.resize(a, (400, 400))
    a= cvtotk(a)
    rightwindow.create_image(0, 0, image=a, anchor="nw")
    rightwindow.pack(side="right")
    root.mainloop()
    print("Нашли решетку")


root = tk.Tk()
acv= cv2.imread(d)
#Настройка окон
righttoll = tk.Frame(root,width = 50, height = 450)
toolbar = tk.Frame(root, width=800, height = 50)
leftwindow = tk.Canvas(root, width=400, height = 400)
rightwindow = tk.Canvas(root, width = 400, height= 400)
#Настройка кнопок
selectim = tk.Button(toolbar, text = "Выберете изображение")
selectim.bind("<Button-1>", selectimage)
selectim.pack(side = "left")
crtgird = tk.Button(toolbar, text ="Создать решетку")
crtgird.bind("<Button-1>", creategird )
fndgird = tk.Button(toolbar, text = "Найти решетку")
fndgird.bind("<Button-1>",findgird)
fndgird.pack(side = "left")
crtgird.pack(side = "left")
#Текст
tred = tk.Canvas(righttoll, width= 70, height =26)
tred.create_text((30,15), text="Красный:")
tgreen = tk.Canvas(righttoll, width= 70, height =26)
tgreen.create_text((33,15), text="Зеленный:")
tblue = tk.Canvas(righttoll, width= 70, height =26)
tblue.create_text((22,15), text="Синий:")
textforwidth = tk.Canvas(toolbar, width = 60, height = 40)
textforwidth.create_text((35,10), text= "Ширина:")
textcount = tk.Canvas(toolbar, width = 60, height = 40)
textcount.create_text((35,10), text ="Кол-во:")
#Настройка ползунков
red = tk.Scale(righttoll, from_=255, to=0)
tred.pack(side ="top")
red.pack(side ="top")
green = tk.Scale(righttoll, from_=255, to=0)
tgreen.pack(side ="top")
green.pack(side ="top")
blue = tk.Scale(righttoll, from_=255, to=0)
tblue.pack(side ="top")
blue.pack(side ="top")
wid= tk.Scale(toolbar,from_=0, to=50, orient = tk.HORIZONTAL)
textforwidth.pack(side="left")
wid.pack(side = "left")
count = tk.Scale(toolbar, from_=0, to=20, orient = tk.HORIZONTAL)
textcount.pack(side = "left")
count.pack(side = "left")
#настройка содержимого окон
a = cvtotk(cv2.resize(acv, (400, 400) ))
rightwindow.create_image(0,0, image =a, anchor = "nw")
toolbar.pack(side = "bottom")
righttoll.pack(side ="right")
rightwindow.pack(side = "right")
leftwindow.create_image(0,0, image=a,anchor ="nw")
leftwindow.addtag_all('im')
leftwindow.pack(side = "left")

#tk.Label(root, text = "/home/anton/Downloads/345.jpg").pack()
root.mainloop()

