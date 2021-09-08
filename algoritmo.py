# Created by Roberto Sá on 22/02/2021
# Email: robertosapaiva@hotmail.com
# Criação do algoritmo de processamento estrutural para pórticos planos
# Celular: (81) 99525-2794
# Aluno: Roberto Sá Barreto Paiva da Cunha
# Orientador: Prof. Dr. Sérgio Priori Jovino Marques Filho
#-----------------------------------------------------------------------------------------------------------------------

from tkinter.ttk import Combobox
from tkinter import *
import math
import matplotlib.pyplot as plt
import numpy as np

# importação dos arquivos que permitem a entrada de dados do pórtico plano
import parametro
import barras
import cargas

def processamento():



    # passo 1:
    # criação dos vetores para armazenar os dados de entrada e formatá-los para o algoritmo
    # dados do arquivo de parametros

    nodal_x = parametro.retornar_coord_x()       #coordenadas iniciais x
    nodal_y = parametro.retornar_coord_y()       #coordenadas iniciais y
    desloc_x = parametro.retornar_comb_x()      #restrição de deslocabilidade na direção x
    desloc_y = parametro.retornar_comb_y()      #restrição de deslocabilidade na direção y
    desloc_z = parametro.retornar_comb_z()      #restrição de deslocabilidade na direção z

    # dados do arquivo de barras
    # 0 arquivo de barras gera um array para posição da barra com a seguinte ordem:
    # (nó inicial 0, nó final 1 , altura útil 2 , bf 3, inércia 4, elasticidade 5)

    # alocação de até 9 barras iniciais e posterior segmentação em N subdivisões, conforme discretização do
    # usuário do código
    barra_1 = barras.retornar_barra_1()
    barra_2 = barras.retornar_barra_2()
    barra_3 = barras.retornar_barra_3()
    barra_4 = barras.retornar_barra_4()
    barra_5 = barras.retornar_barra_5()
    barra_6 = barras.retornar_barra_6()
    barra_7 = barras.retornar_barra_7()
    barra_8 = barras.retornar_barra_8()
    barra_9 = barras.retornar_barra_9()


    #array bidimensional de conectividade
    conectividade = [           [int(barra_1[0]), int(barra_1[1])],
                                [int(barra_2[0]), int(barra_2[1])],
                                [int(barra_3[0]), int(barra_3[1])],
                                [int(barra_4[0]), int(barra_4[1])],
                                [int(barra_5[0]), int(barra_5[1])],
                                [int(barra_6[0]), int(barra_6[1])],
                                [int(barra_7[0]), int(barra_7[1])],
                                [int(barra_8[0]), int(barra_8[1])],
                                [int(barra_9[0]), int(barra_9[1])]
                        ]
    #criação do vetor de área, inercia
    # e módulo de elasticidade (cada barra será armazenado em um espaço do vetor)
    a =    [float(barra_1[2]) * float(barra_1[3]),
            float(barra_2[2]) * float(barra_2[3]),
            float(barra_3[2]) * float(barra_3[3]),
            float(barra_4[2]) * float(barra_4[3]),
            float(barra_5[2]) * float(barra_5[3]),
            float(barra_6[2]) * float(barra_6[3]),
            float(barra_7[2]) * float(barra_7[3]),
            float(barra_8[2]) * float(barra_8[3]),
            float(barra_9[2]) * float(barra_9[3])
            ]  # considerando uma viga retangular de concreto armado - área em m²

    i =   [float(barra_1[4]),
           float(barra_2[4]),
           float(barra_3[4]),
           float(barra_4[4]),
           float(barra_5[4]),
           float(barra_6[4]),
           float(barra_7[4]),
           float(barra_8[4]),
           float(barra_9[4])
               ] #  considerando a inercia para uma seção transversal retangular de concreto m^4

    e =     [float(barra_1[5]),
             float(barra_2[5]),
             float(barra_3[5]),
             float(barra_4[5]),
             float(barra_5[5]),
             float(barra_6[5]),
             float(barra_7[5]),
             float(barra_8[5]),
             float(barra_9[5])
             ]  #  considerando a elasticidade constante ao longo de uma barra

    # dados do arquivo de cargas
    fx = cargas.fx_vetor()  #cargas pontuais na direção x  varia de 0-10
    fy = cargas.fy_vetor()  #cargas pontuais na direção y  varia de 0-10
    mz = cargas.mz_vetor()  # cargas momentos na direção z varia de 0-10

    qx = cargas.qx_vetor()  #cargas distribuidas na direção x varia de 0-9
    qy = cargas.qy_vetor()  #cargas distribuidas na direção y varia de 0-9


    #instrução de comando para determinar a quantidade de barras
    #no futuro, alterações para aumentar a discretização do modelo podem ser feitas aqui
    #primeiro contador sendo zerado pois barra_1 corresponde
    #a posição 0 no vetor indo até 8 (9barras)
    #variável "n" representa a quantidade de barras e será contabilizada se o elemento tiver
    #área diferente de  0

    count1 = 0
    n = 0
    theta = []  # cria theta
    l = [] # cria o vetor de comprimentos de barras

    while count1 <= 8:
        if a[count1] != 0:
            n = n + 1 # contador de barras pela área transversal diferente de zero
            # cálculo dos ângulos
            i_y = float(nodal_y[conectividade[count1][0]-1])
            f_y = float(nodal_y[conectividade[count1][1]-1])
            if f_y == i_y:
                theta.append(0)  # barra na horizontal

            if (f_y - i_y) > 0:
                theta.append(math.pi/2) # barra na vertical em 90 graus

            if (f_y - i_y) < 0:
                theta.append(3*math.pi/ 2)  # barra na vertical em 270 graus

            # cálculo dos comprimentos de barra
            # fórmula de GA --> raiz(deltax^2+deltay^2)
            l.append(math.sqrt((float(nodal_y[conectividade[count1][0]-1])-float(nodal_y[conectividade[count1][1]-1]))**2 + (float(nodal_x[conectividade[count1][0]-1])-float(nodal_x[conectividade[count1][1]-1]))**2))
            #comprimento em metros para cada barra selecionada
        count1 = count1 + 1

    qtd_barras = n # varíavel criada para armazenar a quantidade de barras encontradas em N


    # leitura dos graus de liberdade de cada nó
    #deslocamento em x
    #deslocamento em y
    #deslocamento em z
    #nr significa o número de reações, inicia-se em zero e vai ser contada na instrução while abaixo
    nrx = 0
    nry = 0
    nrz = 0
    nr  = 0

    count1 = 0
    while count1 <= 9:  # considerando 10 nós possíveis
        if desloc_x[count1] == "FIXO":
            nrx = nrx + 1

        if desloc_y[count1] == "FIXO":
            nry = nry + 1

        if desloc_y[count1] == "FIXO":
            nrz = nrz + 1

        count1 = count1 + 1


    nr = nrx + nry + nrz

    #criação das deslocabilidades em cada nó
    #utilização de um vetor bidimensional [x][nó]
    #linha representa o nó, coluna representa a deslocabilidade sendo x,y,z
    #se não tiver o string 'fixo' inserior uma
    # x positivo para direita
    # y positivo para cima
    # z positivo saindo da tela

    contador1 = 0
    contador2 = 1

    id = [[0 for x in range(3)] for y in range(qtd_barras+1)] # inicializa o vetor id

    while contador1 <= qtd_barras:
        if desloc_x[contador1] != 'FIXO':
            print(desloc_x[contador1])
            id[contador1][0] = contador2
            contador2 = contador2 + 1

        if desloc_y[contador1] != 'FIXO':
            print(desloc_x[contador1])
            id[contador1][1] = contador2
            contador2 = contador2 + 1

        if desloc_z[contador1] != 'FIXO':
            print(desloc_x[contador1])
            id[contador1][2] = contador2
            contador2 = contador2 + 1

        contador1 = contador1+1

    # cálculo dos graus de liberdade
    # para ser considerado um grau de liberdade, deve se colocar livre na janela de parametros

    contador3 = 0    #
    ngdle =  0       # número de graus de liberdade
    Fn = []          # cargas diretamente aplicadas em cada grau de liberdade

    while contador3 <= qtd_barras:
        if desloc_x[contador3] != 'FIXO':
            Fn.append(fx[contador3])
            ngdle = ngdle + 1

        if desloc_y[contador3] != 'FIXO':
            Fn.append(fy[contador3])
            ngdle = ngdle + 1


        if desloc_z[contador3] != 'FIXO':
            Fn.append(mz[contador3])
            ngdle = ngdle + 1

        contador3 = contador3 + 1

     #criação da matriz de rigidez de cada elemento
    #[barra][linha][coluna]

    k = np.zeros((qtd_barras, 6, 6))
    for x in range(0, qtd_barras, 1):
        k[x][0][0] = (e[x] * a[x]) / l[x]
        k[x][0][1] = 0
        k[x][0][2] = 0
        k[x][0][3] = (-e[x] * a[x]) / l[x]
        k[x][0][4] = 0
        k[x][0][5] = 0

        k[x][1][0] = 0
        k[x][1][1] = (12 * e[x] * i[x]) / l[x] ** 3
        k[x][1][2] = (6 * e[x] * i[x]) / l[x] ** 2
        k[x][1][3] = 0
        k[x][1][4] = (-12 * e[x] * i[x]) / l[x] ** 3
        k[x][1][5] = (6 * e[x] * i[x]) / l[x] ** 2

        k[x][2][0] = 0
        k[x][2][1] = (6 * e[x] * i[x]) / l[x] ** 2
        k[x][2][2] = (4 * e[x] * i[x]) / l[x]
        k[x][2][3] = 0
        k[x][2][4] = (-6 * e[x] * i[x]) / l[x] ** 2
        k[x][2][5] = (2 * e[x] * i[x]) / l[x]

        k[x][3][0] = (-e[x] * a[x]) / l[x]
        k[x][3][1] = 0
        k[x][3][2] = 0
        k[x][3][3] = (e[x] * a[x]) / l[x]
        k[x][3][4] = 0
        k[x][3][5] = 0

        k[x][4][0] = 0
        k[x][4][1] = (-12 * e[x] * i[x]) / l[x] ** 3
        k[x][4][2] = (-6 * e[x] * i[x]) / l[x] ** 2
        k[x][4][3] = 0
        k[x][4][4] = (12 * e[x] * i[x]) / l[x] ** 3
        k[x][4][5] = (-6 * e[x] * i[x]) / l[x] ** 2

        k[x][5][0] = 0
        k[x][5][1] = (6 * e[x] * i[x]) / l[x] ** 2
        k[x][5][2] = (2 * e[x] * i[x]) / l[x]
        k[x][5][3] = 0
        k[x][5][4] = (-6 * e[x] * i[x]) / l[x] ** 2
        k[x][5][5] = (4 * e[x] * i[x]) / l[x]

    a_file = open("1 - Matriz de rigidez local.txt", "w")
    elemento = 1
    for collums in k:
        np.savetxt(a_file, collums, newline='\n\n',  delimiter='   ',
                   footer ='Matriz de rigidez local da barra:  ' + str(elemento), fmt = '%+4.3E'
                   )
        elemento = elemento + 1
    a_file.close()

    k_memoria = k # salva a matriz de rigidez local em outro vetor
    #criação da matriz de rotação local
    r = np.zeros((qtd_barras, 6, 6))

    for x in range(0, qtd_barras, 1):

        r[x][0][0] = math.cos(theta[x])
        r[x][0][1] = -math.sin(theta[x])
        r[x][0][2] = 0
        r[x][0][3] = 0
        r[x][0][4] = 0
        r[x][0][5] = 0

        r[x][1][0] = math.sin(theta[x])
        r[x][1][1] = math.cos(theta[x])
        r[x][1][2] = 0
        r[x][1][3] = 0
        r[x][1][4] = 0
        r[x][1][5] = 0

        r[x][2][0] = 0
        r[x][2][1] = 0
        r[x][2][2] = 1
        r[x][2][3] = 0
        r[x][2][4] = 0
        r[x][2][5] = 0

        r[x][3][0] = 0
        r[x][3][1] = 0
        r[x][3][2] = 0
        r[x][3][3] = math.cos(theta[x])
        r[x][3][4] = -math.sin(theta[x])
        r[x][3][5] = 0

        r[x][4][0] = 0
        r[x][4][1] = 0
        r[x][4][2] = 0
        r[x][4][3] = math.sin(theta[x])
        r[x][4][4] = math.cos(theta[x])
        r[x][4][5] = 0

        r[x][5][0] = 0
        r[x][5][1] = 0
        r[x][5][2] = 0
        r[x][5][3] = 0
        r[x][5][4] = 0
        r[x][5][5] = 1


    b_file = open("2 - Matriz de rotação local.txt", "w")
    elemento = 1
    for collums in r:
        np.savetxt(b_file, collums, newline='\n\n', delimiter='   ',
                   footer='2 - Matriz de rotação local da barra:  ' + str(elemento),fmt = '%1.0i')
        elemento = elemento + 1
    b_file.close()



    #matriz de rotação transposta dos elementos
    rt = np.zeros((qtd_barras, 6, 6))
    for x in range(0, qtd_barras, 1):
        rt[x][0][0] = math.cos(theta[x])
        rt[x][1][0] = -math.sin(theta[x])
        rt[x][2][0] = 0
        rt[x][3][0] = 0
        rt[x][4][0] = 0
        rt[x][5][0] = 0

        rt[x][0][1] = math.sin(theta[x])
        rt[x][1][1] = math.cos(theta[x])
        rt[x][2][1] = 0
        rt[x][3][1] = 0
        rt[x][4][1] = 0
        rt[x][5][1] = 0

        rt[x][0][2] = 0
        rt[x][1][2] = 0
        rt[x][2][2] = 1
        rt[x][3][2] = 0
        rt[x][4][2] = 0
        rt[x][5][2] = 0

        rt[x][0][3] = 0
        rt[x][1][3] = 0
        rt[x][2][3] = 0
        rt[x][3][3] = math.cos(theta[x])
        rt[x][4][3] = -math.sin(theta[x])
        rt[x][5][3] = 0

        rt[x][0][4] = 0
        rt[x][1][4] = 0
        rt[x][2][4] = 0
        rt[x][3][4] = math.sin(theta[x])
        rt[x][4][4] = math.cos(theta[x])
        rt[x][5][4] = 0

        rt[x][0][5] = 0
        rt[x][1][5] = 0
        rt[x][2][5] = 0
        rt[x][3][5] = 0
        rt[x][4][5] = 0
        rt[x][5][5] = 1


    c_file = open("3 - Matriz de rotação local transposta.txt", "w")
    elemento = 1
    for collums in rt:
        np.savetxt(c_file, collums, newline='\n\n', delimiter='   ',
                   footer='3 - Matriz de rotação local transposta:  ' + str(elemento), fmt = '%1.0i')
        elemento = elemento + 1
    c_file.close()

    kgn = np.zeros((qtd_barras, 6, 6))
    #kg é a primeira parte de multiplicação de matrizes
    #kgnv vai ser a relaçao completa r*k*rt

    for x in range(0, qtd_barras, 1):
        kgn[x][0][0] = (r[x][0][0] * k[x][0][0] + r[x][0][1] * k[x][1][0] + r[x][0][2] * k[x][2][0] + r[x][0][3] * k[x][3][0] + r[x][0][4] * k[x][4][0] + r[x][0][5] * k[x][5][0])
        kgn[x][0][1] = (r[x][0][0] * k[x][0][1] + r[x][0][1] * k[x][1][1] + r[x][0][2] * k[x][2][1] + r[x][0][3] * k[x][3][1] + r[x][0][4] * k[x][4][1] + r[x][0][5] * k[x][5][1])
        kgn[x][0][2] = (r[x][0][0] * k[x][0][2] + r[x][0][1] * k[x][1][2] + r[x][0][2] * k[x][2][2] + r[x][0][3] * k[x][3][2] + r[x][0][4] * k[x][4][2] + r[x][0][5] * k[x][5][2])
        kgn[x][0][3] = (r[x][0][0] * k[x][0][3] + r[x][0][1] * k[x][1][3] + r[x][0][2] * k[x][2][3] + r[x][0][3] * k[x][3][3] + r[x][0][4] * k[x][4][3] + r[x][0][5] * k[x][5][3])
        kgn[x][0][4] = (r[x][0][0] * k[x][0][4] + r[x][0][1] * k[x][1][4] + r[x][0][2] * k[x][2][4] + r[x][0][3] * k[x][3][4] + r[x][0][4] * k[x][4][4] + r[x][0][5] * k[x][5][4])
        kgn[x][0][5] = (r[x][0][0] * k[x][0][5] + r[x][0][1] * k[x][1][5] + r[x][0][2] * k[x][2][5] + r[x][0][3] * k[x][3][5] + r[x][0][4] * k[x][4][5] + r[x][0][5] * k[x][5][5])

        kgn[x][1][0] = (r[x][1][0] * k[x][0][0] + r[x][1][1] * k[x][1][0] + r[x][1][2] * k[x][2][0] + r[x][1][3] * k[x][3][0] + r[x][1][4] * k[x][4][0] + r[x][1][5] * k[x][5][0])
        kgn[x][1][1] = (r[x][1][0] * k[x][0][1] + r[x][1][1] * k[x][1][1] + r[x][1][2] * k[x][2][1] + r[x][1][3] * k[x][3][1] + r[x][1][4] * k[x][4][1] + r[x][1][5] * k[x][5][1])
        kgn[x][1][2] = (r[x][1][0] * k[x][0][2] + r[x][1][1] * k[x][1][2] + r[x][1][2] * k[x][2][2] + r[x][1][3] * k[x][3][2] + r[x][1][4] * k[x][4][2] + r[x][1][5] * k[x][5][2])
        kgn[x][1][3] = (r[x][1][0] * k[x][0][3] + r[x][1][1] * k[x][1][3] + r[x][1][2] * k[x][2][3] + r[x][1][3] * k[x][3][3] + r[x][1][4] * k[x][4][3] + r[x][1][5] * k[x][5][3])
        kgn[x][1][4] = (r[x][1][0] * k[x][0][4] + r[x][1][1] * k[x][1][4] + r[x][1][2] * k[x][2][4] + r[x][1][3] * k[x][3][4] + r[x][1][4] * k[x][4][4] + r[x][1][5] * k[x][5][4])
        kgn[x][1][5] = (r[x][1][0] * k[x][0][5] + r[x][1][1] * k[x][1][5] + r[x][1][2] * k[x][2][5] + r[x][1][3] * k[x][3][5] + r[x][1][4] * k[x][4][5] + r[x][1][5] * k[x][5][5])

        kgn[x][2][0] = (r[x][2][0] * k[x][0][0] + r[x][2][1] * k[x][1][0] + r[x][2][2] * k[x][2][0] + r[x][2][3] * k[x][3][0] + r[x][2][4] * k[x][4][0] + r[x][2][5] * k[x][5][0])
        kgn[x][2][1] = (r[x][2][0] * k[x][0][1] + r[x][2][1] * k[x][1][1] + r[x][2][2] * k[x][2][1] + r[x][2][3] * k[x][3][1] + r[x][2][4] * k[x][4][1] + r[x][2][5] * k[x][5][1])
        kgn[x][2][2] = (r[x][2][0] * k[x][0][2] + r[x][2][1] * k[x][1][2] + r[x][2][2] * k[x][2][2] + r[x][2][3] * k[x][3][2] + r[x][2][4] * k[x][4][2] + r[x][2][5] * k[x][5][2])
        kgn[x][2][3] = (r[x][2][0] * k[x][0][3] + r[x][2][1] * k[x][1][3] + r[x][2][2] * k[x][2][3] + r[x][2][3] * k[x][3][3] + r[x][2][4] * k[x][4][3] + r[x][2][5] * k[x][5][3])
        kgn[x][2][4] = (r[x][2][0] * k[x][0][4] + r[x][2][1] * k[x][1][4] + r[x][2][2] * k[x][2][4] + r[x][2][3] * k[x][3][4] + r[x][2][4] * k[x][4][4] + r[x][2][5] * k[x][5][4])
        kgn[x][2][5] = (r[x][2][0] * k[x][0][5] + r[x][2][1] * k[x][1][5] + r[x][2][2] * k[x][2][5] + r[x][2][3] * k[x][3][5] + r[x][2][4] * k[x][4][5] + r[x][2][5] * k[x][5][5])

        kgn[x][3][0] = (r[x][3][0] * k[x][0][0] + r[x][3][1] * k[x][1][0] + r[x][3][2] * k[x][2][0] + r[x][3][3] * k[x][3][0] + r[x][3][4] * k[x][4][0] + r[x][3][5] * k[x][5][0])
        kgn[x][3][1] = (r[x][3][0] * k[x][0][1] + r[x][3][1] * k[x][1][1] + r[x][3][2] * k[x][2][1] + r[x][3][3] * k[x][3][1] + r[x][3][4] * k[x][4][1] + r[x][3][5] * k[x][5][1])
        kgn[x][3][2] = (r[x][3][0] * k[x][0][2] + r[x][3][1] * k[x][1][2] + r[x][3][2] * k[x][2][2] + r[x][3][3] * k[x][3][2] + r[x][3][4] * k[x][4][2] + r[x][3][5] * k[x][5][2])
        kgn[x][3][3] = (r[x][3][0] * k[x][0][3] + r[x][3][1] * k[x][1][3] + r[x][3][2] * k[x][2][3] + r[x][3][3] * k[x][3][3] + r[x][3][4] * k[x][4][3] + r[x][3][5] * k[x][5][3])
        kgn[x][3][4] = (r[x][3][0] * k[x][0][4] + r[x][3][1] * k[x][1][4] + r[x][3][2] * k[x][2][4] + r[x][3][3] * k[x][3][4] + r[x][3][4] * k[x][4][4] + r[x][3][5] * k[x][5][4])
        kgn[x][3][5] = (r[x][3][0] * k[x][0][5] + r[x][3][1] * k[x][1][5] + r[x][3][2] * k[x][2][5] + r[x][3][3] * k[x][3][5] + r[x][3][4] * k[x][4][5] + r[x][3][5] * k[x][5][5])

        kgn[x][4][0] = (r[x][4][0] * k[x][0][0] + r[x][4][1] * k[x][1][0] + r[x][4][2] * k[x][2][0] + r[x][4][3] * k[x][3][0] + r[x][4][4] * k[x][4][0] + r[x][4][5] * k[x][5][0])
        kgn[x][4][1] = (r[x][4][0] * k[x][0][1] + r[x][4][1] * k[x][1][1] + r[x][4][2] * k[x][2][1] + r[x][4][3] * k[x][3][1] + r[x][4][4] * k[x][4][1] + r[x][4][5] * k[x][5][1])
        kgn[x][4][2] = (r[x][4][0] * k[x][0][2] + r[x][4][1] * k[x][1][2] + r[x][4][2] * k[x][2][2] + r[x][4][3] * k[x][3][2] + r[x][4][4] * k[x][4][2] + r[x][4][5] * k[x][5][2])
        kgn[x][4][3] = (r[x][4][0] * k[x][0][3] + r[x][4][1] * k[x][1][3] + r[x][4][2] * k[x][2][3] + r[x][4][3] * k[x][3][3] + r[x][4][4] * k[x][4][3] + r[x][4][5] * k[x][5][3])
        kgn[x][4][4] = (r[x][4][0] * k[x][0][4] + r[x][4][1] * k[x][1][4] + r[x][4][2] * k[x][2][4] + r[x][4][3] * k[x][3][4] + r[x][4][4] * k[x][4][4] + r[x][4][5] * k[x][5][4])
        kgn[x][4][5] = (r[x][4][0] * k[x][0][5] + r[x][4][1] * k[x][1][5] + r[x][4][2] * k[x][2][5] + r[x][4][3] * k[x][3][5] + r[x][4][4] * k[x][4][5] + r[x][4][5] * k[x][5][5])

        kgn[x][5][0] = (r[x][5][0] * k[x][0][0] + r[x][5][1] * k[x][1][0] + r[x][5][2] * k[x][2][0] + r[x][5][3] * k[x][3][0] + r[x][5][4] * k[x][4][0] + r[x][5][5] * k[x][5][0])
        kgn[x][5][1] = (r[x][5][0] * k[x][0][1] + r[x][5][1] * k[x][1][1] + r[x][5][2] * k[x][2][1] + r[x][5][3] * k[x][3][1] + r[x][5][4] * k[x][4][1] + r[x][5][5] * k[x][5][1])
        kgn[x][5][2] = (r[x][5][0] * k[x][0][2] + r[x][5][1] * k[x][1][2] + r[x][5][2] * k[x][2][2] + r[x][5][3] * k[x][3][2] + r[x][5][4] * k[x][4][2] + r[x][5][5] * k[x][5][2])
        kgn[x][5][3] = (r[x][5][0] * k[x][0][3] + r[x][5][1] * k[x][1][3] + r[x][5][2] * k[x][2][3] + r[x][5][3] * k[x][3][3] + r[x][5][4] * k[x][4][3] + r[x][5][5] * k[x][5][3])
        kgn[x][5][4] = (r[x][5][0] * k[x][0][4] + r[x][5][1] * k[x][1][4] + r[x][5][2] * k[x][2][4] + r[x][5][3] * k[x][3][4] + r[x][5][4] * k[x][4][4] + r[x][5][5] * k[x][5][4])
        kgn[x][5][5] = (r[x][5][0] * k[x][0][5] + r[x][5][1] * k[x][1][5] + r[x][5][2] * k[x][2][5] + r[x][5][3] * k[x][3][5] + r[x][5][4] * k[x][4][5] + r[x][5][5] * k[x][5][5])

        kgnv = np.zeros((qtd_barras, 6, 6))

        for x in range(0, qtd_barras, 1):

            kgnv[x][0][0] = (kgn[x][0][0] * rt[x][0][0] + kgn[x][0][1] * rt[x][1][0] + kgn[x][0][2] * rt[x][2][0] + kgn[x][0][3] * rt[x][3][0] + kgn[x][0][4] * rt[x][4][0] + kgn[x][0][5] * rt[x][5][0])
            kgnv[x][0][1] = (kgn[x][0][0] * rt[x][0][1] + kgn[x][0][1] * rt[x][1][1] + kgn[x][0][2] * rt[x][2][1] + kgn[x][0][3] * rt[x][3][1] + kgn[x][0][4] * rt[x][4][1] + kgn[x][0][5] * rt[x][5][1])
            kgnv[x][0][2] = (kgn[x][0][0] * rt[x][0][2] + kgn[x][0][1] * rt[x][1][2] + kgn[x][0][2] * rt[x][2][2] + kgn[x][0][3] * rt[x][3][2] + kgn[x][0][4] * rt[x][4][2] + kgn[x][0][5] * rt[x][5][2])
            kgnv[x][0][3] = (kgn[x][0][0] * rt[x][0][3] + kgn[x][0][1] * rt[x][1][3] + kgn[x][0][2] * rt[x][2][3] + kgn[x][0][3] * rt[x][3][3] + kgn[x][0][4] * rt[x][4][3] + kgn[x][0][5] * rt[x][5][3])
            kgnv[x][0][4] = (kgn[x][0][0] * rt[x][0][4] + kgn[x][0][1] * rt[x][1][4] + kgn[x][0][2] * rt[x][2][4] + kgn[x][0][3] * rt[x][3][4] + kgn[x][0][4] * rt[x][4][4] + kgn[x][0][5] * rt[x][5][4])
            kgnv[x][0][5] = (kgn[x][0][0] * rt[x][0][5] + kgn[x][0][1] * rt[x][1][5] + kgn[x][0][2] * rt[x][2][5] + kgn[x][0][3] * rt[x][3][5] + kgn[x][0][4] * rt[x][4][5] + kgn[x][0][5] * rt[x][5][5])

            kgnv[x][1][0] = (kgn[x][1][0] * rt[x][0][0] + kgn[x][1][1] * rt[x][1][0] + kgn[x][1][2] * rt[x][2][0] + kgn[x][1][3] * rt[x][3][0] + kgn[x][1][4] * rt[x][4][0] + kgn[x][1][5] * rt[x][5][0])
            kgnv[x][1][1] = (kgn[x][1][0] * rt[x][0][1] + kgn[x][1][1] * rt[x][1][1] + kgn[x][1][2] * rt[x][2][1] + kgn[x][1][3] * rt[x][3][1] + kgn[x][1][4] * rt[x][4][1] + kgn[x][1][5] * rt[x][5][1])
            kgnv[x][1][2] = (kgn[x][1][0] * rt[x][0][2] + kgn[x][1][1] * rt[x][1][2] + kgn[x][1][2] * rt[x][2][2] + kgn[x][1][3] * rt[x][3][2] + kgn[x][1][4] * rt[x][4][2] + kgn[x][1][5] * rt[x][5][2])
            kgnv[x][1][3] = (kgn[x][1][0] * rt[x][0][3] + kgn[x][1][1] * rt[x][1][3] + kgn[x][1][2] * rt[x][2][3] + kgn[x][1][3] * rt[x][3][3] + kgn[x][1][4] * rt[x][4][3] + kgn[x][1][5] * rt[x][5][3])
            kgnv[x][1][4] = (kgn[x][1][0] * rt[x][0][4] + kgn[x][1][1] * rt[x][1][4] + kgn[x][1][2] * rt[x][2][4] + kgn[x][1][3] * rt[x][3][4] + kgn[x][1][4] * rt[x][4][4] + kgn[x][1][5] * rt[x][5][4])
            kgnv[x][1][5] = (kgn[x][1][0] * rt[x][0][5] + kgn[x][1][1] * rt[x][1][5] + kgn[x][1][2] * rt[x][2][5] + kgn[x][1][3] * rt[x][3][5] + kgn[x][1][4] * rt[x][4][5] + kgn[x][1][5] * rt[x][5][5])

            kgnv[x][2][0] = (kgn[x][2][0] * rt[x][0][0] + kgn[x][2][1] * rt[x][1][0] + kgn[x][2][2] * rt[x][2][0] + kgn[x][2][3] * rt[x][3][0] + kgn[x][2][4] * rt[x][4][0] + kgn[x][2][5] * rt[x][5][0])
            kgnv[x][2][1] = (kgn[x][2][0] * rt[x][0][1] + kgn[x][2][1] * rt[x][1][1] + kgn[x][2][2] * rt[x][2][1] + kgn[x][2][3] * rt[x][3][1] + kgn[x][2][4] * rt[x][4][1] + kgn[x][2][5] * rt[x][5][1])
            kgnv[x][2][2] = (kgn[x][2][0] * rt[x][0][2] + kgn[x][2][1] * rt[x][1][2] + kgn[x][2][2] * rt[x][2][2] + kgn[x][2][3] * rt[x][3][2] + kgn[x][2][4] * rt[x][4][2] + kgn[x][2][5] * rt[x][5][2])
            kgnv[x][2][3] = (kgn[x][2][0] * rt[x][0][3] + kgn[x][2][1] * rt[x][1][3] + kgn[x][2][2] * rt[x][2][3] + kgn[x][2][3] * rt[x][3][3] + kgn[x][2][4] * rt[x][4][3] + kgn[x][2][5] * rt[x][5][3])
            kgnv[x][2][4] = (kgn[x][2][0] * rt[x][0][4] + kgn[x][2][1] * rt[x][1][4] + kgn[x][2][2] * rt[x][2][4] + kgn[x][2][3] * rt[x][3][4] + kgn[x][2][4] * rt[x][4][4] + kgn[x][2][5] * rt[x][5][4])
            kgnv[x][2][5] = (kgn[x][2][0] * rt[x][0][5] + kgn[x][2][1] * rt[x][1][5] + kgn[x][2][2] * rt[x][2][5] + kgn[x][2][3] * rt[x][3][5] + kgn[x][2][4] * rt[x][4][5] + kgn[x][2][5] * rt[x][5][5])

            kgnv[x][3][0] = (kgn[x][3][0] * rt[x][0][0] + kgn[x][3][1] * rt[x][1][0] + kgn[x][3][2] * rt[x][2][0] + kgn[x][3][3] * rt[x][3][0] + kgn[x][3][4] * rt[x][4][0] + kgn[x][3][5] * rt[x][5][0])
            kgnv[x][3][1] = (kgn[x][3][0] * rt[x][0][1] + kgn[x][3][1] * rt[x][1][1] + kgn[x][3][2] * rt[x][2][1] + kgn[x][3][3] * rt[x][3][1] + kgn[x][3][4] * rt[x][4][1] + kgn[x][3][5] * rt[x][5][1])
            kgnv[x][3][2] = (kgn[x][3][0] * rt[x][0][2] + kgn[x][3][1] * rt[x][1][2] + kgn[x][3][2] * rt[x][2][2] + kgn[x][3][3] * rt[x][3][2] + kgn[x][3][4] * rt[x][4][2] + kgn[x][3][5] * rt[x][5][2])
            kgnv[x][3][3] = (kgn[x][3][0] * rt[x][0][3] + kgn[x][3][1] * rt[x][1][3] + kgn[x][3][2] * rt[x][2][3] + kgn[x][3][3] * rt[x][3][3] + kgn[x][3][4] * rt[x][4][3] + kgn[x][3][5] * rt[x][5][3])
            kgnv[x][3][4] = (kgn[x][3][0] * rt[x][0][4] + kgn[x][3][1] * rt[x][1][4] + kgn[x][3][2] * rt[x][2][4] + kgn[x][3][3] * rt[x][3][4] + kgn[x][3][4] * rt[x][4][4] + kgn[x][3][5] * rt[x][5][4])
            kgnv[x][3][5] = (kgn[x][3][0] * rt[x][0][5] + kgn[x][3][1] * rt[x][1][5] + kgn[x][3][2] * rt[x][2][5] + kgn[x][3][3] * rt[x][3][5] + kgn[x][3][4] * rt[x][4][5] + kgn[x][3][5] * rt[x][5][5])

            kgnv[x][4][0] = (kgn[x][4][0] * rt[x][0][0] + kgn[x][4][1] * rt[x][1][0] + kgn[x][4][2] * rt[x][2][0] + kgn[x][4][3] * rt[x][3][0] + kgn[x][4][4] * rt[x][4][0] + kgn[x][4][5] * rt[x][5][0])
            kgnv[x][4][1] = (kgn[x][4][0] * rt[x][0][1] + kgn[x][4][1] * rt[x][1][1] + kgn[x][4][2] * rt[x][2][1] + kgn[x][4][3] * rt[x][3][1] + kgn[x][4][4] * rt[x][4][1] + kgn[x][4][5] * rt[x][5][1])
            kgnv[x][4][2] = (kgn[x][4][0] * rt[x][0][2] + kgn[x][4][1] * rt[x][1][2] + kgn[x][4][2] * rt[x][2][2] + kgn[x][4][3] * rt[x][3][2] + kgn[x][4][4] * rt[x][4][2] + kgn[x][4][5] * rt[x][5][2])
            kgnv[x][4][3] = (kgn[x][4][0] * rt[x][0][3] + kgn[x][4][1] * rt[x][1][3] + kgn[x][4][2] * rt[x][2][3] + kgn[x][4][3] * rt[x][3][3] + kgn[x][4][4] * rt[x][4][3] + kgn[x][4][5] * rt[x][5][3])
            kgnv[x][4][4] = (kgn[x][4][0] * rt[x][0][4] + kgn[x][4][1] * rt[x][1][4] + kgn[x][4][2] * rt[x][2][4] + kgn[x][4][3] * rt[x][3][4] + kgn[x][4][4] * rt[x][4][4] + kgn[x][4][5] * rt[x][5][4])
            kgnv[x][4][5] = (kgn[x][4][0] * rt[x][0][5] + kgn[x][4][1] * rt[x][1][5] + kgn[x][4][2] * rt[x][2][5] + kgn[x][4][3] * rt[x][3][5] + kgn[x][4][4] * rt[x][4][5] + kgn[x][4][5] * rt[x][5][5])

            kgnv[x][5][0] = (kgn[x][5][0] * rt[x][0][0] + kgn[x][5][1] * rt[x][1][0] + kgn[x][5][2] * rt[x][2][0] + kgn[x][5][3] * rt[x][3][0] + kgn[x][5][4] * rt[x][4][0] + kgn[x][5][5] * rt[x][5][0])
            kgnv[x][5][1] = (kgn[x][5][0] * rt[x][0][1] + kgn[x][5][1] * rt[x][1][1] + kgn[x][5][2] * rt[x][2][1] + kgn[x][5][3] * rt[x][3][1] + kgn[x][5][4] * rt[x][4][1] + kgn[x][5][5] * rt[x][5][1])
            kgnv[x][5][2] = (kgn[x][5][0] * rt[x][0][2] + kgn[x][5][1] * rt[x][1][2] + kgn[x][5][2] * rt[x][2][2] + kgn[x][5][3] * rt[x][3][2] + kgn[x][5][4] * rt[x][4][2] + kgn[x][5][5] * rt[x][5][2])
            kgnv[x][5][3] = (kgn[x][5][0] * rt[x][0][3] + kgn[x][5][1] * rt[x][1][3] + kgn[x][5][2] * rt[x][2][3] + kgn[x][5][3] * rt[x][3][3] + kgn[x][5][4] * rt[x][4][3] + kgn[x][5][5] * rt[x][5][3])
            kgnv[x][5][4] = (kgn[x][5][0] * rt[x][0][4] + kgn[x][5][1] * rt[x][1][4] + kgn[x][5][2] * rt[x][2][4] + kgn[x][5][3] * rt[x][3][4] + kgn[x][5][4] * rt[x][4][4] + kgn[x][5][5] * rt[x][5][4])
            kgnv[x][5][5] = (kgn[x][5][0] * rt[x][0][5] + kgn[x][5][1] * rt[x][1][5] + kgn[x][5][2] * rt[x][2][5] + kgn[x][5][3] * rt[x][3][5] + kgn[x][5][4] * rt[x][4][5] + kgn[x][5][5] * rt[x][5][5])


    d_file = open("4 -  Matriz de rigidez da barra.txt", "w")
    elemento = 1
    for collums in kgnv:
        np.savetxt(d_file, collums, newline='\n\n', delimiter='   ',
                   footer='Matriz de rigidez da barra:  ' + str(elemento),fmt = '%+4.3E')
        elemento = elemento + 1
    d_file.close()

    # matriz de rigidez global do sistema



    deslocabilidade = np.zeros((ngdle, ngdle))

    if ngdle == 2:
        deslocabilidade = np.zeros((ngdle+1, ngdle+1))

    if ngdle == 0:
        deslocabilidade = np.zeros((ngdle + 3, ngdle + 3))

    if ngdle == 1:
        deslocabilidade = np.zeros((ngdle + 2, ngdle + 2))

    print(ngdle)
    contador4 = 1



    for x in range(0, qtd_barras + 1, 1):
        if desloc_x[x] != "FIXO":
            deslocabilidade[x][0] = contador4
            contador4 = contador4 + 1

        if desloc_y[x] != "FIXO":
            deslocabilidade[x][1] = contador4
            contador4 = contador4 + 1

        if desloc_z[x] != "FIXO":
            deslocabilidade[x][2] = contador4
            contador4 = contador4 + 1

    ngdle_matriz = np.zeros((qtd_barras, 6))

    for x in range(0, qtd_barras, 1):
        ngdle_matriz[x][0] = int(deslocabilidade[(conectividade[x][0])-1][0])
        ngdle_matriz[x][1] = int(deslocabilidade[(conectividade[x][0])-1][1])
        ngdle_matriz[x][2] = int(deslocabilidade[(conectividade[x][0])-1][2])
        ngdle_matriz[x][3] = int(deslocabilidade[(conectividade[x][1])-1][0])
        ngdle_matriz[x][4] = int(deslocabilidade[(conectividade[x][1])-1][1])
        ngdle_matriz[x][5] = int(deslocabilidade[(conectividade[x][1])-1][2])


    np.savetxt("5 - Deslocabilidades.txt", ngdle_matriz,
               newline='\n\n', delimiter=' ', fmt = '%1.0i')

    kg = np.zeros((ngdle, ngdle))

    for i in range(0, qtd_barras, 1):
        for m in range(0, 6, 1):
            j = int(ngdle_matriz[i][m]-1)
            if ngdle_matriz[i][m] > 0:
                for n in range(0, 6, 1):
                    k = int(ngdle_matriz[i][n]-1)
                    if ngdle_matriz[i][n] > 0:
                        kg[j][k] = kg[j][k] + kgnv[i][m][n]


    np.savetxt("6 - Matriz de rigidez global.txt", kg,  newline='\n\n',
               delimiter='   ', fmt = '%+4.3e')

    # montagem do vetor de cargas
    # vetor de esforços de engastamento perfeito de um elemento no sistema local
    # feq carga distribuida

    feq = np.zeros((qtd_barras, 6))

    for x in range(0, qtd_barras, 1):

        # por questões de orientação eu transfiro qx para qy

        if theta[x] == 0: # barra na horizontal
                feq[x][0] = 0 * l[x] / 2
                feq[x][1] = -qy[x] * l[x] / 2
                feq[x][2] = -qy[x] * (l[x]**2) / 12
                feq[x][3] = 0 * l[x] / 2
                feq[x][4] = -qy[x] * l[x] / 2
                feq[x][5] = qy[x] * (l[x] ** 2) / 12

        if theta[x] == math.pi/2:  # barra 90
             # Q[Y] = - Q[X]
             # qx = 0

                feq[x][0] = 0 * l[x] / 2
                feq[x][1] = qx[x] * l[x] / 2
                feq[x][2] = qx[x] * (l[x] ** 2) / 12
                feq[x][3] = 0 * l[x] / 2
                feq[x][4] = qx[x] * l[x] / 2
                feq[x][5] = -qx[x] * (l[x] ** 2) / 12

        if theta[x] == 3*math.pi/ 2:  # barra 270

                feq[x][0] = 0 * l[x] / 2
                feq[x][1] = -qx[x] * l[x] / 2
                feq[x][2] = -qx[x] * (l[x] ** 2) / 12
                feq[x][3] = 0 * l[x] / 2
                feq[x][4] = -qx[x] * l[x] / 2
                feq[x][5] =  qx[x] * (l[x] ** 2) / 12



    #np.savetxt("Vetor de feq.txt", feq, newline='\n\n', delimiter='   ', fmt = '%+1.3E')

    fep = np.zeros((qtd_barras, 6))



    #não é possível cargas pontuais fora dos nós
    #não vai ter a parcela das forças de engastamento de cargas pontuais
    # fe = feq+ fep .... sem fep

    fe = np.zeros((qtd_barras, 6))
    fe = feq+fep
    # esforços nodais equivalentes no sistema global
    #feg = np.zeros((qtd_barras, 6))
    feg = feq + fep

    for x in range(0, qtd_barras, 1):
        feg[x][0] = -r[x][0][0] * feq[x][0] - r[x][0][1] * feq[x][1] - r[x][0][2] * feq[x][2] - r[x][0][3] * feq[x][3] - r[x][0][4] * feq[x][4] - r[x][0][5] * feq[x][5]
        feg[x][1] = -r[x][1][0] * feq[x][0] - r[x][1][1] * feq[x][1] - r[x][1][2] * feq[x][2] - r[x][1][3] * feq[x][3] - r[x][1][4] * feq[x][4] - r[x][1][5] * feq[x][5]
        feg[x][2] = -r[x][2][0] * feq[x][0] - r[x][2][1] * feq[x][1] - r[x][2][2] * feq[x][2] - r[x][2][3] * feq[x][3] - r[x][2][4] * feq[x][4] - r[x][2][5] * feq[x][5]
        feg[x][3] = -r[x][3][0] * feq[x][0] - r[x][3][1] * feq[x][1] - r[x][3][2] * feq[x][2] - r[x][3][3] * feq[x][3] - r[x][3][4] * feq[x][4] - r[x][3][5] * feq[x][5]
        feg[x][4] = -r[x][4][0] * feq[x][0] - r[x][4][1] * feq[x][1] - r[x][4][2] * feq[x][2] - r[x][4][3] * feq[x][3] - r[x][4][4] * feq[x][4] - r[x][4][5] * feq[x][5]
        feg[x][5] = -r[x][5][0] * feq[x][0] - r[x][5][1] * feq[x][1] - r[x][5][2] * feq[x][2] - r[x][5][3] * feq[x][3] - r[x][5][4] * feq[x][4] - r[x][5][5] * feq[x][5]

    #np.savetxt(" - Matriz de feg.txt", feg, newline='\n\n', delimiter='   ', fmt = '%+1.3e')
    #montagem do vetor de forças nodais equivalentes da estrutura

    fnodais = np.zeros((qtd_barras, 6))

    for x in range(0, qtd_barras, 1):

        if desloc_x[(conectividade[x][0] - 1)] == 'FIXO':
            fnodais[x][0] = 0
        else:
            fnodais[x][0] = fx[(conectividade[x][0] - 1)]
            fx[(conectividade[x][0] - 1)] = 0



        if desloc_y[(conectividade[x][0] - 1)] == 'FIXO':
            fnodais[x][1] = 0
        else:
            fnodais[x][1] = fy[(conectividade[x][0] - 1)]
            fy[(conectividade[x][0] - 1)] = 0



        if desloc_z[(conectividade[x][0] - 1)] == 'FIXO':
            fnodais[x][2] = 0
        else:
            fnodais[x][2] = mz[(conectividade[x][0] - 1)]
            mz[(conectividade[x][0] - 1)] = 0


        if desloc_x[(conectividade[x][1] - 1)] == 'FIXO':
            fnodais[x][3] = 0
        else:
            fnodais[x][3] = fx[(conectividade[x][1] - 1)]
            fx[(conectividade[x][1] - 1)] = 0



        if desloc_y[(conectividade[x][1] - 1)] == 'FIXO':
            fnodais[x][4] = 0
        else:
            fnodais[x][4] = fy[(conectividade[x][1] - 1)]
            fy[(conectividade[x][1] - 1)] = 0


        if desloc_z[(conectividade[x][1] - 1)] == 'FIXO':
            fnodais[x][5] = 0
        else:
            fnodais[x][5] = mz[(conectividade[x][1] - 1)]
            mz[(conectividade[x][1] - 1)] = 0


    #np.savetxt("Matriz de fnodais.txt", fnodais, newline='\n\n', delimiter='   ', fmt = '%+1.3e')
    f = np.zeros(ngdle)

    for i in range(0, qtd_barras, 1):
        for n in range(0, 6, 1):
            k = int(ngdle_matriz[i][n] - 1)
            if ngdle_matriz[i][n] > 0:
                f[k] = f[k] + feg[i][n] + fnodais[i][n]



    np.savetxt("7 - Matriz de forças F.txt", f, newline='\n\n', delimiter=' ',    fmt = '%+1.3E')

    x = np.linalg.solve(kg,f)

    np.savetxt("8 - Matriz de deslocamentos.txt", x, newline='\n\n', delimiter='  ', fmt = '%+4.3e')

    #determinação dos esforços internos
    #criação do vetor xg

    xg = np.zeros((qtd_barras, 6))
    for i in range(0, qtd_barras, 1):
        for n in range(0, 6, 1):
            k = int(ngdle_matriz[i][n] - 1)
            if ngdle_matriz[i][n] > 0:
                xg[i][n] = x[k]

    #geração do arquivo de deslocamentos por barra
    f_file = open("9 - Deslocamentos por barra.txt", "w")
    elemento = 1
    for collums in xg:
        np.savetxt(f_file, collums, newline='\n\n', delimiter='   ',
                   footer='Deslocamentos barra:  ' + str(elemento), fmt = '%+4.3E'
                   )
        elemento = elemento + 1
    f_file.close()

    #cálculo dos esforços finais em cada elemento
    esf = np.zeros((qtd_barras, 6))
    k_f = np.zeros((6, 6))
    r_f = np.zeros((6, 6))




    for x in range(0, qtd_barras, 1):

        if desloc_x[(conectividade[x][0] - 1)] == 'FIXO':
            fnodais[x][0] = 0
        else:
            fnodais[x][0] = fx[(conectividade[x][0] - 1)]


        if desloc_y[(conectividade[x][0] - 1)] == 'FIXO':
            fnodais[x][1] = 0
        else:
            fnodais[x][1] = fy[(conectividade[x][0] - 1)]



        if desloc_z[(conectividade[x][0] - 1)] == 'FIXO':
            fnodais[x][2] = 0
        else:
            fnodais[x][2] = mz[(conectividade[x][0] - 1)]



        if desloc_x[(conectividade[x][1] - 1)] == 'FIXO':
            fnodais[x][3] = 0
        else:
            fnodais[x][3] = fx[(conectividade[x][1] - 1)]



        if desloc_y[(conectividade[x][1] - 1)] == 'FIXO':
            fnodais[x][4] = 0
        else:
            fnodais[x][4] = fy[(conectividade[x][1] - 1)]


        if desloc_z[(conectividade[x][1] - 1)] == 'FIXO':
            fnodais[x][5] = 0
        else:
            fnodais[x][5] = mz[(conectividade[x][1] - 1)]

    print("Valores no inicio 2do algoritmo das cargas")
    print(fx)
    print(fy)
    print(mz)
    print(qx)
    print(qy)

    for m in range(0, qtd_barras, 1):
       for count in range(0,6,1):
           for count2 in range(0,6,1):
               k_f[count][count2] = k_memoria[m][count][count2]
               r_f[count][count2] = rt[m][count][count2]
       a = np.matmul(k_f,r_f)
       b = np.matmul(a, xg[m])
       for n in range(0, 6, 1):
           esf[m][n] = fe[m][n] + b[n] + fnodais[m][n]

    # geração do arquivo de esforços por barra
   # g_file = open("10 - Esforços por barra.txt", "w")
   # elemento = 1
    #for collums in esf:
     #   np.savetxt(g_file, collums, newline='\n\n', delimiter='   ',
      #             footer='Esforços na barra:  ' + str(elemento), fmt = '%1.2f'
       #            )
       # elemento = elemento + 1
   # g_file.close()




    #diagramas de esforços solicitantes

    diagramas_window = Tk()
    diagramas_window.title('Diagramas')
    diagramas_window.iconbitmap('imagens/engenharia.ico')  # icone
    diagramas_window.geometry("1366x768")

    def center_window(w=1000, h=1000):
        # get screen width and height
        ws = diagramas_window.winfo_screenwidth()
        hs = diagramas_window.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        diagramas_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    center_window(350, 240)

    lb_diagramas = LabelFrame(diagramas_window, text="Diagramas", borderwidth=1, relief="solid")
    lb_diagramas.place(x=2, y=5, width=345, height=235)

    # Seleção da barra
    barra_diagrama = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    barra_diagrama_combox = Combobox(diagramas_window, values=barra_diagrama, width=5)
    barra_diagrama_combox.place(x=170, y=20)

    set_barra = Label(diagramas_window, text="Escolha uma barra: ")
    set_barra.place(x=5, y=20)


    def grafico_normal():
           barra_escolhida = int(barra_diagrama_combox.get())

           cortante = 0
           x = np.arange(0.0, l[barra_escolhida-1], 0.001)

           normal = esf[barra_escolhida-1][0]*(-1) + x - x
           fig1, ax1 = plt.subplots()

           ax1.plot(x, normal)
           ax1.set(xlabel='Comprimento (m)', ylabel='Normal (kN)', title='Esforço normal na barra: ' + str(barra_escolhida))
           ax1.grid()
           fig1.savefig("normal.png")
           plt.show()


    def grafico_cortante():
           barra_escolhida = int(barra_diagrama_combox.get())

           cortante = 0
           x = np.arange(0.0, l[barra_escolhida-1], 0.001)

           if theta[barra_escolhida-1] == 0:
               cortante = esf[barra_escolhida-1][1] + qy[barra_escolhida-1]*x

           if theta[barra_escolhida-1] == math.pi/2:
               cortante = esf[barra_escolhida-1][1] - qx[barra_escolhida-1]*x

           if theta[barra_escolhida - 1] == (3*math.pi/2):
               cortante = esf[barra_escolhida-1][1] + qx[barra_escolhida-1]*x

           fig1, ax1 = plt.subplots()
           ax1.plot(x, cortante)
           ax1.set(xlabel='Comprimento (m)', ylabel='Cortante (kN)', title='Esforço cortante na barra: ' + str(barra_escolhida))
           ax1.grid()
           fig1.savefig("cortante.png")
           plt.show()

    def grafico_fletor():
        barra_escolhida = int(barra_diagrama_combox.get())

        fletor = 0
        x = np.arange(0.0, l[barra_escolhida - 1], 0.001)


        if theta[barra_escolhida-1] == 0:
            fletor = esf[barra_escolhida-1][2]*(-1) + esf[barra_escolhida-1][1]*x + qy[barra_escolhida-1]*x*x/2


        if theta[barra_escolhida - 1] == math.pi/2:
            fletor = esf[barra_escolhida-1][2]*(-1) + esf[barra_escolhida-1][1]*x-qx[barra_escolhida-1]*x*x/2


        if theta[barra_escolhida - 1] == (3*math.pi)/2:
            fletor = esf[barra_escolhida-1][2] - esf[barra_escolhida-1][1]*x-qx[barra_escolhida-1]*x*x/2





        fig1, ax1 = plt.subplots()
        ax1.plot(x, fletor)
        ax1.invert_yaxis()
        ax1.set(xlabel='Comprimento (m)', ylabel='Fletor (kN.m)',  title='Esforço fletor na barra: ' + str(barra_escolhida))
        ax1.grid()
        fig1.savefig("fletor.png")
        plt.show()



    bottom_normal = Button(diagramas_window, command = grafico_normal, text="Normal", width=10, height=2)
    bottom_normal.place(x=130, y=60)

    bottom_cortante = Button(diagramas_window, command=grafico_cortante, text="Cortante", width=10, height=2)
    bottom_cortante.place(x=130, y=120)

    bottom_fletor = Button(diagramas_window, command=grafico_fletor, text="Fletor", width=10, height=2)
    bottom_fletor.place(x=130, y=180)

    diagramas_window.mainloop()













