from tkinter import *

import customtkinter

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




root.mainloop()