from flask import Flask

app = Flask(__name__)

@app.route('/Decorator')
def decorator_explicacao():
    return 'O Decorator é uma função que recebe outra função como argumento, adiciona funcionalidades a ela e retorna uma nova função, ' \
    'tudo isso sem alterar o código original da função decorada, serve para evitar repetição de código (DRY). É usado para logs,' \
    'medir tempo de execução, validar permissões ou cache. No Flask O decorator registra a função que vem logo abaixo como a responsável por responder quando ' \
    'alguém acessa aquele endereço específico no navegador.'

if __name__ == '__main__':
    app.run(debug=True)