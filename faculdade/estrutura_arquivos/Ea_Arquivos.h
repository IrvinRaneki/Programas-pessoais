#include <cstddef>

struct Nodetype
{
    char info;
    Nodetype *next;
};


class Ea_Arquivos
{
 public:
  Ea_Arquivos() { root = NULL;}

  ~Ea_Arquivos(){}


  void cria_lista(Nodetype *& No, char nome);

  void abrir_arquivo();


  void leitura();
  void inserir();
  void remover();
  void conta_espaco();
  void consulta();
  void tempo();
  void printatudo(Nodetype *No);
  Nodetype* root;
  
};