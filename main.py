from flask import Flask, jsonify
import csv
import random

arquivo_txt = "dicionario.txt"

app = Flask(__name__)

def open_localdicionario(arquivo_txt, c):
    dados = []
    with open(arquivo_txt, mode='r') as meuarquivo:
        buffer = csv.reader(meuarquivo)
        for linha in buffer:
            ## print(linha) #amsdebug
            if  linha[0] == str(c) :
                complex = linha[0]
                cat = linha[1]
                pal = linha[2]
                dados.append({'complexidade': complex, 'categoria': cat, 'palavra':pal})
    return dados

def sortword(cat) :
    dicionario = open_localdicionario(arquivo_txt, 1) ##dicionario
    ##palavra_sorteada = dicionario[0]
    pos = random.randint(0,len(dicionario)-1)
    palavra_sorteada = dicionario[pos]
    ##palavra_sorteada = dicionario[random.randint(0,len(dicionario)-1)]
    return palavra_sorteada

@app.route('/simple-get', methods=['GET'])
def get_simple_message():
    novapalavra = sortword(1)
    return jsonify(palavra=novapalavra['palavra'])

@app.route('/complex-get', methods=['GET'])
def get_complex_message():
    novapalavra = sortword(1)
    return jsonify(palavra=novapalavra['palavra'], 
                categoria=novapalavra['categoria'],
                complexidade=novapalavra['complexidade'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)