typedef char ItemType;

// Estrutura usada para guardar a informacao e o endereco do proximo
// elemento.
struct NodeType
{
  ItemType info;
  NodeType* next;
};

class GenericStack
{
 public:
  // Constructor
  GenericStack();

  // Destructor: Esta funcao serah chamada quando alguem usar o delete
  // neste objeto. Neste caso, serah preciso desalocar todas as
  // regioes de memoria que alocamos dinamicamente.
  ~GenericStack();
  void push(ItemType);
  ItemType pop();
  
  bool isEmpty() const;
  bool isFull() const;

 private:
  NodeType* topPtr;
};
