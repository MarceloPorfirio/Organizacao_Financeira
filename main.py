from tkinter import *
import customtkinter
from PIL import Image,ImageTk
from tkinter import ttk

#importar barra de progresso
from tkinter.ttk import Progressbar

#importar matplotlib (graficos)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as plt
from matplotlib.figure import Figure


root = Tk()

root.title()
root.geometry('900x650')
root.configure(background='#e9edf5')
root.resizable(width=FALSE, height=FALSE)

#Frame top
frameTop =  customtkinter.CTkFrame(root,fg_color='white', width=1043,height=40,relief = 'flat',border_width=1,border_color='#DCDCDC')
frameTop.grid(row=0,column=0,pady=1)

frameMid =  customtkinter.CTkFrame(root,corner_radius=8,fg_color='#F5F5F5', width=890,height=361,relief = 'raised',border_width=1,border_color='#DCDCDC')
frameMid.grid(row=1,column=0,pady=1,padx=5,sticky=W)

frameDown =  customtkinter.CTkFrame(root,corner_radius=8,fg_color='#F5F5F5', width=890,height=240,relief = 'flat',border_width=1,border_color='#DCDCDC')
frameDown.grid(row=2,column=0,pady=1,padx=5,sticky=W)


app_image = Image.open('iconDin.jpg')
app_image = app_image.resize((35,35))
app_image = ImageTk.PhotoImage(app_image)

app_logo = Label(frameTop, image=app_image, text="Orçamento Pessoal",width=900,compound=LEFT,padx=5,relief=RAISED,anchor=NW,font=('Roboto 18 bold'),bg='white')
app_logo.place(x=0,y=0)


#percentual --
def percentual():
    lbl_nome = Label(frameMid, text="Percentual Gasto",height=1,anchor=NW,font=('Verdana 14',),bg='#F5F5F5')
    lbl_nome.place(x=60,y=5),


    bar =  customtkinter.CTkProgressBar(frameMid,height=20,progress_color='lightblue')
    bar.place(x=10,y=35)
    bar['value']= 50

    valor = 50
    lbl_porcentagem = Label(frameMid,text='{:,.2f}%'.format(valor),height=1,anchor=NW,font=('verdana 12'),bg='#F5F5F5')
    lbl_porcentagem.place(x=220,y=35)
percentual()
root.mainloop()