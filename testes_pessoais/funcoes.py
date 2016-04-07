#!/python/bin/python
    #import math
    #def -> abre uma funcao
    #def contagem(numero):
    #    for i in range(0,numero+1):
    #        print('',i)
    #
    #a = int(input(''))#cast in int-input trabalhar como numero
    #contagem(a)
    #print(math.factorial(a))
    ##########################################333
    #def add_nome():
    #    nome=input("nome: ",)
    #    escrever=open('/home/estagiario/svn_irvin/teste','a')
    #    escrever.write(nome+"\n")
    #    escrever.close()
    #def criar():
    #    criar = open('/home/estagiario/svn_irvin/teste','w')
    #    criar.close()
    #def le_arq(arq):
    #    leitura=open(arq,'r')
    #    ler=leitura.readlines()
    #    print(ler)
    #criar()
    #add_nome()
    #le_arq('/home/estagiario/svn_irvin/teste')
    #############################################333

import sqlite3
#conn=sqlite3.connect('/home/estagiario/svn_irvin/impl/database/trunk/src/EnbDb.flash')
#cursor=conn.cursor()

#cursor.execute('SELECT szHwBasebandBoard FROM EnbInventory;')
#print cursor.fetchall()
#cursor.execute('SELECT * FROM EnbPhyPrach;')
#print('',cursor.fetchall())
#conn.close()


update=sqlite3.connect('/home/estagiario/svn_irvin/impl/database/trunk/src/EnbDb.flash')
cur=update.cursor()
valor = int(input('novo valor: '))
cur.execute('UPDATE  EnbInventory SET liLastSwUpgradeTime = ',(valor))
