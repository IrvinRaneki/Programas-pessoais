#!usr/bin/python
# -*- coding:utf-8 -*-
import Tkinter
from Tkinter import *
import ttk

class Packing(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Cadastro FCA")
		
		L1 = Label(self.parent, text="Nome").pack()
		Nome=Entry(self.parent).pack()

		L2 = Label(self.parent, text="RA").pack()
		RA=Entry(self.parent).pack()

		L3 = Label(self.parent, text="Email").pack()
		Email=Entry(self.parent).pack()
	
		self.Motivo_value = StringVar()
		L4 = Label(self.parent, text="Motivo").pack()
		Motivo=ttk.Combobox(self.parent, textvariable = self.Motivo_value,values=['Agendamento Medico', 'Disciplina', \
		'Estagio / Bolsa', 'Eventos Academicos', 'Movimento Estudantil', 'Eventos Culturais', 'Funcionarios - Reuniao de Trabalho', 'Outros']).pack()
		

		a = IntVar()
        	ida_chk=Checkbutton(self.parent,text="Ida",variable=a).pack()
		b = IntVar()
        	volta_chk=Checkbutton(self.parent,text="Volta",variable=b).pack()
		
		L5 = Label(self.parent, text="Mes(1 a 12)").pack()
		Data=Entry(self.parent).pack()
		
		btn1 = Button(self.parent, text="Iniciar Cadastro", command=self.initCadastro).pack()
		btn2 = Button(self.parent, text="Sair", command=self.onExit).pack()

	def onExit(self):
	        self.parent.quit()

	def initCadastro(self):
		print self.Motivo_value.get()


def main():
	root = Tk()
	root.geometry("350x350")
	tela=Packing(root)
	root.mainloop()

if __name__=='__main__':
	main()
