#include "GenericArray.h"

#include <algorithm>
#include <vector>
using namespace std;


GenericArray::GenericArray(){
  length = 0;
}

bool GenericArray::isFull() const {
  return (length == MAX_ITEMS);
}

int GenericArray::getLength() const {
  return length;
}

int GenericArray::retrieveItem(int& item, bool& found){
  /*int location = 0;

  while ((location<length)&& !found) {
    if(item == info[location]){
      found = true;
      item = info[location];
    }
    location = location+1;
  }*/

  found = false;

  int e, meio, location;

  e = -1; location = length;

  while ((e < location-1)&&!found) {
    meio = (e + location)/2;
    if (info[meio] < item) e = meio;
    else location = meio;
    if (item==info[meio]){
      found=true;
    }
  }
  return location;
}

void GenericArray::insertItem(int item){
  if (length==MAX_ITEMS){
    throw string("lista cheia");
  }
  else{
    info[length]=item;
    length++;
  }
  std::vector <int> myvector (info, info+length);
  std::sort (myvector.begin(), myvector.end());
  for(int i = 0; i < myvector.size(); i++){
    info[i]=myvector[i];
  }
}

void GenericArray::deleteItem(int item, bool found, int location){

  if (found !=false){
    for(int i = location; i<length; i++){
      info[i]=info[i+1];
    }
    length--;
  }
  else{
    std::cout << "item nao encontrado" << std::endl;
  }
}
