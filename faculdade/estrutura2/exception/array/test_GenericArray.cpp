#include <iostream>
#include "GenericArray.h"

using namespace std;


ostream& operator<<(ostream& os, const GenericArray& array){
  for (int i = 0; i < array.length; i++) {
    os << array.info[i];
  }
  os << endl;
  return os;
}

int main(){
  GenericArray unsorted;

  int elements[6] = {5, 7, 6, 9, 3, 4};

  for (int i = 0; i <= 6; i++) {
    try{
      int item(elements[i]);
      unsorted.insertItem(item);
    }
    catch(string &message){
      cout << "error:"<<message<< endl;
    }
  }

  cout << unsorted;

  int item(4);
  bool     found = false;
  int location =0;


  location = unsorted.retrieveItem(item, found);
  cout << item << endl;

  unsorted.deleteItem(item, found, location);
  cout << unsorted;
  cout << "Fim" << endl;

}
