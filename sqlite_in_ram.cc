#include <iostream>
#include <sqlite3.h>
#include <list>

sqlite3 *load_in_memory(const char *file_name){
  sqlite3 *file_db = NULL;
  sqlite3 *mem_db = NULL;
  sqlite3_backup *backup = NULL;
  char *err_msg;

  if(sqlite3_open(file_name, &file_db) != SQLITE_OK){
    std::cerr << "Cannot open '" << file_name << "' database" << std::endl;

    return NULL;
  }

  if (sqlite3_open(":memory:", &mem_db) != SQLITE_OK) {
    std::cerr << "Cannot open memory database" << std::endl;

    sqlite3_close(mem_db);

    return NULL;
  }


  backup = sqlite3_backup_init(mem_db, "main", file_db, "main");
  if(backup){
    sqlite3_backup_step(backup, -1);
    sqlite3_backup_finish(backup);
  } else {
    return NULL;
  }

  sqlite3_close(file_db);

  return mem_db;
}
/////////////////////////////////////////////////////////////////////////////////////////////
std::list<std::string> tables;

int table_name_callback(void *not_used, int argc, char **argv,
	     char **col_name) {

  for(int i=0; i<argc; i++) {
    tables.push_back(argv[i]);
  }

  return 0;
}

int table_data_callback(void *table_name, int argc, char **argv,
	     char **col_name) {

  for(int32_t i=0; i<argc; i++) {
    std::cout << col_name[i] << "=" << (argv[i] == NULL ? "<empty>" : argv[i]) << std::endl;
  }
  return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////////
int main(int argc, char *argv[]) {
  sqlite3 *db = load_in_memory("/tmp/lte/database/EnbDb.flash");
  char *err_msg;

  if(sqlite3_exec(db, "SELECT name FROM sqlite_master WHERE type='table'", table_name_callback, NULL, &err_msg) != SQLITE_OK) {
    sqlite3_free(err_msg);
    sqlite3_close(db);

    return 1;
  }

  for(auto it=tables.begin(); it != tables.end(); ++it) {
    if(sqlite3_exec(db, ("SELECT * FROM "+(*it)).c_str(), table_data_callback, NULL, &err_msg) != SQLITE_OK) {
      sqlite3_free(err_msg);
      sqlite3_close(db);

      return 1;
    }
  }

  sqlite3_close(db);
  return 0;
}
