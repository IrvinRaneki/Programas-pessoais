#include "LinkedStack.h"
#include <iostream>

int main() {
  // Untemplated queue of char
  // Templated stack
  using namespace std;
  char character;
  GenericStack stack;
  char stackChar;
  cout << "Enter a string; press return." << endl;
  cin.get(character);
  while (character != '\n')
    {
      stack.push(character);
      cin.get(character);
    }
  while (!stack.isEmpty())
    {
      stackChar = stack.pop();
      cout << stackChar;
    }
  cout << endl;
}
