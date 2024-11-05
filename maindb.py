from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import random
#import os

# Nome do banco de dados SQLite
db_name = 'dicionario.db'


app = Flask(__name__)

def recupera_dados(complex):
    dados = []

    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Executar uma consulta SQL para buscar as palavras da tabela
    #cursor.execute("SELECT complexidade, categoria, palavra FROM dicionario WHERE complexidade=?", (c,))
    cursor.execute("SELECT id, complexidade, categoria, palavra FROM dicionario")
    rows = cursor.fetchall()

    for row in rows:
        id, complexidade, categoria, palavra = row
        if complex == 0 or complex == complexidade : #para complex = 0, considera tudo
            dados.append({'id':id, 'complexidade': complexidade, 'categoria': categoria, 'palavra': palavra})

    # Fechar a conexão com o banco
    conn.close()

    return dados

def add_palavra(complexidade, categoria, palavra):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dicionario (complexidade, categoria, palavra) VALUES (?, ?, ?)",
                   (complexidade, categoria.upper(), palavra.upper()))
    conn.commit()
    conn.close()

def remove_palavra(id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dicionario WHERE id=?", (id,))
    conn.commit()
    conn.close()

@app.route('/wlist/crud', methods=['GET', 'POST'])
def crud():
    if request.method == 'POST':
        # Captura dos dados do formulário
        complexidade = request.form['complexidade']
        categoria = request.form['categoria']
        palavra = request.form['palavra']
        
        # Adiciona a nova palavra no banco de dados
        add_palavra(complexidade, categoria, palavra)
        return redirect(url_for('crud'))  # Redireciona para a mesma página após o POST
    
    # Quando for GET, exibe os dados no banco de dados
    palavras = recupera_dados(0)
    return render_template('crud.html', palavras=palavras)

# Rota para remover uma palavra
@app.route('/wlist/remove/<int:id>')
def remove(id):
    remove_palavra(id)
    return redirect(url_for('crud'))

# Rota para adicionar uma palavra
@app.route('/wlist/add/<string:pal>/<string:cat>/<int:compl>')
def add(pal,cat,compl):
    add_palavra(compl,cat,pal)
    return redirect(url_for('crud'))

def sortword(cat) : # TODO aplicar o filtro 'cat' nesse nivel
    dicionario = recupera_dados(cat)  # Consultar dicionário no banco de dados
    if dicionario:  # Verificar se a lista de palavras não está vazia
        pos = random.randint(0, len(dicionario) - 1)
        palavra_sorteada = dicionario[pos]
        return palavra_sorteada
    else:
        return None  # Caso não haja palavras no banco

@app.route('/wlist/get/<int:complex>', methods=['GET'])
def get_simple_bycomplex(complex):
    novapalavra = sortword(complex) #repassa a categoria
    if novapalavra:
        return jsonify(palavra=novapalavra['palavra'])
    else:
        return jsonify(message="Nenhuma palavra encontrada!"), 404

@app.route('/wlist/get', methods=['GET'])
def get_simple():
    return get_simple_bycomplex(0)

@app.route('/wlist/getfull/<int:complex>', methods=['GET'])
def get_full_bycomplex(complex):
    novapalavra = sortword(complex)
    if novapalavra :
        return jsonify(palavra=novapalavra['palavra'], 
                categoria=novapalavra['categoria'],
                complexidade=novapalavra['complexidade'])
    else:
        return jsonify(message="Nenhuma palavra encontrada!"), 404

@app.route('/wlist/getfull', methods=['GET'])
def get_full():
    return get_full_bycomplex(0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)