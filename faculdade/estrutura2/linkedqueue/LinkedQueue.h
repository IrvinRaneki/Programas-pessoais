typedef char ItemType;

// Estrutura usada para guardar a informacao e o endereco do proximo
// elemento.
struct NodeType
{
  ItemType info;
  NodeType* next;
};



class GenericQueue
{ 
 public:

  GenericQueue();
  ~GenericQueue();
  void     enqueue(ItemType);
  ItemType dequeue();
  
  bool     isEmpty() const;
  bool     isFull() const;

 private:
  NodeType* front;
  NodeType* rear;
};
