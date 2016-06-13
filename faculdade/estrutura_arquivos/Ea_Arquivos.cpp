#include "Ea_Arquivos.h"
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

void abrir_arquivo(){
    char leitura, comparador='#';
    int conta_pipe=0, contador_tamanho=0;
    bool flag_de_comparacao = true;

    ifstream file;
    file.open("arquivo.txt");

    while(flag_de_comparacao == true){
        file.get(leitura);
        cout<<leitura;
        contador_tamanho ++;

        if (leitura == '|'){
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
}

void inserir(){
    ofstream file;

    string escrita;

    getline(cin, escrita);
    file.open("arquivo.txt");
    file << escrita<< endl;
    file.close();
}

void leitura();

void remover();
void conta_espaco();
void consulta();
void tempo();

