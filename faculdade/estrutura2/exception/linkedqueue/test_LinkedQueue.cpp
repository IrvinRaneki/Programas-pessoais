#include "LinkedQueue.h"
#include <iostream>

int main() {
  // Untemplated queue of char
  // Templated queue
  using namespace std;
  char character;
  GenericQueue queue;
  char queueChar;
  cout << "Enter a string; press return." << endl;
  cin.get(character);

  try{
    while (character != '\n')
    {
      queue.enqueue(character);
      cin.get(character);
    }
  } catch(FullQueue &){
    cout << "queue is full" << endl;
  }

  try{

    while (!queue.isEmpty())
    {
      queueChar = queue.dequeue();
      cout << queueChar;
    }
    cout << endl;
  } catch(EmptyQueue &){
    cout << "queue is Empty" << endl;
  }
}
