# -*- coding: cp1252 -*-

import matplotlib.pyplot as plt
#biblioteca de plotagem
import numpy as np
#biblioteca de criacao de sequencia
#linscape(start stop num endpoint retstep)
#start - limite inicial
#stop - limite final
#num - numero de pontos no intervalo(start/stop)
#endpoint - inclui/exclui o ultimo ponto (true/false)
#retstep - false=(stop-start)/num-1 -mostra quantos passos
x = np.linspace(0,7,num=5)
y = x/2
##########################################################
plt.figure(1)
#qual figura sera o grafico
plt.subplot(2,1,2)
#posicao do grafico na figura
plt.title("teste 2")
#escreve o titulo do grafico
plt.text(2.05,2,'escrito')
#escreve um texto no grafico(x,y,string)
plt.plot(2,2.5,'ro')
plt.plot((1,2,3,4),(1,4,9,16),'r:')
#gera o grafico na memoria/ ro circulos vermelhos
plt.ylabel(u'são mais numeros')
#coloca legenda em Y (u=usa acentos)
plt.xlabel('eixo x', fontsize='large', color='r')
##########################################################
plt.figure(1)
plt.subplot(2,1,1)
plt.title("teste 1")
plt.plot(x,y,c='#FFCC00', lw=3, marker='o', ms=12, mfc='r', mec='b', mew=3, drawstyle='steps-mid')
plt.axis((-1,10,-2,20))
#especifica os limites (x,x,y,y)
plt.grid(True)
#coloca grid no grafico
plt.ylabel(u'são numeros')
plt.xlabel('eixo x', fontsize='large', color='r')
##########################################################
plt.show()
#mostra a figura na tela
