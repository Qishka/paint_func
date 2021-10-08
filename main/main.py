from tkinter import *
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import tkinter.messagebox
from tkinter import filedialog as fd

directory_files = "main/saves/" #saves directory
lst = [] #list user drawing
root = Tk()
root.title('DROWA GRAPHICS 1.0') #title

def savePosn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    canvas.create_line((lastx, lasty, event.x, event.y))
    savePosn(event)
    lst.append((event.x,event.y))    

def create_table():
    tl1 = Toplevel(root)
    tl1.title("TABLE")
    lstbox = Listbox(tl1,width=30,height=200)
    for i in range(len(lst)):
        lstbox.insert(END,f"x={lst[i][0]} y={lst[i][1]}")
    lstbox.pack(side='left',fill='both')

def create_table_load():
    tl2 = Toplevel(root)
    tl2.title("TABLE LOAD DATA")
    lstboxLD = Listbox(tl2,width=30,height=200)
    for i in range(len(lstload)):
        lstboxLD.insert(END,f"x={lstload[i][0]} y={lstload[i][1]}")
    lstboxLD.pack(side='left',fill='both')

def clear_canvas():
    canvas.delete("all")
    lst.clear()

def saving_data():
    files = os.listdir(directory_files)
    np.save(f"main/saves/data{len(files)}",lst[1:])
    tkinter.messagebox.showinfo(message=f"data saved in main/saves/data{len(files)}")

def create_from_load():
    clear_canvas()
    for k in range(len(lstload)):
        if (k < len(lstload)):
            canvas.create_line((lstload[k][0],lstload[k][1], lstload[k+1][0],lstload[k+1][1]))

def graphic_show():
    X = []
    for i in range(len(lstload)):
        X.append(lstload[i][0])
    Y = []
    for i in range(len(lstload)):
        Y.append(lstload[i][1])
    X = np.array(X)
    Y = np.array(Y)
    fig, ax = plt.subplots()
    ax.plot(X,Y,color='C1')
    ax.grid()
    plt.show()

def choose_file():
    name = fd.askopenfilename(title='numpy files',filetypes=[('Numpy files', '.npy')])
    global lstload
    lstload = []
    lstload.clear()
    lstload = np.load(f"{name}")
    btn6.configure(state=NORMAL)
    btn7.configure(state=NORMAL)
    tkinter.messagebox.showinfo(message=f"data load from {name}")

#INTERFACE
canvas = Canvas(root,bg='white',width=1100,height=500)
canvas.grid(column=0, row=0,sticky=(E))
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

btn1 = Button(root,width=15, height=5,text='create table', command=lambda:create_table())
btn1.grid(column=0,row=1)

btn2 = Button(root,width=15, height=5,text='clear', command=lambda:clear_canvas())
btn2.grid(column=0,row=2)

btn3 = Button(root,width=15, height=5,text='save', command=lambda:saving_data())    
btn3.grid(column=0,row=3)

btn6 = Button(root,width=15, height=5,text='print', state=DISABLED, command=lambda:create_from_load())
btn6.grid(column=1,row=0)

btn7 = Button(root,width=15, height=5,text='show', state=DISABLED, command=lambda:graphic_show())
btn7.grid(column=1,row=1)

btn8 = Button(root,width=15, height=5,text='choose file', command=lambda:choose_file())
btn8.grid(column=2,row=0)

btn9 = Button(root,width=15, height=5,text='create load data table', command=lambda:create_table_load())
btn9.grid(column=2,row=1)

root.mainloop()