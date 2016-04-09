#include <iostream>

typedef char ItemType;

class HeapSort
{ 
 public:
  HeapSort(int); // recebe o numero maximo de elementos e inicializa uma
	     // heap vazia.

  // Escreva de forma eficiente.
  HeapSort(int, ItemType*, int); // recebe o numero maximo de elementos,
                             // um array de elementos ItemType e um
                             // inteiro dizendo o numero de elementos
                             // nesse array. Perceba que o primeiro
                             // inteiro eh sempre maior ou igual ao
                             // ultimo.

    
  ~HeapSort();

  bool isEmpty() const;
  bool isFull() const;

  void sort(); 

  void enqueue(ItemType newItem);
  ItemType dequeue();

  friend std::ostream& operator<<(std::ostream& os, const HeapSort& st);
  
 private:
  int maxItems; // Numero maximo de elementos que podem ser alocados
		// na nossa Heap.
  int length;   // Armazena o quanto do nosso array interno estah
	        // realmente preenchido.
  ItemType* items; // Ponteiro para uma regiao de memoria. Neste caso,
		   // nos queremos que o array seja alocado
		   // dinamicamente.

  // Duas alteracoes ocorreram aqui. Aqui nem toda o nosso array
  // precisa ser uma heap, apenas uma parte dele. Devemos entao
  // configurar o limite que tem que ser obedecido.
  void descida(int index, int bottom);
  void subida(int root, int index);
};

