from tkinter import *
import customtkinter
from PIL import Image,ImageTk
from tkinter import ttk

#importar barra de progresso
from tkinter.ttk import Progressbar

#importar matplotlib (graficos)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


root = Tk()

root.title()
root.geometry('900x650')
root.configure(background='#e9edf5')
root.resizable(width=FALSE, height=FALSE)

#Frame top
frameTop =  customtkinter.CTkFrame(root,fg_color='white', width=1043,height=40,relief = 'flat',border_width=1,border_color='#DCDCDC')
frameTop.grid(row=0,column=0,pady=1)

frameMid =  customtkinter.CTkFrame(root,corner_radius=8,fg_color='white', width=890,height=350,relief = 'raised',border_width=1,border_color='#DCDCDC')
frameMid.grid(row=1,column=0,pady=1,padx=5,sticky=W)

frameDown =  customtkinter.CTkFrame(root,corner_radius=8,fg_color='white', width=890,height=240,relief = 'flat',border_width=1,border_color='#DCDCDC')
frameDown.grid(row=2,column=0,pady=1,padx=5,sticky=W)

frame_gra_pie = Frame(frameMid, width=580, height=250)
frame_gra_pie.place(x=415, y=5)



app_image = Image.open('iconDin.jpg')
app_image = app_image.resize((35,35))
app_image = ImageTk.PhotoImage(app_image)

app_logo = Label(frameTop, image=app_image, text="Orçamento Pessoal",width=900,compound=LEFT,padx=5,relief=RAISED,anchor=NW,font=('Roboto 18 bold'),bg='white')
app_logo.place(x=0,y=0)


#percentual --
def percentual():
    lbl_nome = Label(frameMid, text="Percentual Gasto",height=1,anchor=NW,font=('Verdana 14',),bg='white')
    lbl_nome.place(x=60,y=5),


    bar =  customtkinter.CTkProgressBar(frameMid,height=20,progress_color='lightblue')
    bar.place(x=10,y=35)
    bar['value']= 50

    valor = 50
    lbl_porcentagem = Label(frameMid,text='{:,.2f}%'.format(valor),height=1,anchor=NW,font=('verdana 12'),bg='white')
    lbl_porcentagem.place(x=220,y=35)

def grafBar():
    lista_categorias = ['Renda','Despesas','Saldo']
    lista_valores = [3000,2000,6236]

    figura = plt.figure(figsize=(4,3.45),dpi=60)
    ax = figura.add_subplot(111)
    ax.bar(lista_categorias,lista_valores, color='red',width=0.9)

    c = 0

    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='#F5F5F5')

        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMid)
    canva.get_tk_widget().place(x=10, y=70)

def resumo():
    valor = [500,600,420]

    l_linha = Label(frameMid,text='',width=215,height=1,anchor=NW, font=('Arial 1'),bg='#545454')
    l_linha.place(x=309, y=52)
    l_renda = Label(frameMid,text='Total Renda Mensal      '.upper(),anchor=NW, font=('verdana 12'),bg='white')
    l_renda.place(x=309, y=35)
    l_valor_renda = Label(frameMid,text='R$ {:,.2f}'.format(valor[0]),anchor=NW, font=('verdana 12'),bg='white')
    l_valor_renda.place(x=309, y=65)

    l_linha2 = Label(frameMid,text='',width=215,height=1,anchor=NW, font=('Arial 1'),bg='#545454')
    l_linha2.place(x=309, y=132)
    l_despesas = Label(frameMid,text='Total Despesas Mensais   '.upper(),anchor=NW, font=('verdana 12'),bg='white')
    l_despesas.place(x=309, y=115)
    l_valor_despesa = Label(frameMid,text='R$ {:,.2f}'.format(valor[1]),anchor=NW, font=('verdana 12'),bg='white')
    l_valor_despesa.place(x=309, y=150)

    l_linha3 = Label(frameMid,text='',width=215,height=1,anchor=NW, font=('Arial 1'),bg='white')
    l_linha3.place(x=309, y=207)
    l_saldo = Label(frameMid,text='Total Saldo Mensal      '.upper(),anchor=NW, font=('verdana 12'),bg='white')
    l_saldo.place(x=309, y=190)
    l_valor_saldo = Label(frameMid,text='R$ {:,.2f}'.format(valor[2]),anchor=NW, font=('verdana 12'),bg='white')
    l_valor_saldo.place(x=309, y=220)

def grafico_pie():
    figura = plt.Figure(figsize=(5,3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_despesas = ['Renda','Despesa','Saldo']

     # only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_valores:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%',shadow=True, startangle=90)
    ax.legend(lista_valores, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)

#-------------------------------------------------------------------------------------------------------------------------------#

# Frames para tabelas de baixo #
frame_renda = Frame(frameDown, width=300, height=230,bg='white')
frame_renda.grid(row=0,column=0,padx=5,pady=5)

frame_operacoes = Frame(frameDown, width=220, height=230,bg='white')
frame_operacoes.grid(row=0,column=1, padx=5)

frame_configuracao = Frame(frameDown, width=220, height=230,bg='white')
frame_configuracao.grid(row=0,column=2, padx=5)

# funcao para mostrar_renda
def mostrar_renda():

    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


percentual()
grafBar()
resumo()
grafico_pie()
mostrar_renda()
root.mainloop()