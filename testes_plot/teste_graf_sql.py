import os
import sqlite3
import time
import sys
import matplotlib.pyplot as plt
import subprocess
x=[]
y=[]
cont = 0
##################################################################
#                funcao para conectar no BD                      #
##################################################################

def get_table_list(table_name):
        db_path = os.getenv('DATABASE_RAM_PATH')
        conn = sqlite3.connect( db_path + '/' + 'EnbDb.flash' )
        cur = conn.cursor()
        cur.execute('SELECT * FROM %s' % table_name )
        result = cur.fetchall()
        conn.close()
        return result
##################################################################
#             transformacao da string para um vetor int          #
##################################################################
string = get_table_list('*')
print string
#str1=str(string).replace("[(", "")
#str1=str(str1).replace(")]", "")
##retira os elementos da string
#str2=str(str1).split(', ')
####################################################################
##             utiliza o tamanho de str2 para criar y             #
###################################################################
#str3=range(len(str2))
##################################################################
#                       criacao do grafico                       #
##################################################################
#x=str3
#y=str2
#plt.plot(x,y,'r')
#plt.show()
