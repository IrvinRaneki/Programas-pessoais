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
      try{
        stack.push(character);
      } catch(FullStack &){
        cout << "stack is full" << endl;
      }
      cin.get(character);
    }

  while (!stack.isEmpty())
    {
      try{
        stackChar = stack.pop();
      } catch(EmpytStack &){
        cout << "stack is Empyt" << endl;
      }
      cout << stackChar;
    }
  cout << endl;
}
