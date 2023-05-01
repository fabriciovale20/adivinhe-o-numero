from flask import Flask, render_template, request
from random import randint
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, filename='logs.log', format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def home():
    while True:
        try:
            primeiro_valor = 1  # Valor inicial, alterável
            ultimo_valor = 3  # Valor final, alterável
            if request.method == 'GET':
                logging.info('Pagina aberta!')
                return render_template('home.html')  # Página inicial
            else:
                logging.info('Numero inserido')
                numero_computador = randint(primeiro_valor, ultimo_valor)  # Range de números, possível altera-los acima
                valor = int(request.form.get('valor'))  # Recebe o valor informado pelo usuário

                # Faz a condição se o usuário escolheu o mesmo número do computador
                if numero_computador == valor:
                    logging.info(f'Usuario acertou! Numero = {numero_computador}')
                    return render_template('acertou.html')  # Se acertou, retorna essa página
                else:
                    logging.info(f'Usuario errou! Numero correto = {numero_computador} - Numero inserido {valor}')
                    return render_template('errou.html')  # Se errou, retorna essa página
        except ValueError:
            logging.error('Erro na pagina')
            return render_template('home.html')  # Página inicial

# Manter o app rodando
if __name__ == '__main__':
    app.run(debug=True)
