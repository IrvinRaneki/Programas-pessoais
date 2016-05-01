#include "SearchTree.h"


int main() {
  // Untemplated queue of char
  // Templated heap
  using namespace std;
  char       character;
  SearchTree tree;

  cout << "Insira um monte de characteres." << endl;

  cin.get(character);
  while (character != '\n')
    {
      tree.insertItem(character);
      cin.get(character);
    }
  tree.printTree();
  cout << endl;
  cout << "Insira alguns characteres para remover" << endl;

  cin.get(character);
  while (character != '\n')
    {
      tree.deleteItem(character);
      cin.get(character);
    }
  tree.printTree();

  cout << endl;
}
