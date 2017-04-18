#!usr/bin/python
# -*- coding:utf-8 -*-

import cadastro_intercamp_FCA
import sys
import os

import Tkinter
from Tkinter import *
import ttk
import string

class Packing(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Cadastro FCA")

		L1 = Label(self.parent, text="Nome").pack()
		self.nameUser =StringVar()
		self.entryNome=StringVar(Entry(self.parent, textvariable = self.nameUser).pack())

		L11 = Label(self.parent, text="Sobrenome").pack()
		self.sobreNomeUser =StringVar()
		self.entrySobreNome=StringVar(Entry(self.parent, textvariable = self.sobreNomeUser).pack())

		L2 = Label(self.parent, text="RA").pack()
		self.raUser =StringVar()
		self.entryRA=Entry(self.parent, textvariable =self.raUser).pack()

		L3 = Label(self.parent, text="Email").pack()
		self.emailUser =StringVar()
		self.etryEmail =Entry(self.parent, textvariable =self.emailUser).pack()

		self.Motivo_value = StringVar()
		L4 = Label(self.parent, text="Motivo").pack()
		Motivo=ttk.Combobox(self.parent, textvariable = self.Motivo_value,values=['Agendamento_Medico', 'Disciplina', \
		'Bolsa_/_Estagio', 'Eventos_Academicos', 'Movimento_Estudantil', 'Eventos_Culturais', 'Funcionarios-Reuniao_de_Trabalho', 'Outros']).pack()

		self.a = IntVar()
		a_chk=Checkbutton(self.parent,text="Limeira-Campinas - 06:00",variable=self.a).pack()
		self.b = IntVar()
		b_chk=Checkbutton(self.parent,text="Limeira-Campinas - 07:30",variable=self.b).pack()
		self.c = IntVar()
		c_chk=Checkbutton(self.parent,text="Limeira-Campinas - 12:00",variable=self.c).pack()
		self.d = IntVar()
		d_chk=Checkbutton(self.parent,text="Campinas-Limeira - 13:15",variable=self.d).pack()
		self.e = IntVar()
		e_chk=Checkbutton(self.parent,text="Campinas-Limeira - 16:30",variable=self.e).pack()
		self.f = IntVar()
		f_chk=Checkbutton(self.parent,text="Campinas-Limeira - 18:00",variable=self.f).pack()
		self.g = IntVar()
		g_chk=Checkbutton(self.parent,text="Campinas-Limeira - 23:00",variable=self.g).pack()
		self.h = IntVar()
		h_chk=Checkbutton(self.parent,text="Limeira-Campinas - 23:00",variable=self.h).pack()

		L5 = Label(self.parent, text="Mes(1 a 12)").pack()
		Data=Entry(self.parent).pack()

		btn1 = Button(self.parent, text="Iniciar Cadastro", command=self.initCadastro).pack()
		btn2 = Button(self.parent, text="Sair", command=self.onExit).pack()

	def onExit(self):
	        self.parent.quit()

	def initCadastro(self):

		nameUser = self.nameUser.get()
		sobreNomeUser = self.sobreNomeUser.get()
		raUser =  self.raUser.get()
		emailUser =  self.emailUser.get()
		motivoUser =  self.Motivo_value.get()

		a = self.a.get()
		b = self.b.get()
		c = self.c.get()
		d = self.d.get()
		e = self.e.get()
		f = self.f.get()
		g = self.g.get()
		h = self.h.get()

		os.system("python2 cadastro_intercamp_FCA.py "
		+str(nameUser) + " " + str(sobreNomeUser) + " " + str(raUser) + " " + str(emailUser) + " "+ str(motivoUser) + " "
		+str(a)+ " " +str(b)+ " " +str(c)+ " " +str(d)+ " " +str(e)+ " " +str(f)+ " " +str(g)+ " " +str(h))

def main():
	root = Tk()
	root.geometry("400x450")
	tela=Packing(root)
	root.mainloop()

if __name__=='__main__':
	main()
