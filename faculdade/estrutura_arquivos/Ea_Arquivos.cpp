#include "Ea_Arquivos.h"
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

void Ea_Arquivos::cria_lista(Nodetype *&No, char nome){
  if (No == NULL){
    No = new Nodetype;
    No->info = nome;
  } else{
      cria_lista(No->next, nome);
    }
}

void Ea_Arquivos::abrir_arquivo(){
    char leitura, comparador='#';
    int conta_pipe=0, contador_tamanho=0;
    bool flag_de_comparacao = true;

    Ea_Arquivos();
    
    ifstream file;
    file.open("arquivo.txt");

    while(flag_de_comparacao == true){
        file.get(leitura);
        cout<<leitura;
        contador_tamanho ++;
	
	cria_lista(root, leitura);

        if (leitura == '|'){
	    cria_lista(root, leitura);
            conta_pipe ++;
            cout<<endl;
        }
        if (leitura==comparador){
            flag_de_comparacao = false;
        }
    }
    cout<<endl;
    cout<<endl;
    cout<<conta_pipe<<endl;
    cout<<contador_tamanho<<endl;
    file.close();
    printatudo(root);
}

void Ea_Arquivos::inserir(){
    ofstream file;

    string escrita;

    getline(cin, escrita);
    file.open("arquivo.txt");
    file << escrita<< endl;
    file.close();
}

void Ea_Arquivos::leitura(){}

void Ea_Arquivos::remover(){}
void Ea_Arquivos::conta_espaco(){}
void Ea_Arquivos::consulta(){}
void Ea_Arquivos::tempo(){}

void Ea_Arquivos::printatudo(Nodetype *No){
      std::cout << No->info;
      printatudo(No->next);
}

