from tkinter.ttk import Combobox
from tkinter import *
import parametrosConcreto
import math




def ancoragem():

        ancoragem_window = Tk()
        ancoragem_window.title('Ancoragem')
        ancoragem_window.iconbitmap('imagens/engenharia.ico')  # icone
        ancoragem_window.geometry("1366x768")



        def center_window(w=1000, h=1000):
            # get screen width and height
            ws = ancoragem_window.winfo_screenwidth()
            hs = ancoragem_window.winfo_screenheight()
            # calculate position x, y
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            ancoragem_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        center_window(600, 550)

        lb_ancoragem = LabelFrame(ancoragem_window, text="Ancoragem de armadura ", font=10, borderwidth=1,                                         relief="solid")
        lb_ancoragem.place(x=2, y=12, width=594, height=535)

        lb_ancoragem_fctd = Label(ancoragem_window, text="Resistência à tração direta do concreto - Fctd (mPa):", font=4)
        lb_ancoragem_fctd.place(x=5, y=40)

        lb_ancoragem_num = Label(ancoragem_window,   text="Parâmetro η1 (Tipo de barra):", font=4)
        lb_ancoragem_num.place(x=5, y = 75)

        lb_ancoragem_ndois = Label(ancoragem_window, text="Parâmetro η2 (Região de aderência) :", font=4)
        lb_ancoragem_ndois.place(x=5, y=110)

        lb_ancoragem_ntres = Label(ancoragem_window, text="Parâmetro η3 (Diâmetro de barra):", font=4)
        lb_ancoragem_ntres.place(x=5, y=145)

        lb_ancoragem_fctd = Label(ancoragem_window, text="Resistência de aderência mo concreto - Fbd (mPa):", font=4)
        lb_ancoragem_fctd.place(x=5, y=180)

        lb_ancoragem_alfa = Label(ancoragem_window, text="Parâmetro α :", font=4)
        lb_ancoragem_alfa.place(x=5, y=215)

        lb_ancoragem_bitola = Label(ancoragem_window, text="Bitola comercial ⌀ :", font=4)
        lb_ancoragem_bitola.place(x=5, y=250)

        lb_ancoragem_qtd_barras = Label(ancoragem_window, text="Quantidade de  barras:", font=4)
        lb_ancoragem_qtd_barras.place(x=5, y=285)

        lb_ancoragem_as_efetiva = Label(ancoragem_window, text="Área de aço efetiva - (cm²):", font=4)
        lb_ancoragem_as_efetiva.place(x=5, y=320)

        lb_ancoragem_as_calculada = Label(ancoragem_window, text="Área de aço calculada - (cm²):", font=4)
        lb_ancoragem_as_calculada.place(x=5, y=355)

        lb_ancoragem_lb = Label(ancoragem_window, text="Comprimento básico de ancoragem - Lb(cm):", font=4)
        lb_ancoragem_lb.place(x=5, y=390)

        lb_ancoragem_lbmin = Label(ancoragem_window, text="Comprimento básico de ancoragem mínimo - Lb min(cm):", font=4)
        lb_ancoragem_lbmin.place(x=5, y=425)

        lb_ancoragem_lbnec = Label(ancoragem_window, text="Comprimento básico de ancoragem necessário - Lb nec(cm):", font=4)
        lb_ancoragem_lbnec.place(x=5, y=460)



        ancoragem_num = ["η1 =  1.00 Barras lisas      CA-25",
                         "η1 =  1.40 Barras entalhadas CA-60",
                         "η1 =  2.25 Barras entalhadas CA-50"]

        ancoragem_ndois = ["η2 = 1.00 Boa aderência",
                          "η2 = 1.40  Má aderência"]

        ancoragem_ntres = ["η3 = 1.00 ⌀ <= 32.0 mm"]

        ancoragem_n_alfa = ["α = 1.00 Barras sem gancho",
                            "α = 0.70 Barras com gancho"]

        ancoragem_bitolas_comerciais = ["⌀5.0 mm", "⌀6.3 mm", "⌀8.0 mm", "⌀10.0 mm", "⌀12.5 mm", "⌀16.0 mm", "⌀20.0 mm","⌀25.0 mm", "⌀32.0 mm"]

        qtd_barras = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]



        entry_as_calculada = Entry(ancoragem_window)
        entry_as_calculada.place(x=540, y=355, height=20, width=50)




        combo_ancoragem_num = Combobox(ancoragem_window, values=ancoragem_num, width=33)
        combo_ancoragem_num.place(x=370, y=75)

        combo_ancoragem_ndois = Combobox(ancoragem_window, values=ancoragem_ndois, width=33)
        combo_ancoragem_ndois.place(x=370, y = 110)

        combo_ancoragem_ntres = Combobox(ancoragem_window, values=ancoragem_ntres, width=33)
        combo_ancoragem_ntres.place(x=370, y= 145)

        combo_ancoragem_nalfa = Combobox(ancoragem_window, values=ancoragem_n_alfa, width=33)
        combo_ancoragem_nalfa.place(x=370, y=215)

        combo_ancoragem_bitola = Combobox(ancoragem_window, values=ancoragem_bitolas_comerciais, width=25)
        combo_ancoragem_bitola.place(x=370, y=250)

        combo_ancoragem_qtd_barras = Combobox(ancoragem_window, values=qtd_barras, width=25)
        combo_ancoragem_qtd_barras.place(x=370, y=285)



        def ancoragem_update():

            fckadotado_global = parametrosConcreto.retornar_fck()
            tipo_aco_global = parametrosConcreto.retornar_tipo_aco()
            gamac_global = parametrosConcreto.retornar_gamac()
            gamay_global = parametrosConcreto.retornar_gamay()
            caa_global = parametrosConcreto.retornar_caa()
            fctm = parametrosConcreto.retornar_fctm()
            fctkinf = parametrosConcreto.retornar_fctkinf()
            fctksup = parametrosConcreto.retornar_fctksup()

            global ancoragem_fctd
            global ancoragem_valor_num
            global ancoragem_valor_ndois
            global ancoragem_valor_ntres
            global ancoragem_fbd
            global ancoragem_alfa
            global ancoragem_bitola
            global ancoragem_qtd_barras
            global ancoragem_area_efetiva
            global ancoragem_area_calculada
            global ancoragem_lb
            global ancoragem_lbmin
            global ancoragem_lbnec

            ancoragem_fctd = (0.21 * (fckadotado_global ** (2 / 3))) / gamac_global


            lb_valor_ancoragem_fctd = Label(ancoragem_window, text="%.2f" % ancoragem_fctd,font=4)
            lb_valor_ancoragem_fctd.place(x=550, y=35)
            lb_valor_ancoragem_fctd.update()


            if combo_ancoragem_num.get() == "η1 =  1.00 Barras lisas      CA-25":
                ancoragem_valor_num = 1

            if combo_ancoragem_num.get() == "η1 =  1.40 Barras entalhadas CA-60":
                ancoragem_valor_num = 1.4

            if combo_ancoragem_num.get() == "η1 =  2.25 Barras entalhadas CA-50":
                ancoragem_valor_num = 2.25

            if combo_ancoragem_ndois.get() == "η2 = 1.00 Boa aderência":
                ancoragem_valor_ndois = 1

            if combo_ancoragem_ndois.get() == "η2 = 1.40  Má aderência":
                ancoragem_valor_ndois = 1.4

            if combo_ancoragem_ntres.get() == "η3 = 1.00 ⌀ <= 32.0 mm":
                ancoragem_valor_ntres = 1


            print("Num")
            print(ancoragem_valor_num)
            print("Ndois")
            print(ancoragem_valor_ndois)
            print("Ntres")
            print( ancoragem_valor_ntres)

            # formula para resistência de aderência
            ancoragem_fbd = ancoragem_valor_num*ancoragem_valor_ndois*ancoragem_valor_ntres*ancoragem_fctd # em mpa

            lb_valor_ancoragem_fbd = Label(ancoragem_window, text="%.2f" % ancoragem_fbd, font=4)
            lb_valor_ancoragem_fbd.place(x=550, y=180)
            lb_valor_ancoragem_fbd.update()

            if combo_ancoragem_bitola.get() == '⌀5.0 mm':
                ancoragem_bitola = 5 / 10  # inseri bitola em cm

            if combo_ancoragem_bitola.get() == '⌀6.3 mm':
                ancoragem_bitola = 6.3 / 10  # inseri bitola em cm

            if combo_ancoragem_bitola.get() == '⌀8.0 mm':
                ancoragem_bitola = 8 / 10  # inseri bitola em cm

            if combo_ancoragem_bitola.get() == '⌀10.0 mm':
                ancoragem_bitola = 10 / 10  # inseri bitola em cm

            if combo_ancoragem_bitola.get() == '⌀12.5 mm':
                ancoragem_bitola = 12.5 / 10  # inseri bitola em cm

            if combo_ancoragem_bitola.get() == '⌀16.0 mm':
                ancoragem_bitola = 16 / 10  # inseri bitola em cm

            if combo_ancoragem_bitola.get() == '⌀20.0 mm':
                ancoragem_bitola = 20 / 10  # inseri bitola em cm

            if combo_ancoragem_bitola.get() == '⌀25.0 mm':
                ancoragem_bitola = 25 / 10  # inseri bitola em cm

            if combo_ancoragem_bitola.get() == '⌀32.0 mm':
                ancoragem_bitola = 32 / 10  # inseri bitola em cm

            print("Bitola")
            print(ancoragem_bitola)



            if combo_ancoragem_qtd_barras.get() == '1':
                ancoragem_qtd_barras = 1

            if combo_ancoragem_qtd_barras.get() == '2':
                ancoragem_qtd_barras = 2

            if combo_ancoragem_qtd_barras.get() == '3':
                ancoragem_qtd_barras = 3

            if combo_ancoragem_qtd_barras.get() == '4':
                ancoragem_qtd_barras = 4

            if combo_ancoragem_qtd_barras.get() == '5':
                ancoragem_qtd_barras = 5

            if combo_ancoragem_qtd_barras.get() == '6':
                ancoragem_qtd_barras = 6

            if combo_ancoragem_qtd_barras.get() == '7':
                ancoragem_qtd_barras = 7

            if combo_ancoragem_qtd_barras.get() == '8':
                ancoragem_qtd_barras = 8

            if combo_ancoragem_qtd_barras.get() == '9':
                ancoragem_qtd_barras = 9

            if combo_ancoragem_qtd_barras.get() == '10':
                ancoragem_qtd_barras = 10


            print("qtd de barras")
            print(ancoragem_qtd_barras)




            if combo_ancoragem_nalfa.get() == 'α = 1.00 Barras sem gancho':
                ancoragem_n_alfa = 1

            if combo_ancoragem_nalfa.get() == 'α = 0.70 Barras com gancho':
                ancoragem_n_alfa = 0.7

            print("Numero alfa ")
            print(ancoragem_n_alfa)


            #áreas de aço
            ancoragem_area_efetiva = ancoragem_qtd_barras*((math.pi*ancoragem_bitola**2)/4) # em cm²
            ancoragem_area_calculada = float(entry_as_calculada.get())
            print(ancoragem_area_calculada)


            lb_valor_ancoragem_as_efetiva = Label(ancoragem_window, text="%.2f" % ancoragem_area_efetiva, font=4)
            lb_valor_ancoragem_as_efetiva.place(x=550, y=320)
            lb_valor_ancoragem_as_efetiva.update()

            #calculo do lb - comprimento básico de ancoragem



            ancoragem_lb = (ancoragem_bitola/4)*(fyd_global/ancoragem_fbd) # em cm

            #verificação se atende o requisito da norma de ser menor que 25x a bitola

            if 25*ancoragem_bitola > ancoragem_lb:
                ancoragem_lb = 25*ancoragem_bitola

            print(ancoragem_lb)

            lb_valor_lb = Label(ancoragem_window, text="%.2f" % ancoragem_lb, font=4)
            lb_valor_lb.place(x=550, y=390)
            lb_valor_lb.update()

            #valor para o lb min . maior valor da lista

            lista_lbmin = [0.3*ancoragem_lb, 10*ancoragem_bitola, 10] # valores em cm

            ancoragem_lbmin = max(lista_lbmin)
            print("O comprimento mínimo de ancoragem lb min É")
            print(ancoragem_lbmin)

            # calculo do lb necessário

            ancoragem_lbnec = ancoragem_alfa*ancoragem_lb*(ancoragem_area_calculada/ancoragem_area_efetiva)

            if ancoragem_lbnec < ancoragem_lbmin:
                ancoragem_lbnec = ancoragem_lbmin

            print("valor da ancoragem necessária é de :")
            print(ancoragem_lbnec)

            lb_valor_lbmin = Label(ancoragem_window, text="%.2f" % ancoragem_lbmin, font=4)
            lb_valor_lbmin.place(x=550, y=425)
            lb_valor_lbmin.update()

            lb_valor_lbnec = Label(ancoragem_window, text="%.2f" % ancoragem_lbnec, font=4)
            lb_valor_lbnec.place(x=545, y=460)
            lb_valor_lbnec.update()





        salvar = Button(ancoragem_window, command=ancoragem_update, text="SALVAR", width=10, height=2)
        salvar.place(x=510, y=500)


        ancoragem_window.mainloop()
