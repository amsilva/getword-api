from flask import Flask, jsonify
import sqlite3
import random

# Nome do banco de dados SQLite
db_name = 'dicionario.db'


app = Flask(__name__)

def open_localdicionario(c):
    dados = []

    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Executar uma consulta SQL para buscar as palavras da tabela
    cursor.execute("SELECT complexidade, categoria, palavra FROM dicionario WHERE complexidade=?", (c,))
    rows = cursor.fetchall()

    for row in rows:
        complexidade, categoria, palavra = row
        dados.append({'complexidade': complexidade, 'categoria': categoria, 'palavra': palavra})

    # Fechar a conexão com o banco
    conn.close()

    return dados

def sortword(cat) :
    dicionario = open_localdicionario(cat)  # Consultar dicionário no banco de dados
    if dicionario:  # Verificar se a lista de palavras não está vazia
        pos = random.randint(0, len(dicionario) - 1)
        palavra_sorteada = dicionario[pos]
        return palavra_sorteada
    else:
        return None  # Caso não haja palavras no banco

@app.route('/wlist/get', methods=['GET'])
def get_simple_message():
    # Sugerir uma complexidade qualquer (exemplo: 1)
    novapalavra = sortword(1)
    if novapalavra:
        return jsonify(palavra=novapalavra['palavra'])
    else:
        return jsonify(message="Nenhuma palavra encontrada para a complexidade solicitada."), 404

@app.route('/wlist/getfull', methods=['GET'])
def get_complex_message():
    novapalavra = sortword(1)
    return jsonify(palavra=novapalavra['palavra'], 
                categoria=novapalavra['categoria'],
                complexidade=novapalavra['complexidade'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)