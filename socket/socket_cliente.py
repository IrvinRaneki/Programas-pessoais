############## client.py#################
#!/usr/bin/python
import socket
import random
import time
#ip = raw_input('digite o ip de conexao: ')
##################################################################
#                funcao para conectar e enviar                   #
##################################################################
def conect(addr, mensagem):
    val = 7
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #tipo de protocolo UDP - SOCK_DGRAM
    while mensagem != 'exit':
        val=random.randint(-10,10)

        mensagem = str(val)
        client_socket.sendto(mensagem,addr)
        time.sleep(0.005)
        #->faz envio de dado para o servidor
        print 'enviado: ',mensagem
    client_socket.close()
    #->fecha a conexao entre os app

##################################################################
#                           funcao main                          #
##################################################################
def main():
    mensagem=''
    port = 8080
    ip = "10.202.35.138"
    addr = ((ip,port))

    conect(addr, mensagem)

if __name__ == '__main__':
    main()
