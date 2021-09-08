
import tkinter
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import *

global barra_1_vetor_global
global barra_2_vetor_global
global barra_3_vetor_global
global barra_4_vetor_global
global barra_5_vetor_global
global barra_6_vetor_global
global barra_7_vetor_global
global barra_8_vetor_global
global barra_9_vetor_global




# Janela de barras-------------------------------------------------------------------------------------------------------
def barra():
    barra_window = Tk()
    barra_window.title('Barras')
    barra_window.iconbitmap('imagens/engenharia.ico')  # icone
    barra_window.geometry("1366x768")

    lb_resistencias = LabelFrame(barra_window, text="Elementos de barras",  borderwidth=1, relief="solid")
    lb_resistencias.place(x=2, y=5, width=795, height=385)

    def center_window(w=1000, h=1000):
        # get screen width and height
        ws = barra_window.winfo_screenwidth()
        hs = barra_window.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        barra_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    center_window(800, 395)
    barra_window.resizable(0, 0)


    #label_barra = Label(barra_window, text="Dados das Barras", font=44)
    #label_barra.place(x=440, y=10)
    label_barrainicial = Label(barra_window, text="Barra Inicial")
    label_barrainicial.place(x=10, y=40)
    label_barrainicial1 = Label(barra_window, text="1")
    label_barrainicial1.place(x=40, y=70)
    label_barrainicial2 = Label(barra_window, text="2")
    label_barrainicial2.place(x=40, y=100)
    label_barrainicial3 = Label(barra_window, text="3")
    label_barrainicial3.place(x=40, y=130)
    label_barrainicial4 = Label(barra_window, text="4")
    label_barrainicial4.place(x=40, y=160)
    label_barrainicial5 = Label(barra_window, text="5")
    label_barrainicial5.place(x=40, y=190)
    label_barrainicial6 = Label(barra_window, text="6")
    label_barrainicial6.place(x=40, y=220)
    label_barrainicial7 = Label(barra_window, text="7")
    label_barrainicial7.place(x=40, y=250)
    label_barrainicial8 = Label(barra_window, text="8")
    label_barrainicial8.place(x=40, y=280)
    label_barrainicial9 = Label(barra_window, text="9")
    label_barrainicial9.place(x=40, y=310)

    label_noinicial = Label(barra_window, text="Nó Inicial")
    label_noinicial.place(x=115, y=40)
    vetor_no_valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    combo_1_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_1_no.place(x=120, y=70)
    combo_2_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_2_no.place(x=120, y=100)
    combo_3_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_3_no.place(x=120, y=130)
    combo_4_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_4_no.place(x=120, y=160)
    combo_5_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_5_no.place(x=120, y=190)
    combo_6_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_6_no.place(x=120, y=220)
    combo_7_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_7_no.place(x=120, y=250)
    combo_8_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_8_no.place(x=120, y=280)
    combo_9_no = Combobox(barra_window, values=vetor_no_valor, width=5)
    combo_9_no.place(x=120, y=310)

    vetor_nofinal_valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    label_nofinal = Label(barra_window, text="Nó Final")
    label_nofinal.place(x=200, y=40)

    combo_1_no.insert(END, "0")
    combo_2_no.insert(END, "0")
    combo_3_no.insert(END, "0")
    combo_4_no.insert(END, "0")
    combo_5_no.insert(END, "0")
    combo_6_no.insert(END, "0")
    combo_7_no.insert(END, "0")
    combo_8_no.insert(END, "0")
    combo_9_no.insert(END, "0")


    combo_1_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_1_nofinal.place(x=200, y=70)
    combo_2_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_2_nofinal.place(x=200, y=100)
    combo_3_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_3_nofinal.place(x=200, y=130)
    combo_4_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_4_nofinal.place(x=200, y=160)
    combo_5_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_5_nofinal.place(x=200, y=190)
    combo_6_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_6_nofinal.place(x=200, y=220)
    combo_7_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_7_nofinal.place(x=200, y=250)
    combo_8_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_8_nofinal.place(x=200, y=280)
    combo_9_nofinal = Combobox(barra_window, values=vetor_nofinal_valor, width=5)
    combo_9_nofinal.place(x=200, y=310)

    combo_1_nofinal.insert(END, "0")
    combo_2_nofinal.insert(END, "0")
    combo_3_nofinal.insert(END, "0")
    combo_4_nofinal.insert(END, "0")
    combo_5_nofinal.insert(END, "0")
    combo_6_nofinal.insert(END, "0")
    combo_7_nofinal.insert(END, "0")
    combo_8_nofinal.insert(END, "0")
    combo_9_nofinal.insert(END, "0")



    label_alturautil = Label(barra_window, text="Altura útil(m)")
    label_alturautil.place(x=280, y=40)

    # criação das entry
    # criação das entry
    no_1_alturautil = Entry(barra_window)
    no_1_alturautil.place(x=290, y=70, height=20, width=50)
    no_1_alturautil.insert(END, "0")

    no_2_alturautil = Entry(barra_window)
    no_2_alturautil.place(x=290, y=100, height=20, width=50)
    no_2_alturautil.insert(END, "0")

    no_3_alturautil = Entry(barra_window)
    no_3_alturautil.place(x=290, y=130, height=20, width=50)
    no_3_alturautil.insert(END, "0")

    no_4_alturautil = Entry(barra_window)
    no_4_alturautil.place(x=290, y=160, height=20, width=50)
    no_4_alturautil.insert(END, "0")

    no_5_alturautil = Entry(barra_window)
    no_5_alturautil.place(x=290, y=190, height=20, width=50)
    no_5_alturautil.insert(END, "0")

    no_6_alturautil = Entry(barra_window)
    no_6_alturautil.place(x=290, y=220, height=20, width=50)
    no_6_alturautil.insert(END, "0")

    no_7_alturautil = Entry(barra_window)
    no_7_alturautil.place(x=290, y=250, height=20, width=50)
    no_7_alturautil.insert(END, "0")

    no_8_alturautil = Entry(barra_window)
    no_8_alturautil.place(x=290, y=280, height=20, width=50)
    no_8_alturautil.insert(END, "0")

    no_9_alturautil = Entry(barra_window)
    no_9_alturautil.place(x=290, y=310, height=20, width=50)
    no_9_alturautil.insert(END, "0")

    label_bf = Label(barra_window, text="Bf(m)")
    label_bf.place(x=390, y=40)
    no_1_bf = Entry(barra_window)
    no_1_bf.place(x=390, y=70, height=20, width=50)
    no_1_bf.insert(END, "0")

    no_2_bf = Entry(barra_window)
    no_2_bf.place(x=390, y=100, height=20, width=50)
    no_2_bf.insert(END, "0")

    no_3_bf = Entry(barra_window)
    no_3_bf.place(x=390, y=130, height=20, width=50)
    no_3_bf.insert(END, "0")

    no_4_bf = Entry(barra_window)
    no_4_bf.place(x=390, y=160, height=20, width=50)
    no_4_bf.insert(END, "0")

    no_5_bf = Entry(barra_window)
    no_5_bf.place(x=390, y=190, height=20, width=50)
    no_5_bf.insert(END, "0")

    no_6_bf = Entry(barra_window)
    no_6_bf.place(x=390, y=220, height=20, width=50)
    no_6_bf.insert(END, "0")

    no_7_bf = Entry(barra_window)
    no_7_bf.place(x=390, y=250, height=20, width=50)
    no_7_bf.insert(END, "0")

    no_8_bf = Entry(barra_window)
    no_8_bf.place(x=390, y=280, height=20, width=50)
    no_8_bf.insert(END, "0")

    no_9_bf = Entry(barra_window)
    no_9_bf.place(x=390, y=310, height=20, width=50)
    no_9_bf.insert(END, "0")

    # configurar com formula

    label_momentoinercia = Label(barra_window, text="Mom. de Inércia(m4)")
    label_momentoinercia.place(x=450, y=40)

    # configurar com formula

    label_elasticidade = Label(barra_window, text="Módulo de Elasticidade")
    label_elasticidade.place(x=620, y=40)

    no_1_elasticidade = Entry(barra_window)

    no_1_elasticidade.place(x=650, y=70, height=20, width=50)

    no_2_elasticidade = Entry(barra_window)
    no_2_elasticidade.place(x=650, y=100, height=20, width=50)

    no_3_elasticidade = Entry(barra_window)
    no_3_elasticidade.place(x=650, y=130, height=20, width=50)

    no_4_elasticidade = Entry(barra_window)
    no_4_elasticidade.place(x=650, y=160, height=20, width=50)

    no_5_elasticidade = Entry(barra_window)
    no_5_elasticidade.place(x=650, y=190, height=20, width=50)

    no_6_elasticidade = Entry(barra_window)
    no_6_elasticidade.place(x=650, y=220, height=20, width=50)

    no_7_elasticidade = Entry(barra_window)
    no_7_elasticidade.place(x=650, y=250, height=20, width=50)

    no_8_elasticidade = Entry(barra_window)
    no_8_elasticidade.place(x=650, y=280, height=20, width=50)

    no_9_elasticidade = Entry(barra_window)
    no_9_elasticidade.place(x=650, y=310, height=20, width=50)
    no_1_elasticidade = Entry(barra_window)
    no_1_elasticidade.place(x=650, y=70, height=20, width=100)

    no_2_elasticidade = Entry(barra_window)
    no_2_elasticidade.place(x=650, y=100, height=20, width=100)

    no_3_elasticidade = Entry(barra_window)
    no_3_elasticidade.place(x=650, y=130, height=20, width=100)

    no_4_elasticidade = Entry(barra_window)
    no_4_elasticidade.place(x=650, y=160, height=20, width=100)

    no_5_elasticidade = Entry(barra_window)
    no_5_elasticidade.place(x=650, y=190, height=20, width=100)

    no_6_elasticidade = Entry(barra_window)
    no_6_elasticidade.place(x=650, y=220, height=20, width=100)

    no_7_elasticidade = Entry(barra_window)
    no_7_elasticidade.place(x=650, y=250, height=20, width=100)

    no_8_elasticidade = Entry(barra_window)
    no_8_elasticidade.place(x=650, y=280, height=20, width=100)

    no_9_elasticidade = Entry(barra_window)
    no_9_elasticidade.place(x=650, y=310, height=20, width=100)

    no_1_elasticidade.insert(END, "0")
    no_2_elasticidade.insert(END, "0")
    no_3_elasticidade.insert(END, "0")
    no_4_elasticidade.insert(END, "0")
    no_5_elasticidade.insert(END, "0")
    no_6_elasticidade.insert(END, "0")
    no_7_elasticidade.insert(END, "0")
    no_8_elasticidade.insert(END, "0")
    no_9_elasticidade.insert(END, "0")

    # por padrão o vetor barra ( no inicial , final , altura util, bf , mom inercia , elasticidade )

    def update_barra():
        global barra_1_vetor_global
        global barra_2_vetor_global
        global barra_3_vetor_global
        global barra_4_vetor_global
        global barra_5_vetor_global
        global barra_6_vetor_global
        global barra_7_vetor_global
        global barra_8_vetor_global
        global barra_9_vetor_global

        altura_util_vetor = []
        altura_util_vetor = [float(no_1_alturautil.get()), float(no_2_alturautil.get()),float(no_3_alturautil.get()), float(no_4_alturautil.get()),
                             float(no_5_alturautil.get()), float(no_6_alturautil.get()),float(no_7_alturautil.get()), float(no_8_alturautil.get()),float(no_9_alturautil.get())]

        bf_vetor = []
        bf_vetor = [float(no_1_bf.get()), float(no_2_bf.get()), float(no_3_bf.get()), float(no_4_bf.get()),float(no_5_bf.get()),float(no_6_bf.get()), float(no_7_bf.get()), float(no_8_bf.get()), float(no_9_bf.get())]

        momento_inercia_Vetor = []
        momento_inercia_Vetor = [round((bf_vetor[0] * altura_util_vetor[0] ** 3) / 12, 10),
                                 round((bf_vetor[1] * altura_util_vetor[1] ** 3) / 12, 10),
                                 round((bf_vetor[2] * altura_util_vetor[2] ** 3) / 12, 10),
                                 round((bf_vetor[3] * altura_util_vetor[3] ** 3) / 12, 10),
                                 round((bf_vetor[4] * altura_util_vetor[4] ** 3) / 12, 10),
                                 round((bf_vetor[5] * altura_util_vetor[5] ** 3) / 12, 10),
                                 round((bf_vetor[6] * altura_util_vetor[6] ** 3) / 12, 10),
                                 round((bf_vetor[7] * altura_util_vetor[7] ** 3) / 12, 10),
                                 round((bf_vetor[8] * altura_util_vetor[8] ** 3) / 12, 10)]

        # documentação, nó inicial 0, nó final 1 , altura útil 2 , bf 3, inércia 4, elasticidade 5
        barra_1_vetor = []
        barra_1_vetor = [combo_1_no.get(), combo_1_nofinal.get(), no_1_alturautil.get(), no_1_bf.get(),momento_inercia_Vetor[0],
                         no_1_elasticidade.get()]

        barra_1_vetor = []
        barra_1_vetor = [combo_1_no.get(), combo_1_nofinal.get(), no_1_alturautil.get(), no_1_bf.get(),momento_inercia_Vetor[0],no_1_elasticidade.get()]

        barra_2_vetor = []
        barra_2_vetor = [combo_2_no.get(), combo_2_nofinal.get(), no_2_alturautil.get(), no_2_bf.get(),momento_inercia_Vetor[1],no_2_elasticidade.get()]

        barra_3_vetor = []
        barra_3_vetor = [combo_3_no.get(), combo_3_nofinal.get(), no_3_alturautil.get(), no_3_bf.get(),momento_inercia_Vetor[2],no_3_elasticidade.get()]

        barra_4_vetor = []
        barra_4_vetor = [combo_4_no.get(), combo_4_nofinal.get(), no_4_alturautil.get(), no_4_bf.get(),momento_inercia_Vetor[3],no_4_elasticidade.get()]

        barra_5_vetor = []
        barra_5_vetor = [combo_5_no.get(), combo_5_nofinal.get(), no_5_alturautil.get(), no_5_bf.get(),
                         momento_inercia_Vetor[4],
                         no_5_elasticidade.get()]

        barra_6_vetor = []
        barra_6_vetor = [combo_6_no.get(), combo_6_nofinal.get(), no_6_alturautil.get(), no_6_bf.get(),
                         momento_inercia_Vetor[5],
                         no_6_elasticidade.get()]

        barra_7_vetor = []
        barra_7_vetor = [combo_7_no.get(), combo_7_nofinal.get(), no_7_alturautil.get(), no_7_bf.get(),
                         momento_inercia_Vetor[6],
                         no_7_elasticidade.get()]

        barra_8_vetor = []
        barra_8_vetor = [combo_8_no.get(), combo_8_nofinal.get(), no_8_alturautil.get(), no_8_bf.get(),
                         momento_inercia_Vetor[7],
                         no_8_elasticidade.get()]

        barra_9_vetor = []
        barra_9_vetor = [combo_9_no.get(), combo_9_nofinal.get(), no_9_alturautil.get(), no_9_bf.get(),
                         momento_inercia_Vetor[8],
                         no_9_elasticidade.get()]

        label_momentoinercia_1 = Label(barra_window, text=momento_inercia_Vetor[0])
        label_momentoinercia_1.place(x=450, y=70)

        label_momentoinercia_2 = Label(barra_window, text=momento_inercia_Vetor[1])
        label_momentoinercia_2.place(x=450, y=100)

        label_momentoinercia_3 = Label(barra_window, text=momento_inercia_Vetor[2])
        label_momentoinercia_3.place(x=450, y=130)

        label_momentoinercia_4 = Label(barra_window, text=momento_inercia_Vetor[3])
        label_momentoinercia_4.place(x=450, y=160)

        label_momentoinercia_5 = Label(barra_window, text=momento_inercia_Vetor[4])
        label_momentoinercia_5.place(x=450, y=190)

        label_momentoinercia_6 = Label(barra_window, text=momento_inercia_Vetor[5])
        label_momentoinercia_6.place(x=450, y=220)

        label_momentoinercia_7 = Label(barra_window, text=momento_inercia_Vetor[6])
        label_momentoinercia_7.place(x=450, y=250)

        label_momentoinercia_8 = Label(barra_window, text=momento_inercia_Vetor[7])
        label_momentoinercia_8.place(x=450, y=280)

        label_momentoinercia_9 = Label(barra_window, text=momento_inercia_Vetor[8])
        label_momentoinercia_9.place(x=450, y=310)

        barra_1_vetor_global = barra_1_vetor
        barra_2_vetor_global = barra_2_vetor
        barra_3_vetor_global = barra_3_vetor
        barra_4_vetor_global = barra_4_vetor
        barra_5_vetor_global = barra_5_vetor
        barra_6_vetor_global = barra_6_vetor
        barra_7_vetor_global = barra_7_vetor
        barra_8_vetor_global = barra_8_vetor
        barra_9_vetor_global = barra_9_vetor

    botao_barra_salvar = Button(barra_window, text="SALVAR", width=8, height=2, command=update_barra)
    botao_barra_salvar.place(x=360, y=345)
    barra_window.mainloop()

def retornar_barra_1():
    return barra_1_vetor_global

def retornar_barra_2():
    return barra_2_vetor_global

def retornar_barra_3():
    return barra_3_vetor_global

def retornar_barra_4():
    return barra_4_vetor_global

def retornar_barra_5():
    return barra_5_vetor_global

def retornar_barra_6():
    return barra_6_vetor_global

def retornar_barra_7():
    return barra_7_vetor_global

def retornar_barra_8():
    return barra_8_vetor_global

def retornar_barra_9():
    return barra_9_vetor_global


