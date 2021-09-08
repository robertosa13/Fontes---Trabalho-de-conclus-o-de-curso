from tkinter import *

import tkinter
from tkinter.ttk import Combobox
import tkinter as tk

global carganodal_fx_vetor_global
global carganodal_fy_vetor_global
global carganodal_mz_vetor_global

global cargadistribuida_qx_vetor_global
global cargadistribuida_qy_vetor_global


def carregamentos():
    carregamentos_window = Tk()
    carregamentos_window.title('Carregamentos')
    carregamentos_window.iconbitmap('imagens/engenharia.ico')
    carregamentos_window.geometry("1366x768")

    lb_resistencias = LabelFrame(carregamentos_window, text="Dados de Cargas Nodais       "
                                                            "                          "
                                                            "Dados de Cargas  Distribuídas ", borderwidth=1, relief="solid")
    lb_resistencias.place(x=2, y=5, width=620, height=385)


    def center_window(w=1000, h=1000):
        # get screen width and height
        ws = carregamentos_window.winfo_screenwidth()
        hs = carregamentos_window.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        carregamentos_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    center_window(630, 400)
    carregamentos_window.resizable(0, 0)

    #label_carregamento_nodais = Label(carregamentos_window, text="Dados de Cargas Nodais em Nós", font=44)
    #label_carregamento_nodais.place(x=10, y=10)

    lb_no = Label(carregamentos_window, text="Nó")
    lb_no.place(x=5, y=35)
    lb_no_1 = Label(carregamentos_window, text="1")
    lb_no_1.place(x=10, y=65)
    lb_no_2 = Label(carregamentos_window, text="2")
    lb_no_2.place(x=10, y=95)
    lb_no_3 = Label(carregamentos_window, text="3")
    lb_no_3.place(x=10, y=125)
    lb_no_4 = Label(carregamentos_window, text="4")
    lb_no_4.place(x=10, y=155)
    lb_no_5 = Label(carregamentos_window, text="5")
    lb_no_5.place(x=10, y=185)
    lb_no_6 = Label(carregamentos_window, text="6")
    lb_no_6.place(x=10, y=215)
    lb_no_7 = Label(carregamentos_window, text="7")
    lb_no_7.place(x=10, y=245)
    lb_no_8 = Label(carregamentos_window, text="8")
    lb_no_8.place(x=10, y=275)
    lb_no_9 = Label(carregamentos_window, text="9")
    lb_no_9.place(x=10, y=305)
    lb_no_10 = Label(carregamentos_window, text="10")
    lb_no_10.place(x=10, y=335)

    lb_fx = Label(carregamentos_window, text="Fx (kN)")
    lb_fx.place(x=45, y=35)
    lb_fy = Label(carregamentos_window, text="Fy (kN)")
    lb_fy.place(x=110, y=35)
    lb_mz = Label(carregamentos_window, text="Mz (kN.m)")
    lb_mz.place(x=180, y=35)

    no_1_fx = Entry(carregamentos_window)
    no_1_fx.place(x=50, y=65, height=20, width=40)

    no_2_fx = Entry(carregamentos_window)
    no_2_fx.place(x=50, y=95, height=20, width=40)

    no_3_fx = Entry(carregamentos_window)
    no_3_fx.place(x=50, y=125, height=20, width=40)

    no_4_fx = Entry(carregamentos_window)
    no_4_fx.place(x=50, y=155, height=20, width=40)

    no_5_fx = Entry(carregamentos_window)
    no_5_fx.place(x=50, y=185, height=20, width=40)

    no_6_fx = Entry(carregamentos_window)
    no_6_fx.place(x=50, y=215, height=20, width=40)

    no_7_fx = Entry(carregamentos_window)
    no_7_fx.place(x=50, y=245, height=20, width=40)

    no_8_fx = Entry(carregamentos_window)
    no_8_fx.place(x=50, y=275, height=20, width=40)

    no_9_fx = Entry(carregamentos_window)
    no_9_fx.place(x=50, y=305, height=20, width=40)

    no_10_fx = Entry(carregamentos_window)
    no_10_fx.place(x=50, y=335, height=20, width=40)

    no_1_fy = Entry(carregamentos_window)
    no_1_fy.place(x=115, y=65, height=20, width=40)

    no_2_fy = Entry(carregamentos_window)
    no_2_fy.place(x=115, y=95, height=20, width=40)

    no_3_fy = Entry(carregamentos_window)
    no_3_fy.place(x=115, y=125, height=20, width=40)

    no_4_fy = Entry(carregamentos_window)
    no_4_fy.place(x=115, y=155, height=20, width=40)

    no_5_fy = Entry(carregamentos_window)
    no_5_fy.place(x=115, y=185, height=20, width=40)

    no_6_fy = Entry(carregamentos_window)
    no_6_fy.place(x=115, y=215, height=20, width=40)

    no_7_fy = Entry(carregamentos_window)
    no_7_fy.place(x=115, y=245, height=20, width=40)

    no_8_fy = Entry(carregamentos_window)
    no_8_fy.place(x=115, y=275, height=20, width=40)

    no_9_fy = Entry(carregamentos_window)
    no_9_fy.place(x=115, y=305, height=20, width=40)

    no_10_fy = Entry(carregamentos_window)
    no_10_fy.place(x=115, y=335, height=20, width=40)

    no_1_mz = Entry(carregamentos_window)
    no_1_mz.place(x=185, y=65, height=20, width=40)

    no_2_mz = Entry(carregamentos_window)
    no_2_mz.place(x=185, y=95, height=20, width=40)

    no_3_mz = Entry(carregamentos_window)
    no_3_mz.place(x=185, y=125, height=20, width=40)

    no_4_mz = Entry(carregamentos_window)
    no_4_mz.place(x=185, y=155, height=20, width=40)

    no_5_mz = Entry(carregamentos_window)
    no_5_mz.place(x=185, y=185, height=20, width=40)

    no_6_mz = Entry(carregamentos_window)
    no_6_mz.place(x=185, y=215, height=20, width=40)

    no_7_mz = Entry(carregamentos_window)
    no_7_mz.place(x=185, y=245, height=20, width=40)

    no_8_mz = Entry(carregamentos_window)
    no_8_mz.place(x=185, y=275, height=20, width=40)

    no_9_mz = Entry(carregamentos_window)
    no_9_mz.place(x=185, y=305, height=20, width=40)

    no_10_mz = Entry(carregamentos_window)
    no_10_mz.place(x=185, y=335, height=20, width=40)

    no_1_fx.insert(END, "0")
    no_2_fx.insert(END, "0")
    no_3_fx.insert(END, "0")
    no_4_fx.insert(END, "0")
    no_5_fx.insert(END, "0")
    no_6_fx.insert(END, "0")
    no_7_fx.insert(END, "0")
    no_8_fx.insert(END, "0")
    no_9_fx.insert(END, "0")
    no_10_fx.insert(END, "0")

    no_1_fy.insert(END, "0")
    no_2_fy.insert(END, "0")
    no_3_fy.insert(END, "0")
    no_4_fy.insert(END, "0")
    no_5_fy.insert(END, "0")
    no_6_fy.insert(END, "0")
    no_7_fy.insert(END, "0")
    no_8_fy.insert(END, "0")
    no_9_fy.insert(END, "0")
    no_10_fy.insert(END, "0")

    no_1_mz.insert(END, "0")
    no_2_mz.insert(END, "0")
    no_3_mz.insert(END, "0")
    no_4_mz.insert(END, "0")
    no_5_mz.insert(END, "0")
    no_6_mz.insert(END, "0")
    no_7_mz.insert(END, "0")
    no_8_mz.insert(END, "0")
    no_9_mz.insert(END, "0")
    no_10_mz.insert(END, "0")

   # label_carregamento_distribuidos = Label(carregamentos_window, text="Dados de Carregamentos Uniformemente Distribuídos em Barras",font=44)
   # label_carregamento_distribuidos.place(x=280, y=10)

    lb_barra = Label(carregamentos_window, text="Barra")
    lb_barra.place(x=280, y=35)

    lb_qx = Label(carregamentos_window, text="Qx (kN/m)")
    lb_qx.place(x=350, y=35)

    lb_qy = Label(carregamentos_window, text="Qy (kN/m)")
    lb_qy.place(x=450, y=35)

    lb_direcao = Label(carregamentos_window, text="Direção")
    lb_direcao.place(x=550, y=35)

    lb_direcao1 = Label(carregamentos_window, text="Global")
    lb_direcao1.place(x=552, y=65)

    lb_direcao2 = Label(carregamentos_window, text="Global")
    lb_direcao2.place(x=552, y=95)

    lb_direcao3 = Label(carregamentos_window, text="Global")
    lb_direcao3.place(x=552, y=125)

    lb_direcao4 = Label(carregamentos_window, text="Global")
    lb_direcao4.place(x=552, y=155)

    lb_direcao5 = Label(carregamentos_window, text="Global")
    lb_direcao5.place(x=552, y=185)

    lb_direcao6 = Label(carregamentos_window, text="Global")
    lb_direcao6.place(x=552, y=215)

    lb_direcao7 = Label(carregamentos_window, text="Global")
    lb_direcao7.place(x=552, y=245)

    lb_direcao8 = Label(carregamentos_window, text="Global")
    lb_direcao8.place(x=552, y=275)

    lb_direcao9 = Label(carregamentos_window, text="Global")
    lb_direcao9.place(x=552, y=305)

    lb_barra_1 = Label(carregamentos_window, text="1")
    lb_barra_1.place(x=285, y=65)
    lb_barra_2 = Label(carregamentos_window, text="2")
    lb_barra_2.place(x=285, y=95)
    lb_barra_3 = Label(carregamentos_window, text="3")
    lb_barra_3.place(x=285, y=125)
    lb_barra_4 = Label(carregamentos_window, text="4")
    lb_barra_4.place(x=285, y=155)
    lb_barra_5 = Label(carregamentos_window, text="5")
    lb_barra_5.place(x=285, y=185)
    lb_barra_6 = Label(carregamentos_window, text="6")
    lb_barra_6.place(x=285, y=215)
    lb_barra_7 = Label(carregamentos_window, text="7")
    lb_barra_7.place(x=285, y=245)
    lb_barra_8 = Label(carregamentos_window, text="8")
    lb_barra_8.place(x=285, y=275)
    lb_barra_9 = Label(carregamentos_window, text="9")
    lb_barra_9.place(x=285, y=305)

    no_1_qx = Entry(carregamentos_window)
    no_1_qx.place(x=360, y=65, height=20, width=55)

    no_2_qx = Entry(carregamentos_window)
    no_2_qx.place(x=360, y=95, height=20, width=55)

    no_3_qx = Entry(carregamentos_window)
    no_3_qx.place(x=360, y=125, height=20, width=55)

    no_4_qx = Entry(carregamentos_window)
    no_4_qx.place(x=360, y=155, height=20, width=55)

    no_5_qx = Entry(carregamentos_window)
    no_5_qx.place(x=360, y=185, height=20, width=55)

    no_6_qx = Entry(carregamentos_window)
    no_6_qx.place(x=360, y=215, height=20, width=55)

    no_7_qx = Entry(carregamentos_window)
    no_7_qx.place(x=360, y=245, height=20, width=55)

    no_8_qx = Entry(carregamentos_window)
    no_8_qx.place(x=360, y=275, height=20, width=55)

    no_9_qx = Entry(carregamentos_window)
    no_9_qx.place(x=360, y=305, height=20, width=55)

    no_1_qy = Entry(carregamentos_window)
    no_1_qy.place(x=460, y=65, height=20, width=55)

    no_2_qy = Entry(carregamentos_window)
    no_2_qy.place(x=460, y=95, height=20, width=55)

    no_3_qy = Entry(carregamentos_window)
    no_3_qy.place(x=460, y=125, height=20, width=55)

    no_4_qy = Entry(carregamentos_window)
    no_4_qy.place(x=460, y=155, height=20, width=55)

    no_5_qy = Entry(carregamentos_window)
    no_5_qy.place(x=460, y=185, height=20, width=55)

    no_6_qy = Entry(carregamentos_window)
    no_6_qy.place(x=460, y=215, height=20, width=55)

    no_7_qy = Entry(carregamentos_window)
    no_7_qy.place(x=460, y=245, height=20, width=55)

    no_8_qy = Entry(carregamentos_window)
    no_8_qy.place(x=460, y=275, height=20, width=55)

    no_9_qy = Entry(carregamentos_window)
    no_9_qy.place(x=460, y=305, height=20, width=55)

    no_1_qx.insert(END, "0")
    no_2_qx.insert(END, "0")
    no_3_qx.insert(END, "0")
    no_4_qx.insert(END, "0")
    no_5_qx.insert(END, "0")
    no_6_qx.insert(END, "0")
    no_7_qx.insert(END, "0")
    no_8_qx.insert(END, "0")
    no_9_qx.insert(END, "0")

    no_1_qy.insert(END, "0")
    no_2_qy.insert(END, "0")
    no_3_qy.insert(END, "0")
    no_4_qy.insert(END, "0")
    no_5_qy.insert(END, "0")
    no_6_qy.insert(END, "0")
    no_7_qy.insert(END, "0")
    no_8_qy.insert(END, "0")
    no_9_qy.insert(END, "0")

    def carregamentos_update():
        carganodal_fx_vetor = []
        carganodal_fy_vetor = []
        carganodal_mz_vetor = []

        cargadistribuida_qx_vetor = []
        cargadistribuida_qy_vetor = []

        global carganodal_fx_vetor_global
        global carganodal_fy_vetor_global
        global carganodal_mz_vetor_global

        global cargadistribuida_qx_vetor_global
        global cargadistribuida_qy_vetor_global

        carganodal_fx_vetor = [float(no_1_fx.get()), float(no_2_fx.get()), float(no_3_fx.get()),
                               float(no_4_fx.get()),
                               float(no_5_fx.get()), float(no_6_fx.get()),
                               float(no_7_fx.get()), float(no_8_fx.get()), float(no_9_fx.get()),
                               float(no_10_fx.get())]

        carganodal_fy_vetor = [float(no_1_fy.get()), float(no_2_fy.get()), float(no_3_fy.get()),
                               float(no_4_fy.get()),
                               float(no_5_fy.get()), float(no_6_fy.get()),
                               float(no_7_fy.get()), float(no_8_fy.get()), float(no_9_fy.get()),
                               float(no_10_fy.get())]

        carganodal_mz_vetor = [float(no_1_mz.get()), float(no_2_mz.get()), float(no_3_mz.get()),
                               float(no_4_mz.get()),
                               float(no_5_mz.get()), float(no_6_mz.get()),
                               float(no_7_mz.get()), float(no_8_mz.get()), float(no_9_mz.get()),
                               float(no_10_mz.get())]

        cargadistribuida_qx_vetor = [float(no_1_qx.get()), float(no_2_qx.get()), float(no_3_qx.get()),
                                     float(no_4_qx.get()),
                                     float(no_5_qx.get()), float(no_6_qx.get()),
                                     float(no_7_qx.get()), float(no_8_qx.get()), float(no_9_qx.get())]

        cargadistribuida_qy_vetor = [float(no_1_qy.get()), float(no_2_qy.get()), float(no_3_qy.get()),
                                     float(no_4_qy.get()),
                                     float(no_5_qy.get()), float(no_6_qy.get()),
                                     float(no_7_qy.get()), float(no_8_qy.get()), float(no_9_qy.get())]

        carganodal_fx_vetor_global = carganodal_fx_vetor
        carganodal_fy_vetor_global = carganodal_fy_vetor
        carganodal_mz_vetor_global = carganodal_mz_vetor

        cargadistribuida_qx_vetor_global = cargadistribuida_qx_vetor
        cargadistribuida_qy_vetor_global = cargadistribuida_qy_vetor
        print(carganodal_fx_vetor_global)
        print(carganodal_fy_vetor_global)
        print(carganodal_mz_vetor_global)
        print(cargadistribuida_qx_vetor_global)
        print(cargadistribuida_qy_vetor_global)


    salvar = Button(carregamentos_window, command=carregamentos_update, text="SALVAR", width = 8, height = 2)
    salvar.place(x=540, y=343)

    carregamentos_window.mainloop()


def fx_vetor():
    return carganodal_fx_vetor_global

def fy_vetor():
    return carganodal_fy_vetor_global

def mz_vetor():
    return  carganodal_mz_vetor_global

def qx_vetor():
    return cargadistribuida_qx_vetor_global

def qy_vetor():
    return cargadistribuida_qy_vetor_global
