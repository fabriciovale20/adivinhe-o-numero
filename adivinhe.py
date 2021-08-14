from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    while True:
        try:
            primeiro_valor = 1  # Valor inicial, alterável
            ultimo_valor = 10  # Valor final, alterável
            if request.method == 'GET':
                return render_template('home.html')  # Página inicial
            else:
                numero_computador = randint(primeiro_valor, ultimo_valor)  # Range de números, possível altera-los acima
                valor = int(request.form.get('valor'))  # Recebe o valor informado pelo usuário

                # Faz a condição se o usuário escolheu o mesmo número do computador
                if numero_computador == valor:
                    return render_template('acertou.html')  # Se acertou, retorna essa página
                else:
                    return render_template('errou.html')  # Se errou, retorna essa página
        except ValueError:
            return render_template('home.html')  # Página inicial


if __name__ == '__main__':
    app.run(debug=True)
