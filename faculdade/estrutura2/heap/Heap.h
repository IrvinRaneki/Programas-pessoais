typedef char ItemType;

class Heap
{ 
 public:
  Heap(int); // recebe o numero maximo de elementos e inicializa uma
	     // heap vazia.

  // Escreva de forma eficiente.
  Heap(int, ItemType*, int); // recebe o numero maximo de elementos,
                             // um array de elementos ItemType e um
                             // inteiro dizendo o numero de elementos
                             // nesse array. Perceba que o primeiro
                             // inteiro eh sempre maior ou igual ao
                             // ultimo.
   
  ~Heap();

  bool isEmpty() const;
  bool isFull() const;

  void enqueue(ItemType newItem);
  ItemType dequeue();

 private:
  int maxItems; // Numero maximo de elementos que podem ser alocados
		// na nossa Heap.
  int length;   // Armazena o quanto do nosso array interno estah
	        // realmente preenchido.
  ItemType* items; // Ponteiro para uma regiao de memoria. Neste caso,
		   // nos queremos que o array seja alocado
		   // dinamicamente.

  // Voce deve passar como parametro o indice do elemento que
  // possivelmente esta fora de ordem.
  void descida(int);
  void subida(int);
};

