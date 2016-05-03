#include "LinkedStack.h"
#include <cstddef>
#include <new>

GenericStack::GenericStack(){
  topPtr = NULL;
}

GenericStack::~GenericStack(){
  NodeType* tempPtr;
  while (topPtr != NULL) {
    tempPtr = topPtr;
    topPtr  = topPtr -> next;
    delete tempPtr;
  }
}

void GenericStack::push(ItemType item){
  if (not isFull()){
    NodeType* location;
    location = new NodeType;
    location->info = item;
    location->next = topPtr;
    topPtr         = location;
  }
}

ItemType GenericStack::pop(){
  if (isEmpty()) {
    return '0';
  } else {
    NodeType* tempPtr;
    tempPtr = topPtr;
    ItemType item = topPtr->info;
    topPtr        = topPtr->next;
    delete tempPtr;
    return item;
  }
}

bool GenericStack::isEmpty() const {
  return (topPtr == NULL);
}

bool GenericStack::isFull() const {
  NodeType* location;
  try {
    location = new NodeType;
    delete location;
    return false;
  } catch(std::bad_alloc exception){
    return true;
  }
}
