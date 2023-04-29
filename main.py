from tkinter import *
import customtkinter
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox

#importar barra de progresso
from tkinter.ttk import Progressbar

#importar matplotlib (graficos)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

root = Tk()

root.title('Gestão Pessoal')
root.geometry('1000x600')
root.configure(background='#e9edf5')
root.resizable(width=FALSE, height=FALSE)
style = ttk.Style(root)
style.configure("RoundedButton", padding=6, relief="flat",
                foreground="#ffffff", background="#2c3e50")


colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#Frame top
frameTop =  customtkinter.CTkFrame(root,fg_color='white', width=990,height=40,relief = 'flat',border_width=1,border_color='#DCDCDC')
frameTop.place(relx=0.005,rely=0.01)

frameMid =  customtkinter.CTkFrame(root,corner_radius=8,fg_color='white', width=990,height=300,relief = 'raised',border_width=1,border_color='#DCDCDC')
frameMid.place(relx=0.005,rely=0.08)

frameDown =  customtkinter.CTkFrame(root,corner_radius=8,fg_color='white', width=990,height=300,relief = 'flat',border_width=1,border_color='#DCDCDC')
frameDown.place(relx=0.005,rely=0.58)

frame_gra_pie = Frame(frameMid, width=600, height=250)
frame_gra_pie.place(x=430, y=5)



app_image = Image.open('iconDin.jpg')
app_image = app_image.resize((35,35))
app_image = ImageTk.PhotoImage(app_image)

app_logo = Label(frameTop, image=app_image, text="Orçamento Pessoal",width=990,compound=LEFT,padx=5,relief=RAISED,anchor=NW,font=('Roboto 18 bold'),bg='white')
app_logo.place(x=0,y=0)

# Funções -------------------------------------------------------------------

global tree

def inserir_categoria_b():
    nome = e_n_categoria.get()
    lista_inserir = [nome]
    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro','Preencha todos os campos')
            return
    # passando a lista para a função inserir gastos
    inserir_categoria(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos!')

    e_n_categoria.delete(0,'end')

            # Pegando os valores da categoria
    categoria_funcao = ver_categoria()
    categoria = []
            
    for i in categoria_funcao:
        categoria.append(i[1])

            # atualizar a lista de categorias
        combo_categoria_despesa['values'] = (categoria)

# função inserir receitas
def iserir_receita_b():
    nome = 'Receita'
    data = e_cal_receitas.get()
    valor = e_valor_receitas.get()

    lista_inserir = [nome,data,valor]
    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro','Preencha todos os campos')
            return
    
    #chamando a função inserir receitas presentes na view
    inserir_receitas(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos!')

    e_cal_receitas.delete(0,'end')
    e_valor_receitas.delete(0,'end')
     
    #atualizando dados
    mostrar_renda()
    percentual()
    grafico_pie()
    resumo()
    grafBar()
# função inserir despesas
def inserir_despesas():
    nome = combo_categoria_despesa.get()
    data = e_cal_despesas.get()
    valor = e_valor_despesas.get()

    lista_inserir = [nome,data,valor]
    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro','Preencha todos os campos')
            return
    #chamando a função inserir despesas presentes na view
    inserir_gastos(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos!')

    combo_categoria_despesa.delete(0,'end')
    e_cal_despesas.delete(0,'end')
    e_valor_despesas.delete(0,'end')
     
    #atualizando dados
    mostrar_renda()
    percentual()
    grafico_pie()
    resumo()
    grafBar()

def deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]

        if nome == "Receita":
            deletar_receitas([valor])
            messagebox.showinfo('Sucesso','Os dados foram deletados!')

            #atualizando dados
            mostrar_renda()
            percentual()
            grafico_pie()
            resumo()
            grafBar()

        else:
            deletar_gastos([valor])
            messagebox.showinfo('Sucesso','Os dados foram deletados!')

            #atualizando dados
            mostrar_renda()
            percentual()
            grafico_pie()
            resumo()
            grafBar()

    except IndexError: # se o index estiver vazio (id da tabela no caso)
        messagebox.showerror('Erro','Selecione os dados da Tabela.')
#-------------------------------------------------------------------------------------------------
#percentual --
def percentual():
    lbl_nome = Label(frameMid, text="Percentual Gasto",height=1,anchor=NW,font=('Verdana 14',),bg='white')
    lbl_nome.place(x=60,y=5),


    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frameMid, length=180,style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value']= percentual_valores()[0]

    valor = percentual_valores()[0]
    lbl_porcentagem = Label(frameMid,text='{:,.2f}%'.format(valor),height=1,anchor=NW,font=('verdana 12'),bg='white')
    lbl_porcentagem.place(x=220,y=35)

def grafBar():
    lista_categorias = ['Renda','Despesas','Saldo']
    lista_valores = bar_valores()

    figura = plt.figure(figsize=(4,3.45),dpi=60)
    ax = figura.add_subplot(111)
    ax.bar(lista_categorias,lista_valores, color=colors,width=0.9)

    c = 0

    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom')

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
    valor = bar_valores()

    l_linha = Label(frameMid,text='',width=215,height=1,anchor=NW, font=('Arial 1'),bg='#545454')
    l_linha.place(x=312, y=52)
    l_renda = Label(frameMid,text='Total Renda Mensal      '.upper(),anchor=NW, font=('verdana 12'),bg='white')
    l_renda.place(x=312, y=35)
    l_valor_renda = Label(frameMid,text='R$ {:,.2f}'.format(valor[0]),anchor=NW, font=('verdana 12'),bg='white')
    l_valor_renda.place(x=309, y=65)

    l_linha2 = Label(frameMid,text='',width=215,height=1,anchor=NW, font=('Arial 1'),bg='#545454')
    l_linha2.place(x=312, y=132)
    l_despesas = Label(frameMid,text='Total Despesas Mensais   '.upper(),anchor=NW, font=('verdana 12'),bg='white')
    l_despesas.place(x=312, y=115)
    l_valor_despesa = Label(frameMid,text='R$ {:,.2f}'.format(valor[1]),anchor=NW, font=('verdana 12'),bg='white')
    l_valor_despesa.place(x=312, y=150)

    l_linha3 = Label(frameMid,text='',width=215,height=1,anchor=NW, font=('Arial 1'),bg='white')
    l_linha3.place(x=312, y=207)
    l_saldo = Label(frameMid,text='Total Saldo Mensal      '.upper(),anchor=NW, font=('verdana 12'),bg='white')
    l_saldo.place(x=312, y=190)
    l_valor_saldo = Label(frameMid,text='R$ {:,.2f}'.format(valor[2]),anchor=NW, font=('verdana 12'),bg='white')
    l_valor_saldo.place(x=312, y=220)

def grafico_pie():
    figura = plt.Figure(figsize=(5,3), dpi=90) #dpi espessura da figura
    ax = figura.add_subplot(111)
    lista_valores = pie_valores()[1]
    lista_categorias = pie_valores()[0]

     # only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.25), autopct='%1.1f%%',shadow=True, startangle=90)
    ax.legend(lista_categorias
    , loc="center right", bbox_to_anchor=(1.60, 0.50)) # largura e altura da legenda

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)

#-------------------------------------------------------------------------------------------------------------------------------#

# Frames para tabelas de baixo #
frame_renda = Frame(frameDown, width=330, height=230,bg='white')
frame_renda.grid(row=0,column=0,padx=5,pady=5)

frame_operacoes = Frame(frameDown, width=330, height=230,bg='white')
frame_operacoes.grid(row=0,column=1, padx=5)

frame_configuracao = Frame(frameDown, width=284, height=230,bg='white')
frame_configuracao.grid(row=0,column=2, padx=5)

# funcao para mostrar_renda
def mostrar_renda():

    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Valor']

    lista_itens = tabela()
    
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

# Configurações de despesas

l_descricao = Label(frame_operacoes,text= 'Insira novas despesas', height=1,anchor=NW,font=('verdana 10 bold'),bg='white')
l_descricao.place(x=10,y=5)


# Adicionar categoria
l_categoria = Label(frame_operacoes,text= 'Categoria', height=1,anchor=NW,font=('verdana 10'),bg='white')
l_categoria.place(x=25,y=40)

# Lista de categorias
categoria_funcao = ver_categoria()
categoria = []

for i in categoria_funcao:
    categoria.append(i[1]) #pega apenas o primeiro elemento da lista, tirando o ID, por isso [1]

combo_categoria_despesa = ttk.Combobox(frame_operacoes,width=12)
combo_categoria_despesa['values'] = (categoria)
combo_categoria_despesa.place(x=110,y=40)

l_cal_despesas = Label(frame_operacoes,text='Data', height=1,anchor=NW,font=('Verdana 10'),bg='white')
l_cal_despesas.place(x=25, y=70)

e_cal_despesas = DateEntry(frame_operacoes,width=12,background = 'darkblue',foreground='white', borderwidth=2,year=2022)
e_cal_despesas.place(x=110,y=70)

# Valor ----------

l_valor_despesas = Label(frame_operacoes, text="Valor",width=20,height=1,anchor=NW, font=('Ivy 10 '), bg='white')
l_valor_despesas.place(x=25, y=100)
e_valor_despesas = Entry(frame_operacoes, width=14, justify='left',relief="solid")
e_valor_despesas.place(x=110, y=100)

# Botao Inserir
img_add_despesas  = Image.open('Button-Add-icon.png')
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)

botao_inserir_despesas = Button(frame_operacoes,image=img_add_despesas,command=inserir_despesas, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg='white' )
botao_inserir_despesas.place(x=110, y=130)

# operacao Excluir -----------------------
l_n_categoria = Label(frame_operacoes, text="Excluir", height=1,anchor=NW, font=('Ivy 10 bold'), bg='white')
l_n_categoria.place(x=25, y=190)

img_delete  = Image.open('delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frame_operacoes, image=img_delete, command=deletar_dados, compound=LEFT, anchor=NW, text="   Deletar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg='white' )
botao_deletar.place(x=110, y=190)

# Configuracoes Receitas -----------------------------------

l_descricao = Label(frame_configuracao, text="Insira novas receitas", height=1,anchor=NW,relief="flat", font=('Verdana 10 bold'),bg='white')
l_descricao.place(x=10, y=5)

l_cal_receitas = Label(frame_configuracao, text="Data", height=1,anchor=NW, font=('Ivy 10 '), bg='white')
l_cal_receitas.place(x=10, y=40)
e_cal_receitas = DateEntry(frame_configuracao, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
e_cal_receitas.place(x=110, y=41)

l_valor_receitas = Label(frame_configuracao, text="Valor", height=1,anchor=NW, font=('Ivy 10 '), bg='white')
l_valor_receitas.place(x=10, y=70)
e_valor_receitas = Entry(frame_configuracao, width=14, justify='left',relief="solid")
e_valor_receitas.place(x=110, y=71)

# Botao Inserir
img_add_receitas  = Image.open('Button-Add-icon.png')
img_add_receitas = img_add_receitas.resize((17,17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)
botao_inserir_receitas = Button(frame_configuracao, image=img_add_receitas,command=iserir_receita_b, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg='white')
botao_inserir_receitas.place(x=110, y=111)


# operacao Nova Categoria -----------------------

l_n_categoria = Label(frame_configuracao, text="Categoria", height=1,anchor=NW, font=('Ivy 10 bold'), bg='white')
l_n_categoria.place(x=10, y=160)
e_n_categoria = Entry(frame_configuracao, width=14, justify='left',relief="solid")
e_n_categoria.place(x=110, y=160)

# Botao Inserir
img_add_categoria  = Image.open('Button-Add-icon.png')
img_add_categoria = img_add_categoria.resize((17,17))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria)
botao_inserir_categoria = Button(frame_configuracao,image=img_add_categoria,command=inserir_categoria_b, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg='white' )
botao_inserir_categoria.place(x=110, y=190)




percentual()
grafBar()
resumo()
grafico_pie()
mostrar_renda()
root.mainloop()