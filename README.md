
##### ambiente de instalação do API
faccamp.pythonanywhere.com
user: faccamp

##### esquema de projeto
- main.py -> dicionario.txt (endpoints: get e getfull)
- maindb.py -> dicionario.db (sqlite3) (endpoints: crud, get e getfull)

##### serviços disponíveis
- /wlist/crud 
- /wlist/get 
- /wlist/getfull


##### arquivos de projeto, teste
main.py - main do api que manipula arquivo csv estatico (tipo sort get)
maindb.py - main que manipula o dados de um banco sqlite (tipo sort get)
dicionario.txt - lista de palavras tipo csv
dicionario.db - banco de dados com a tabela de lista de palavras
dbsquema.py - script python para criacao e inserts iniciais do banco

##### especificação de componentes
Flask API: O componente central que recebe as requisições do usuário via HTTP. Ele interage com o banco de dados SQLite para recuperar ou armazenar informações.
GET /get: Endpoint que retorna uma palavra aleatória, como vimos em seu código.
GET /getfull: Endpoint que provavelmente retorna informações completas (como todas as palavras ou mais detalhes).
POST /crud: Endpoint que permite a criação de novas palavras no banco de dados.
GET /crud: Endpoint que exibe todas as palavras cadastradas.
GET /remove: Endpoint para remover palavras do banco de dados.
SQLite DB: O banco de dados que armazena as palavras, suas categorias e complexidades. A Flask API faz consultas (SELECT) e manipulação de dados (INSERT, DELETE).

