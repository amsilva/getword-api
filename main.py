from flask import Flask, jsonify
import csv
import random
from bs4 import BeautifulSoup
import requests

arquivo_txt = "dicionario.txt"
url_txt = "https://dontpad.com/faccamphoy/getworld/dicionario"

app = Flask(__name__)

def open_webdicionario():
    # URL da página Don'tPad
    url = url_txt

    # Faz uma requisição para obter o conteúdo da página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Faz o parsing do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontra o conteúdo na página
        conteudo = soup.get_text()

        # Exibe o conteúdo
        print(conteudo)
    else:
        print("Erro ao acessar a página:", response.status_code)

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
    open_webdicionario()
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