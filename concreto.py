import tkinter
from tkinter.ttk import Combobox
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
import math

import parametrosConcreto


def concreto():

        concreto_window = tk.Tk()
        concreto_window.title('Concreto')
        concreto_window.iconbitmap('imagens/engenharia.ico')  # icone
        #concreto_window.geometry("1200x650")

        def center_window(w=1200, h=300):
            # get screen width and height
            ws = concreto_window.winfo_screenwidth()
            hs = concreto_window.winfo_screenheight()
            # calculate position x, y
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            concreto_window.geometry('%dx%d+%d+%d' % (w, h, x, y))


        center_window(1200,650)
        concreto_window.resizable(0, 0)


        lb_resistencias = LabelFrame(concreto_window, text="  Resistências do concreto ",  borderwidth = 1, relief ="solid" )
        lb_resistencias.place( x = 2, y = 25, width = 535 , height = 245)


        lb_fckadotado = Label(concreto_window,   text="Resistência característica à compressão  F'ck (mPa):")
        lb_fckadotado.place(x=5, y=55)

        lb_fctm = Label(concreto_window,         text="Resistência à tração média F'ctm (mPa):")
        lb_fctm.place(x=5, y=95)

        lb_fctkinf = Label(concreto_window,      text="Resistência característica à tração inferior F'ctk inf (mPa):")
        lb_fctkinf.place(x=5, y=135)

        lb_fctksup = Label(concreto_window,      text="Resistência característica à tração superior F'ctk sup (mPa):")
        lb_fctksup.place(x=5, y=175)


        def resistencias_update():

            fckadotado_global = parametrosConcreto.retornar_fck()
            tipo_aco_global = parametrosConcreto.retornar_tipo_aco()
            gamac_global = parametrosConcreto.retornar_gamac()
            gamay_global = parametrosConcreto.retornar_gamay()
            caa_global = parametrosConcreto.retornar_caa()
            fctm = parametrosConcreto.retornar_fctm()
            fctkinf = parametrosConcreto.retornar_fctkinf()
            fctksup = parametrosConcreto.retornar_fctksup()


            lb_fckadotado_valor = Label(concreto_window,text= str(fckadotado_global))
            lb_fckadotado_valor.place(x=470, y=55)
            lb_fckadotado_valor.update()

            lb_fctm_valor = Label(concreto_window, text= str(fctm))
            lb_fctm_valor.place(x=470, y=95)
            lb_fctm_valor.update()

            lb_fctkinf_valor = Label(concreto_window, text= str(fctkinf))
            lb_fctkinf_valor.place(x=470, y=135)
            lb_fctkinf_valor.update()

            lb_fctksup = Label(concreto_window, text= str(fctksup))
            lb_fctksup.place(x=470, y=175)
            lb_fctksup.update()

            lb_fckadotado.update()
            lb_fctm.update()
            lb_fctkinf.update()
            lb_fctksup.update()

        salvarresistencias = Button(concreto_window, command= resistencias_update, text="Calcular", width=10, height=2)
        salvarresistencias.place(x=450, y=220)

        lb_modulo_elasticidade = LabelFrame(concreto_window, text= "Módulo de Elasticidade",  borderwidth=1,relief="solid")
        lb_modulo_elasticidade.place(x=2, y=295, width=535, height=285)

        agregado_concreto = ["Basalto e diabásio: αe = 1.2",
                             "Granito e gnaisse: αe = 1.0",
                             "Calcário: αe = 0.9",
                             "Arenito: αe = 0.7"]

        lb_agregadograudo = Label(concreto_window, text="Escolha o agregado graúdo: ")
        lb_agregadograudo.place(x=5, y=335)

        combo_agregado_concreto = Combobox(concreto_window, values=agregado_concreto, width=30)
        combo_agregado_concreto.place(x=220, y=335)

        lb_modulo_tang_inicial = Label(concreto_window, text="Módulo de elasticidade tangente inicial do concreto Eci (mPa): ")
        lb_modulo_tang_inicial.place(x=5, y=385)

        lb_alfai = Label(concreto_window,text="Parâmetro αi: ")
        lb_alfai.place(x=5, y=435)

        lb_modulo_long_comp = Label(concreto_window, text="Módulo de elasticidade secante do concreto Ecs (mPa): ")
        lb_modulo_long_comp.place(x=5, y= 485)



        def elasticidade_update():

            fckadotado_global = parametrosConcreto.retornar_fck()
            tipo_aco_global = parametrosConcreto.retornar_tipo_aco()
            gamac_global = parametrosConcreto.retornar_gamac()
            gamay_global = parametrosConcreto.retornar_gamay()
            caa_global = parametrosConcreto.retornar_caa()
            fctm = parametrosConcreto.retornar_fctm()
            fctkinf = parametrosConcreto.retornar_fctkinf()
            fctksup = parametrosConcreto.retornar_fctksup()


            local_alfae = combo_agregado_concreto.get()

            if local_alfae == 'Basalto e diabásio: αe = 1.2':
                alfae = 1.2

            if local_alfae == 'Granito e gnaisse: αe = 1.0':
                alfae = 1.0

            if local_alfae == 'Calcário: αe = 0.9':
                alfae = 0.9

            if local_alfae == 'Arenito: αe = 0.7':
                alfae = 0.7

            print("valor do alfae é :")
            print(alfae)

            # cálculo do ECI

            if fckadotado_global <= 50:
                eci = round(alfae*5600*fckadotado_global**(1/2), 2)
                print("classe até  C50 eci:")
                print(eci)
            else:
                eci = round(21500*alfae*((fckadotado_global/10)+1.25)**(1/3), 2)
                print("classe maior que C50 eci:")
                print(eci)


            #conforme o chust Ecs <= ECI, portanto alfaI não pode ser maior que 1 mesmo que pela fórmula seja permitido, por isso colocado a condicional
            alfai = round(0.8+0.2*(fckadotado_global/80),5)
            if alfai > 1:
                alfai = 1


            ecs = round(alfai*eci,2)

            print("alfai:")
            print(alfai)
            print("ecs")
            print(ecs)

            lb_modulo_tang_inicial_valor = Label(concreto_window, text= str("%.2f" % eci))
            lb_modulo_tang_inicial_valor.place(x=450, y=385)
            lb_modulo_tang_inicial_valor.update()

            lb_alfai_valor = Label(concreto_window, text=str("%.3f" % alfai))
            lb_alfai_valor.place(x=110, y=435)
            lb_alfai_valor.update()

            lb_modulo_long_comp = Label(concreto_window,text= str("%.2f"% ecs))
            lb_modulo_long_comp.place(x=450, y=485)
            lb_modulo_long_comp.update()





        salvarelasticidade = Button(concreto_window, command=elasticidade_update, text="Calcular", width=10, height=2)
        salvarelasticidade.place(x=450, y=530)

        def grafico_tensao():

            fckadotado_global = parametrosConcreto.retornar_fck()
            tipo_aco_global = parametrosConcreto.retornar_tipo_aco()
            gamac_global = parametrosConcreto.retornar_gamac()
            gamay_global = parametrosConcreto.retornar_gamay()
            caa_global = parametrosConcreto.retornar_caa()
            fctm = parametrosConcreto.retornar_fctm()
            fctkinf = parametrosConcreto.retornar_fctkinf()
            fctksup = parametrosConcreto.retornar_fctksup()

            import matplotlib
            import matplotlib.pyplot as plt
            import numpy as np


            # Data for plotting

            deformacao = np.arange(0.0, 2, 0.001)

            if fckadotado_global <= 50:
                n = 2
            else:
                n = 1.4 + 23.4*((90-fckadotado_global)/100)**4

            fcd = fckadotado_global/gamac_global


            if fckadotado_global <= 50:
                ec2 = 0.002
                ecu = 0.0035
            else:
                ec2 = 0.002 + (0.085/1000)*(fckadotado_global-50)**0.53
                ecu = 0.0026 + 0.035*((90-fckadotado_global)/100)**4

            fcd = fckadotado_global/gamac_global



            trechoinferior = 0.85 * fcd * (1 - (1 - (deformacao/1000)/ ec2) ** n)
            trechosuperior = fckadotado_global*(1-(1-(deformacao/1000)/ec2)**n)



            fig1 = Figure(figsize=(1, 1), dpi=100)
            fig1, ax1 = plt.subplots()
            ax1.plot(deformacao, trechoinferior)
            ax1.plot(deformacao, trechosuperior)



            ax1.set(xlabel='deformação (ε ‰)', ylabel='Tensão (σ mPa)', title='Gráfico tensão-deformação do concreto')
            ax1.grid()

            canvas = FigureCanvasTkAgg(fig1, master=concreto_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.RIGHT)

            toolbar = NavigationToolbar2Tk(canvas, concreto_window)
            toolbar.update()
            canvas.get_tk_widget().pack(side = tkinter.RIGHT)

            fig1.savefig("diagrama tensão-deformação.png")


        janelagrafico = Button(concreto_window, command=grafico_tensao, text="Gerar gráfico", width=10, height=2)
        janelagrafico.place(x=750, y=600)




        concreto_window.mainloop()