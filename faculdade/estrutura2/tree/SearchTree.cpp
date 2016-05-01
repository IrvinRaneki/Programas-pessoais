#include "SearchTree.h"
#include <cstddef>
#include <iostream>
#include <new>

bool SearchTree::isFull() const {
  return (root == NULL);
}
bool SearchTree::isEmpty() const {
  return (root == NULL);
}

void SearchTree::insertItem(Node*& tree, ItemType item){
  if(isEmpty()){
    Node* location;
    location = new Node;
    location->label = item;
    location->esquerda = NULL;
    location->direita = NULL;
  }
}
