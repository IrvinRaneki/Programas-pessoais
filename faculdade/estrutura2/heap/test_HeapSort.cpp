#include <iostream>
#include "HeapSort.h"

using namespace std;

ostream& operator<<(ostream& os, const HeapSort& array){
  for (int i = 0; i < array.length; i++) {
    os << array.items[i];
  }
  os << endl;
  return os;
}

int main() {
  // Untemplated queue of char
  // Templated heap
  using namespace std;
  char character;
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

  HeapSort heap(100, characters, count);

  cout << heap;
  heap.sort();
  cout << heap;
  
}
