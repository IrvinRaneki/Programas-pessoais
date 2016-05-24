#include "AVLSearchTree.h"


int main() {
  // Untemplated queue of char
  // Templated heap
  using namespace std;
  int       character;
  AVLSearchTree tree;


  cout << "Insira um numero e pressione enter." << endl;
  cin  >> character;
  while (character != -1)
    {
      tree.insertItem(character);
      tree.printTree();
      cout << endl;
      cin  >> character;
    }

  cout << endl;
  cout << "Insira alguns characteres para remover" << endl;

  cin  >> character;
  while (character != -1)
    {
      tree.deleteItem(character);
      tree.printTree();
      cout << endl;
      cin  >> character;
    }
  cout << endl;
}
