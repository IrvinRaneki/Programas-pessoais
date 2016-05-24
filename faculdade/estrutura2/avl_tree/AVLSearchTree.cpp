#include "AVLSearchTree.h"

bool AVLSearchTree::isEmpty() const{
  return root==NULL;
}

bool AVLSearchTree::isFull() const{
  //teste
}

void AVLSearchTree::destroyTree(Node*& tree){
  if (tree != NULL){
    destroyTree(tree->esquerda);
    destroyTree(tree->direita);
    //deleteNode(tree);
  }
}

void AVLSearchTree::retrieveItem(Node* tree, ItemType& item, bool& found) const{
  tree->label = item;
}

void AVLSearchTree::getSuccessor(Node* tree, ItemType& data){
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
  //deleteItem(location,location->label);
}

void AVLSearchTree::printPreOrder(Node* tree)  const{
  if (tree != NULL){
    std::cout << tree->label << "[" << tree->fatorB << "] ";
    printPreOrder(tree->esquerda);
    printPreOrder(tree->direita);
  }
}

void AVLSearchTree::printInOrder(Node* tree)   const{
  if (tree != NULL){
    printInOrder(tree->esquerda);
    std::cout << tree->label << "[" << tree->fatorB << "] ";
    printInOrder(tree->direita);
  }
}

void AVLSearchTree::printPostOrder(Node* tree) const{
  if (tree != NULL){
    printPostOrder(tree->esquerda);
    printPostOrder(tree->direita);
    std::cout << tree->label << "[" << tree->fatorB << "] ";
  }
}

void AVLSearchTree::insertItem(Node*& tree, ItemType item, bool& isTaller){
  if(tree==NULL){
    tree = new Node;
    tree->label = item;
  } else{
    if(item<=tree->label){
      insertItem(tree->esquerda, item, isTaller);
    } else{
      insertItem(tree->direita, item, isTaller);
    }
  }
}

void AVLSearchTree::deleteItem(Node*& tree, ItemType item, bool& isShorter){
  Node *location;
  location=new Node;
  location=tree;
  if (isEmpty()){
    tree = NULL;
  } else{
    if(item!= location->label){
      if(item<location->label){
        location = location->esquerda;
        deleteItem(location, item, isShorter);
      } else{
        location = location->direita;
        deleteItem(location, item, isShorter);
      }
    } else{
      deleteNode(location, isShorter);
    }
  }
}

void AVLSearchTree::deleteNode(Node*& tree, bool& isShorter){
  if(tree->esquerda == NULL && tree->direita == NULL){
    delete tree;
  } else{
    if(tree->esquerda == NULL && tree->direita != NULL){
      tree=tree->direita;
    }
    if(tree->esquerda != NULL && tree->direita == NULL){
      tree=tree->esquerda;
    }
  }
}

////////////////////////////////////////////////////////////////////////////////////////

void AVLSearchTree::rotateToLeft(Node*& tree) const{}
void AVLSearchTree::rotateToRight(Node*& tree) const{}
void AVLSearchTree::rotateToLeftAndRight(Node*& tree) const{}
void AVLSearchTree::rotateToRightAndLeft(Node*& tree) const{}

void AVLSearchTree::performRotations(Node*& tree) const{}
