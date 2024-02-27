from math import comb
from tkinter import *  #type: ignore
from os import system
import threading
from random import choice
from time import sleep


try: system('cls')
except: system('clear')

def jogo():
    def gerarNota():
        cor = choice(cores_notas)
        nota = Label(window, bg=cor)
        nota.place(x=701+(cores_notas.index(cor)*60), y=1, width=45, height=20)
        notas.append([nota, 0])

    def alterarPonteiro():
        try: window.state()
        except: return
        ponteiro_barra.place(y=406+6*ponteiro_perda)
        if ponteiro_perda <= 11:
            barras[0]['bg'] = 'green3'
            barras[1]['bg'] = 'gold4'
        elif ponteiro_perda <= 22:
            barras[0]['bg'] = 'green4'
            barras[1]['bg'] = 'gold'
            barras[2]['bg'] = 'red4'
        else:
            barras[1]['bg'] = 'gold4'
            barras[2]['bg'] = 'red2'

    def descerNotas():
        global combo, xpontos, perdidas, ponteiro_perda

        for nota in notas[::-1]:
            try:
                idx = cores_notas.index(nota[0]['bg'])
                if nota[1] >= 645:
                    nota[0].destroy()
                    del notas[notas.index(nota)]
                    continue
                nota[1] += 15
                nota[0].place(y=nota[1])
                if nota[1] >= 565 and nota[1] < 625 and nota[0] not in notas_clicaveis[idx]:
                    notas_clicaveis[idx].append(nota[0])
                elif nota[1] >= 625:
                    del notas_clicaveis[idx][0]
                    combo = 0
                    texto_combo['text'] = 'combo:   0000'
                    xpontos = 1
                    texto_xpontos['text'] = '1X'
                    perdidas += 1
                    ponteiro_perda += 1
                    if ponteiro_perda == 34:
                        saida()
                    alterarPonteiro()
            except: continue

    def clicadaTecla(indext):
        global combo, notas_clicaveis, xpontos, pontos, erradas, combo_max, ponteiro_perda, acertadas

        try: window.state()
        except: return
        teclas_clicar[indext]['bg'] = cores_notas[indext]
        if notas_clicaveis[indext] == []:
            combo = 0
            xpontos = 1
            erradas += 1
            ponteiro_perda += 1
            if ponteiro_perda == 34:
                saida()
            alterarPonteiro()
        else:
            for nota in notas:
                if nota[0] in notas_clicaveis[indext]:
                    nota[0].destroy()
                    del notas[notas.index(nota)]
                    break
            del notas_clicaveis[indext][0]
            combo += 1
            combo_max = combo if combo > combo_max else combo_max
            acertadas += 1
            ponteiro_perda -= 1 if ponteiro_perda > 1 else 0
            alterarPonteiro()
            if combo == 30:
                xpontos = 4
            elif combo == 20:
                xpontos = 3
            elif combo == 10:
                xpontos = 2
            pontos += 5 * xpontos
        try: window.state()
        except: return
        texto_pontos['text'] = f'pontos: {pontos:05.0f}'
        texto_xpontos['text'] = f'{xpontos}X'
        texto_combo['text'] = f'combo:   {combo:04.0f}'

    window.bind('a', lambda e: clicadaTecla(0))
    window.bind('A', lambda e: clicadaTecla(0))
    window.bind('s', lambda e: clicadaTecla(1))
    window.bind('S', lambda e: clicadaTecla(1))
    window.bind('j', lambda e: clicadaTecla(2))
    window.bind('J', lambda e: clicadaTecla(2))
    window.bind('k', lambda e: clicadaTecla(3))
    window.bind('K', lambda e: clicadaTecla(3))
    while True:
        for x in range(3):
            descerNotas()
            #    (0.03)
            sleep(0.03)
        for i, x in enumerate(teclas_clicar):
            x['bg'] = cores_teclas[i]
        gerarNota()
        # if len(notas) != 5:
        #     gerarNota()
        ...


window = Tk()
alturaTela, larguraTela = int(window.winfo_screenheight()), int(window.winfo_screenwidth())
window.geometry(f'{larguraTela}x{alturaTela}+-8+-31')
fundo = Label(window, bg='black')
fundo.place(x=0, y=0, height=alturaTela, width=larguraTela)
window.resizable(False, False)
notas = []
# VERDE, VERMELHO, AMARELO, AZUL, LARANJA
cores_notas = ['green2', 'red', 'yellow', 'blue']
cores_teclas = ['green4', 'red3', 'gold2', 'blue4']
teclas_txts = ['A', 'S', 'J', 'K']
teclas_clicar = []
notas_clicaveis = [[], [], [], []]
combo = 0
combo_max = 0
acertadas = 0
erradas = 0
perdidas = 0
pontos = 0
xpontos = 1

for x in range(5):
    linha = Label(window, bg='black')
    linha.place(x=692+x*60, y=0, width=60, height=665)
    linha = Label(window, bg='white')
    linha.place(x=692+x*60, y=0, width=3, height=665)
    if x <= 3:
        tecla_txt = Label(window, bg='black', fg=cores_teclas[x], text=teclas_txts[x], font=['Impact', 30])
        tecla_txt.place(x=711+x*60, y=630)
        tecla = Label(window, bg=cores_teclas[x])
        tecla.place(x=701+(cores_teclas.index(cores_teclas[x])*60), y=585, width=45, height=40)
        teclas_clicar.append(tecla)

# green3, gold, red2
# green4, gold4, red4
barras = []
for x in range(3):
    cores_barra = ['green4', 'gold', 'red4']
    barra = Label(window, bg=cores_barra[x])
    barra.place(x=620, y=412+66*x, width=50, height=66)
    barras.append(barra)
ponteiro_perda = 17
ponteiro_barra = Label(window, bg='gainsboro')
ponteiro_barra.place(x=620, y=406+6*ponteiro_perda, width=50, height=6)

texto_pontos = Label(window, bg='black', fg='white', text=f'pontos: {pontos:05.0f}', font=('', 20))
texto_pontos.place(x=400, y=400)
texto_combo = Label(window, bg='black', fg='white', text=f'combo:   {combo:04.0f}', font=('', 20))
texto_combo.place(x=400, y=440)
texto_xpontos = Label(window, bg='black', fg='white', text=f'{xpontos}X', font=('', 20))
texto_xpontos.place(x=796, y=690)

def saida():
    print(f'Pontuação:    {pontos:5.0f}')
    print(f'Combo Máximo: {combo_max:5.0f}')
    print(f'Acertadas:    {acertadas:5.0f}')
    print(f'Erradas:      {erradas:5.0f}')
    print(f'Perdidas:     {perdidas:5.0f}')
    window.destroy()
window.bind('<Escape>', lambda e: saida())

thread = threading.Thread(target=jogo)
thread.daemon = True
thread.start()


window.mainloop()
