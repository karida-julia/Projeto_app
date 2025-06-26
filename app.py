from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

co0 = "#000000"
co1 = "#feffff"
co2 = "#9400d3"
co3 = "#38576b"
co4 = "#403d3d"


janela = Tk()
janela.title("")
janela.geometry("400x300")
janela.configure(bg=co1)
janela.resizable(False, False)
#configuração do frame cima
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief= "flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, stick=NSEW)
frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
#configuração de linhas
l_nome = Label(frame_cima, text="LOGIN", height=1, anchor=NE, font =('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, width=275, text="", height=1, anchor = NW, font=('Ivy 1'), bg=co2)
l_linha.place(x=10, y=45)

credenciais = ['', '']
#função para verificar senha
def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo(a) Admin!!!!' )

    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo(a) de volta ' +credenciais[0])

        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verifique o nome de usuario ou a palavra passe')
 #função para gerar janela       
def nova_janela():
    l_nome = Label(frame_cima, text="Usuario: " + credenciais[0], height=1, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)
    
    l_linha = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy 1'), bg = co2)
    l_linha.place(x=10, y=45)
    
    l_nome = Label(frame_baixo, text="Seja Bem vindo "  + credenciais [0], height=1, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)


l_nome = Label(frame_baixo, text= "Nome*" , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text="password *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, show= '*', width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_pass.place(x=15, y=130)

botao_confirmar = Button(frame_baixo, text="Entra", width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confirmar.place(x=15, y=170)

from tkinter import *
from tkinter import ttk

co1 = '#feffff'
c02 = "#9064E7"
co3 = '#000000'

janela = Tk()
janela.title('')
janela.geometry("")
janela.configure(bg=co1)


frame_cima = Frame(janela, width=295, heigth=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=180, bg= co1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row= 0, column=0, sticky=NSEW)
frame_baixo()
style = ttk.Style(janela)
style.themee_use('clam')

l_nome = Label(frame_cima, text='Calculadoras', width=23, height=1, padx=0, relief='flat', font=('Ivy 10 bold'), bg=co1, fg=co2)
l_nome.place(x= 0, y= 25)

b_calculadora_imc = Button(frame_baixo, text='Calculadora IMC', width=6, height=1, padx=0, bg=co2, font=('Ivy 16 bold'), anchor='center') 
b_calculadora_imc.grid(row= 0, column= 1, columspan = 1)
b_calculadora_cientifica = Button(frame_baixo, text='Calculadora IMC', width=6, height=1, padx=0, bg=co2, font=('Ivy 16 bold'), anchor='center')
b_calculadora_cientifica.grid(row=1, column=1, columspan = 1)

from tkinter import *
from tkinter import ttk
import math

co1 = '#feffff'
co2 = '#6f9fbd'
co3 = '#38576b'

fundo = '#e8e6e6'
co10 = '#363434'
cor11 = '#424345'

cor1 ='#ffab40'
cor2 ='#ff333a'
cor3 ='#6bd66f'
cor4 ='#ab8918'


janela = Tk()
janela.title('')
janela.geometry('235x289')
janela.configure(bg=co1)


style = ttk.Style(janela)
style.theme_use("clam")

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_score = Frame(janela, width=300, height=56, bg=co3, pady=0, padx=0, relief="flat",)
frame_score.grid(row=1, column=0, sticky=NW)

frame_cientifica = Frame(janela, width=300, height=86, bg=co3, pady=0, padx=0, relief="flat",)
frame_cientifica.grid(row=2, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340, bg=fundo, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=3, column=0, sticky=NW)

def entering_values(event):
    global all_values
    all_values = all_values + str(event)
    value_text.set(all_values)

def calculate():
    global all_values
    global texto
    texto = all_values

    modulos = ['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log', 'math.log10', 'math.e', 'math.pow' , 'math.pi', 'math.radian']

    for i in modulos:
        if i == 'math.tan':
            texto = texto.replace("tan", i)
        if i == 'math.sin':
            texto = texto.replace("sin", i)
        if i == 'math.cos':
            texto = texto.replace("cos", i)
        if i == 'math.sqrt':
            texto = texto.replace("sqrt", i)

        if i == 'math.log':
            texto = texto.replace("log", i)
        if i == 'math.log10':
            texto = texto.replace("log10", i)
        if i == 'math.e':
            texto = texto.replace("e",i)
        if i == 'math.pow':
            texto = texto.replace("pow",i)

        if i == 'math.radians':
            texto = texto.replace("rad", i)
        if i == 'math.pi':
            texto = texto.replace("pi", i)

    result = str(eval(texto))

    print(result)
    print(texto)

    value_text.set(result)
    all_values = ""

def scream_clear():
    global all_values
    all_values = ""
    value_text.set("")

all_values= ""

value_text = StringVar()

app_scream = Label(frame_score, width=16, height=2, textvariable= value_text, padx=7, relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg= '#37474f', fg=co1)
app_scream.place(x=0, y=0)

b_tan = Button(frame_cientifica, text="tan", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('tan'))
b_tan.place(x=0, y=1)

b_sin = Button(frame_cientifica, text="sin", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('sin'))
b_sin.place(x=59, y=1)

b_cos = Button(frame_cientifica, text="cos", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('cos'))
b_cos.place(x=118, y=1)

b_sqrt = Button(frame_cientifica, text="sqrt", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('sqrt'))
b_sqrt.place(x=177, y=1)

b_log = Button(frame_cientifica, text="log", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('log'))
b_log.place(x=0, y=30)

b_log10 = Button(frame_cientifica, text="log10", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('log10'))
b_log10.place(x=59, y=30)

b_euler = Button(frame_cientifica, text="e", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('e'))
b_euler.place(x=118, y=30)

b_pow = Button(frame_cientifica, text="pow", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('pow'))
b_pow.place(x=177, y=30)

b_12 = Button(frame_cientifica, text="pi", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('pi'))
b_12.place(x=0, y=58)

b_13= Button(frame_cientifica, text=",", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(','))
b_13.place(x=59, y=58)

b_14 = Button(frame_cientifica, text="(", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('('))
b_14.place(x=118, y=58)

b_15 = Button(frame_cientifica, text=")", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(')'))
b_15.place(x=177, y=58)

b_l = Button(frame_quadros, text="C", width=14, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:scream_clear())
b_l.place(x=0, y=0)

b_2 = Button(frame_quadros, text="%", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('%'))
b_2.place(x=118, y=0)

b_3 = Button(frame_quadros, text="/", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('/'))
b_3.place(x=177, y=0)

b_4 = Button(frame_quadros, text="7", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(7))
b_4.place(x=0, y=29)

b_5 = Button(frame_quadros, text="8", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(8))
b_5.place(x=59, y=29)

b_6 = Button(frame_quadros, text="9", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(9))
b_6.place(x=118, y=29)

b_7= Button(frame_quadros, text="*", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('*'))
b_7.place(x=177, y=29)

b_8 = Button(frame_quadros, text="4", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(4))
b_8.place(x=0, y=58)

b_9 = Button(frame_quadros, text="5", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(5))
b_9.place(x=59, y=58)

b_10 = Button(frame_quadros, text="6", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(6))
b_10.place(x=118, y=58)

b_11 = Button(frame_quadros, text="-", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('-'))
b_11.place(x=177, y=58)

b_12 = Button(frame_quadros, text="1", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(1))
b_12.place(x=0, y=87)

b_13 = Button(frame_quadros, text="2", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(2))
b_13.place(x=59, y=87)

b_14 = Button(frame_quadros, text="3", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(3))
b_14.place(x=118, y=87)

b_15 = Button(frame_quadros, text="+", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('+'))
b_15.place(x=177, y=87)

b_16 = Button(frame_quadros, text="0", width=14, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(0))
b_16.place(x=0, y=116)

b_17 = Button(frame_quadros, text=".", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('.'))
b_17.place(x=118, y=116)

b_18 = Button(frame_quadros, text="=", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:calculate())
b_18.place(x=177, y=116)

from tkinter import *
from tkinter import ttk


co0 = "#4B0082"
co1 = "#F8F8FF"
co2 = "#C7C7C7"

janela = Tk()
janela.title('')
janela.geometry('235x289')
janela.configure(bg=co1)

frame_cima = Frame(janela, width=295, height=50, bg=co1, pady=0, padx=0,relief='flat')
frame_cima.grid(row=0, column=0,sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=180, bg=co1, pady=0, padx=0,relief='flat')
frame_baixo.grid(row=1, column=0,sticky=NSEW)

app_nome = Label(frame_cima, text='CALCULADORA DE IMC', width=30, height=1, pady=0, padx=0, font=('Ivy 10 bold'), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

def calcular():

    imc= peso/altura**2

    resultado = imc

    if imc < 18.5:
        l_resultado['text'] = "Seu IMC é: Abaixo Do Peso"
    elif 18.5 <= imc <24.9:
        l_resultado['text'] = "Seu IMC é: Normal"
    elif 25 <=imc < 29.9:
        l_resultado['text'] = "Seu IMC é: Sobrepeso "
    else:
        l_resultado['text'] = "Seu imc é: Obeso"

    l_resultado['text'] = "{:.{}f}".format(resultado,2)


l_peso = Label(frame_baixo, text='insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
l_peso.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)


l_altura = Label(frame_baixo, text='insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
l_altura.grid(row=0, column=0, sticky=NSEW, pady=25, padx=3)

l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6, pady=12, anchor='center', font=('Ivy 24 bold'), bg=co0, fg=co1)
l_resultado.place(x=175, y=10)

l_resultado = Label(frame_baixo, text='', width=37, height=1, padx=0, pady=12, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_resultado.place(x=0, y=90)

b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', )
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, comlumspan=30)

janela.mainloop()


































































