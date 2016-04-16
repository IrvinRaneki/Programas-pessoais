#include "LinkedQueue.h"
#include <cstddef>
#include <new>

GenericQueue::GenericQueue(){
  front = NULL;
  rear  = NULL;
}

GenericQueue::~GenericQueue(){
  NodeType* tempPtr;
  NodeType* tempPtr2;
  while (front != NULL) {
    tempPtr = front;
    front = front -> next;
    tempPtr2 = rear;
    rear = rear -> next;
    delete tempPtr;
    delete tempPtr2;
  }
}

void GenericQueue::enqueue(ItemType item){
  if (not isFull()){
    NodeType* location;
    location = new NodeType;
    location->info = item;
    location->next = NULL;

    if (isEmpty()){
      front = location;
      rear  = location;
    }
    else{
      rear->next = location;
      rear = location;
    }
  }
}

ItemType GenericQueue::dequeue(){
  if (isEmpty()){
    return '0';
  }
  else {
    if (front->next==NULL){
      ItemType item = front->info;
      front = NULL;
      rear  = NULL;
      return item;    
    }
    else{
      ItemType item = front->info;
      front = front->next;
      return item;
    }
  }
}

bool GenericQueue::isEmpty() const {
  return (front == NULL);
}

bool GenericQueue::isFull() const {
  NodeType* location;
  try {
    location = new NodeType;
    delete location;
    return false;
  } catch(std::bad_alloc exception){
    return true;
  }
}
