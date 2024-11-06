
##### ambiente de instalação do API
- faccamp.pythonanywhere.com
- user: faccamp
- modulo: hangman-api

##### esquema de projeto
- main.py -> dicionario.txt (endpoints: get e getfull)
- maindb.py -> dicionario.db (sqlite3) (endpoints: crud, get e getfull)

##### serviços disponíveis
- /hangman/crud
- /hangman/add/?/?/? (palavra,categoria,complexidade)
- /hangman/remove/? (by id)
- /hangman/getword
- /hangman/getword/? (by complexidade)
- /hangman/getdata
- /hangman/getdata/? (by complexidade)
- /hangman/getlist
- /hangman/getlist/? (by complexidade)

##### arquivos de projeto, teste
- main.py - main do api que manipula arquivo csv estatico (tipo sort get)
- maindb.py - main que manipula o dados de um banco sqlite (tipo sort get)
- dicionario.txt - lista de palavras tipo csv
- dicionario.db - banco de dados com a tabela de lista de palavras
- /templates/crud.html - pagina de gerenciamento de CRUD
- /projeto/dbsquema.py - script python para criacao e inserts iniciais do banco
- /test_curl-api - listagem de inserções CURL para teste da api

##### especificação de componentes
- Flask API: O componente central que recebe as requisições do usuário via HTTP. Ele interage com o banco de dados SQLite para recuperar ou armazenar informações.
- SQLite DB: O banco de dados que armazena as palavras, suas categorias e complexidades. A Flask API faz consultas (SELECT) e manipulação de dados (INSERT, DELETE).

##### pacotes python

pip install:

- flask
- jsonify
- requests
- beautifulsoup4

pip list - Package e Version
------------------------- ---------
- aniso8601                 9.0.1
- attrs                     24.2.0
- beautifulsoup4            4.12.3
- blinker                   1.8.2
- certifi                   2024.8.30
- charset-normalizer        3.4.0
- click                     8.1.7
- flask                     3.0.3
- idna                      3.10
- importlib-metadata        8.5.0
- itsdangerous              2.2.0
- jinja2                    3.1.4
- jsonify                   0.5
- jsonschema                4.23.0
- jsonschema-specifications 2024.10.1
- MarkupSafe                3.0.2
- pip                       20.3.4
- pkg-resources             0.0.0
- pytz                      2024.2
- referencing               0.35.1
- requests                  2.32.3
- rpds-py                   0.20.1
- setuptools                44.1.1
- six                       1.16.0
- soupsieve                 2.6
- urllib3                   2.2.3
- werkzeug                  3.1.0
- zipp                      3.20.2
