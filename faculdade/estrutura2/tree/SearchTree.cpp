#include "SearchTree.h"
bool SearchTree::isEmpty() const{
  return root==NULL;
}
////////////////////////////////////////////
void SearchTree::deleteItem(Node*& tree, ItemType item){
  Node *location;
  location = new Node;
  location = tree;
  if (isEmpty()){
    tree = NULL;
  }
  else{
    if(item!= location->label){
      if (item < location->label){
        location = location->esquerda;
        deleteItem(location, item);
      }
      else{
        location = location->direita;
        deleteItem(location, item);
      }
    }
    else{
      deleteNode(location);
    }
  }
}
////////////////////////////////////////////
void SearchTree::insertItem(Node*& tree, ItemType item){
  if (tree == NULL){
    tree = new Node;
    tree->label = item;
  } else{
    if(item <= tree->label){
      insertItem(tree->esquerda, item);
    } else{
      insertItem(tree->direita, item);
      }
    }
}
///////////////////////////////////////////
void SearchTree::destroyTree(Node*& tree){
  if (tree != NULL){
    destroyTree(tree->esquerda);
    destroyTree(tree->direita);
    deleteNode(tree);
  }
}
///////////////////////////////////////////
void SearchTree::deleteNode(Node*& tree){
  if (tree->esquerda == NULL && tree->direita == NULL){ // se eh folha
    delete tree;
  }
  else{
    getSuccessor(tree, tree->label);
  }
}
///////////////////////////////////////////
void SearchTree::getSuccessor(Node* tree, ItemType& data){
  Node *location, *temp;
  temp = new Node;
  location = new Node;
  location = tree;

  bool flag;
  if (location->direita!=NULL){
    location = location->direita;
  }
  while (location->esquerda != NULL) {
    temp = location;
    location = location->esquerda;
  }
  retrieveItem(tree, location->label, flag);
  deleteItem(location,location->label);
}
///////////////////////////////////////////
void SearchTree::retrieveItem(Node* tree, ItemType& item, bool& found) const{
  tree->label = item;
}
///////////////////////////////////////////
void SearchTree::printPreOrder(Node* tree)  const{
  if (tree != NULL){
    std::cout << tree->label;
    printPreOrder(tree->esquerda);
    printPreOrder(tree->direita);
  }
}
///////////////////////////////////////////
void SearchTree::printInOrder(Node* tree)   const{
  if (tree != NULL){
    printInOrder(tree->esquerda);
    std::cout << tree->label;
    printInOrder(tree->direita);
  }
}
///////////////////////////////////////////
void SearchTree::printPostOrder(Node* tree) const{
  if (tree != NULL){
    printPostOrder(tree->esquerda);
    printPostOrder(tree->direita);
    std::cout << tree->label;
  }
}
