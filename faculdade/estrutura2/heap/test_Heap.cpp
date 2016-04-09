#include "Heap.h"
#include <iostream>

int main() {
  // Untemplated queue of char
  // Templated heap
  using namespace std;
  char character;
  Heap heap1(100);
  char heapChar;
  cout << "Enter several numbers; press return." << endl;
  cin.get(character);
  while (character != '\n')
    {
      heap1.enqueue(character);
      cin.get(character);
    }
  while (!heap1.isEmpty())
    {
      heapChar = heap1.dequeue();
      cout << heapChar;
    }
  cout << "\n";
  

  char* characters   = new char[100];
  int count = 0;

  cout << "Enter several numbers again; press return." << endl;
  cin.get(character); 
  while (character != '\n')
    {
      characters[count] = character;
      cin.get(character);
      count++;
    }

  Heap heap2(100, characters, count);
  while (!heap2.isEmpty())
    {
      heapChar = heap2.dequeue();
      cout << heapChar;
    }


  cout << endl;
}
