from Labs import Logic
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile as fo
def printer (event):
    print ("hello world")
def cvtotk(a):
    alo = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    alo = Image.fromarray(alo)
    alo = ImageTk.PhotoImage(alo)
    return alo
def selectimage(event):
    d = fo()
    print(d.name)
    acv = cv2.imread(d.name)
    a= cvtotk(cv2.resize(acv, (400, 400)))
    leftwindow.create_image(0, 0, image=a, anchor="nw")
    leftwindow.pack(side="right")
    root.mainloop()
def creategird(event):
    a= Logic.Logic.creategrid(acv, 10, 5, color =(0,125,0))
    a = cv2.resize(a, (400, 400))
    a= cvtotk(a)
    rightwindow.create_image(0, 0, image=a, anchor="nw")
    rightwindow.pack(side="right")
    root.mainloop()
    print("Решетка")
def findgird(event):
#    cv2.imshow('234', acv)
#    cv2.waitKey(0)
    a = Logic.Logic.findgrid(acv)
    a = cv2.resize(a, (400, 400))
    a= cvtotk(a)
    rightwindow.create_image(0, 0, image=a, anchor="nw")
    rightwindow.pack(side="right")
    root.mainloop()
    print("Нашли решетку")


root = tk.Tk()
acv= cv2.imread('Stock.jpg')
#Настройка кнопок
selectim = tk.Button(root, text = "Выберете изображение")
selectim.bind("<Button-1>", selectimage)
selectim.pack()
crtgird = tk.Button(root, text ="Создать решетку")
crtgird.bind("<Button-1>", creategird )
crtgird.pack()
fndgird = tk.Button(root, text = "Найти решетку")
fndgird.bind("<Button-1>",findgird)
fndgird.pack()

root.resizable
leftwindow = tk.Canvas(root, width=400, height = 400)
rightwindow = tk.Canvas(root, width = 400, height= 400)
#a = Image.open(a)
a = cvtotk(cv2.resize(acv, (400, 400) ))
rightwindow.create_image(0,0, image =a, anchor = "nw")
rightwindow.addtag_all('im')
rightwindow.pack(side = "right")
leftwindow.create_image(0,0, image=a,anchor ="nw")
leftwindow.addtag_all('im')
leftwindow.pack(side = "left")
#tk.Label(root, text = "/home/anton/Downloads/345.jpg").pack()
root.mainloop()

