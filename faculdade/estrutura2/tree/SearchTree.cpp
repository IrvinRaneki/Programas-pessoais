#include "SearchTree.h"

bool SearchTree::isEmpty() const{
  return root==NULL;
}
////////////////////////////////////////////
void SearchTree::deleteItem(Node*& tree, ItemType item){
  if (isEmpty()){
    tree = NULL;
  }
  else{
    if (item < tree->label){
      deleteItem(tree->esquerda, item);
    }
    if (item > tree->label){
      deleteItem(tree->direita, item);
    }
    else{
      deleteNode(tree);
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

}
///////////////////////////////////////////
void SearchTree::deleteNode(Node*& tree){
  if (tree->esquerda == NULL && tree->direita == NULL){ // se eh folha
    delete tree;
  }
  else{

  }
}
///////////////////////////////////////////
void SearchTree::getSuccessor(Node* tree, ItemType& data){
  Node *location;
  location = new Node;
  location = tree->direita;
  while (location->esquerda != NULL) {
    location = location->esquerda;
  }
  retrieveItem(location, location->label);
  delete location;
}
///////////////////////////////////////////
void SearchTree::retrieveItem(Node* tree, ItemType& item, bool& found) const{

}
