#########=====servpy=====##########
#!/user/bin/python
import socket

import matplotlib.pyplot as plt
import time
from collections import deque
import numpy as np

##################################################################
#                          plota grafico                         #
##################################################################
def plota_graf(addr, num):
    a1 = deque([0]*100)
    ax = plt.axes(xlim=(0, 100), ylim=(0, 10))
    d = conect(addr, num)

    line, = plt.plot(a1)
    plt.ion()
    plt.ylim([-15,15])
    plt.show()
    while num != 'exit':
        a1.appendleft(next(d))
        datatoplot = a1.pop()
        line.set_ydata(a1)
        plt.draw()
        print 'recebido: ',a1[0]
        #time.sleep(0.1)
        #plt.pause(0.005)

##################################################################
#             funcao conect: aguarda o recebimento da msg        #
##################################################################
def conect(addr, recebe):
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #->mecanismos de recepcao de conexao - argv[1-familia do protocolo() 2-tipo de envio(tcp/ip)]
    serv_socket.bind(addr)
    #->mostra qual o ip e porta o servidor devem aguardar a conexao
    while recebe!='exit':
        recebe, cliente = serv_socket.recvfrom(1024)
        #->apos conexao ha o aguardo de dado enviado pela rede de ate 1024 Bytes (1 argv -> tamanho do buffer)
        #print "mensagem recebida: "+ recebe
        if recebe != 'exit':
            yield recebe
    serv_socket.close()

##################################################################
#                           funcao main                          #
##################################################################
def main():
    recebe=''
    host = ''
    port = 8888
    addr = (host, port)

    plota_graf(addr, recebe)

if __name__ == '__main__':
    main()
