#include <iostream>

const int MAX_ITEMS = 6;
const int MAX_ITEMS2 = MAX_ITEMS*2;
;

// Percebam que nenhuma das operacoes da nossa lista depende de
// informacoes especificas sobre o objeto ItemType. Essa independencia
// logica eh o que chamamos de abstracao.

class GenericArray {
 public:

  // Constructor
  GenericArray(); // Inicializa o nosso objeto com uma lista vazia.

  // Observers
  bool isFull() const;
  int  getLength() const;

  // Recebe um ponteiro para um elemento do tipo int. Esse
  // elemento int que recebemos por parametro tem uma
  // chave. Usamos essa chave para buscar um elemento em nossa lista e
  // retornar esse elemento, caso ele exista.

  // Se o elemento nao estiver na lista, entao nao precisa alterar o
  // parametro item, basta avisar na variavel found que o elemento nao
  // foi achado.
  int retrieveItem(int& item, bool& found);

  // Insere o elemento na lista em uma posicao arbitraria no caso do
  // Unsorted e na posicao correta no caso do Sorted.
  void insertItem(int item);

  // Remove uma ocorrencia do elemento na lista.
  void deleteItem(int item, bool found, int location); // Nos nao sabemos qual a chave da
				  // classe int, entao precisamos
				  // de um objeto para saber se os
				  // elementos listados sao iguais ao
				  // nosso.

  friend std::ostream& operator<<(std::ostream& os, const GenericArray& st);

 private:
  int length;
  int info[MAX_ITEMS];
};
