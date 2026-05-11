from flask import Flask

app = Flask(__name__)

@app.route('/Atv')
def decorator_explicacao():
    return 'O Decorator é uma função que modifica ou estende o comportamento de outra função, método ou classe sem alterar seu código-fonte original.'

if __name__ == '__main__':
    app.run(debug=True)