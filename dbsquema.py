import sqlite3

# Nome do banco de dados SQLite
db_name = 'dicionario.db'

# Criar a tabela dicionario
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS dicionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    complexidade INTEGER,
    categoria TEXT,
    palavra TEXT
);
''')

# Inserir dados de exemplo
cursor.executemany('''
INSERT INTO dicionario (complexidade, categoria, palavra) 
VALUES (?, ?, ?)
''', [
    (1, 'ANIMAL', 'CAVALO'),
    (1, 'FRUTA', 'BANANA'),
    (1, 'ANIMAL', 'CAMELO'),
    (1, 'FRUTA', 'GOIABA'),
    (1, 'PAIS', 'BRASIL'),
    (1, 'PAIS', 'PORTUGAL'),
    (2, 'FRUTA', 'KIWI'),
    (2, 'PAIS', 'HOLANDA')
])

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()
