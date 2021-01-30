import os
from tkinter import*
root=Tk()
root.geometry('900x200')
root.title("Graphing Calculator")
l=Label(root, text="Choose one of the given options!", font=("Arial Bold", 25))
l.grid(row=0,column=0)

def fourier():
    os.system('fourier.py')

def ft():
    os.system('fourier_transformation.py')    

b2=Button(root,text="Fourier Series",bg="cyan", fg="blue",font=("Arial Bold", 15),command=fourier)
b2.grid(row=2,column=0)

b5=Button(root,text="A fourier Transform",bg="grey", fg="black",font=("Arial Bold", 15),command=ft)
b5.grid(row=2,column=2)
