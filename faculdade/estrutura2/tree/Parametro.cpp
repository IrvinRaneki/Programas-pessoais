#include <iostream>

using namespace std;

void pass_by_value(int* p)
{
  // Alocaremos uma nova regiao de memoria e colocaremos o endereco em
  // p. Fora dessa funcao, o parametro continuara apontando para o
  // endereco antigo.
  p = new int;
  *p = 7;
}

void pass_by_value_and_changing_pointed_location(int* p)
{
  // Nao estamos alocando memoria, estamos apenas alterando o inteiro
  // que estah na posicao de memoria para onde p esta apontando.
  *p = 8;
}

void pass_by_reference(int*& p)
{
  // Alocaremos uma nova regiao de memoria e colocaremos o endereco em
  // p. Como o parametro foi passado por referencia, fora da funcao o
  // ponteiro apontara para a nova posicao que foi alocada dentro
  // desta funcao.
  p = new int;
  *p = 9;
}

int main()
{
  int a  = 1;
  int b  = 2;
  int c  = 3;

  int* p1 = &a;
  int* p2 = &b;
  int *p3 = &c;

  cout << "Enderecos Antes:  "<<  p1 << "  " <<  p2 << "  "  <<  p3 << endl;
  cout << "Valores   Antes:  "<< *p1 << "  " << *p2 << "  "  << *p3 << endl;
  cout << endl;

  pass_by_value(p1); //Observe que nao podemos alterar o ponteiro
		     //propriamente dito.
  pass_by_value_and_changing_pointed_location(p2); //Observe que
						  //podemos alterar a
						  //posicao de memoria
						  //para onde o
						  //ponteiro aponta.
  pass_by_reference(p3);  // Observe que aqui nos podemos alterar o
			  // proprio ponteiro.

  cout << "Enderecos Depois: "<<  p1 << "  " <<  p2 << "  "  <<  p3 << endl;
  cout << "Valores   Depois: "<< *p1 << "  " << *p2 << "  "  << *p3 << endl;

  return 0;
}
