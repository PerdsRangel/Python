from flask import Flask

app = Flask(__name__)

@app.route('/')
def portifolio():
    dados = {
        
    }
    return'''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Currículo - Pedro Rangel Mendes Martins</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
        h1 { color: #333; }
        h2 { color: #0056b3; border-bottom: 2px solid #0056b3; }
        .section { margin-bottom: 20px; }
    </style>
</head>
<body>
    <header>
        <h1>Pedro Rangel Mendes Martins</h1>
        <p>Telefone: (31) 98252-4017 | E-mail: perdsrangel@email.com</p>
    </header>

    <div class="section">
        <h2>Experiência de Trabalho</h2>
            <p><strong>No momento não tive experiências na área da tecnologia.</strong></p>
    </div>

    <div class="section">
        <h2>Educação</h2>
            <p>Colégio/Faculdade COTEMIG Ano 2024 - 2026</p>
    </div>

    <div class="section">
        <h2>Cursos</h2>
            <p>Curso CISCO - Manutenção de Computadores</p>
    </div>

    <div class="section">
        <h2>Idiomas</h2>
        <ul>
                <li>Ingles: Avançado - Espanhol: Inicial</li>
        </ul>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
