#!/bin/python2

novalista=[1,2,3]
lista=[0,1,2,3]

novonome = raw_input("Digite o novo nome:")#somente input = string
print ('ola', novonome)
sobrenome=raw_input("agora o segundo nome:")
print((novonome+' '+sobrenome+'\n')*10)
print(type(novonome))#tudo que quiser imprimir print(comando)

print(len(lista))
print('')

for i in range(0,len(lista)):#(de, ate antes de)
    print(lista[i])

lista.append(input("novo numero"))#append adiciona um item ao final da lista

for i in range(0,len(lista)):#(de, ate antes de)
    print(lista[i])

for i in range(0,len(novalista)):
    novalista[i]=input("numero:")

novalista.extend(lista)#extend adiciona uma lista ao final da lista existente

for i in range(0,len(novalista)):#(de, ate antes de)
    print(novalista[i])
print('')
del novalista[5]#na verdade estah excluindo o sexto numero pois comeca de 0
for i in range(0,len(novalista)):
    print(novalista[i])
print("o tamanho da lista: ",len(novalista))

while len(novalista)<10:
    novalista.append(input("numero: "))

print tuple(novalista)
