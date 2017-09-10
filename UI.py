import cv2
import tkinter as tk
from PIL import Image, ImageTk
def printer (event):
    print ("hello world")
root = tk.Tk()
a= cv2.imread('/home/anton/Downloads/345.jpg')
grid = tk.Button(root)

grid.bind("<Button-1>", printer)
grid.pack()
root.resizable
c = tk.Canvas(root, width=300, height = 500)
#a = Image.open(a)
a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
a = Image.fromarray(a)
a = ImageTk.PhotoImage(a)
c.create_image(0,0, image=a,anchor ="nw")
c.pack()
tk.Label(root, text = "/home/anton/Downloads/345.jpg").pack()

root.mainloop()

