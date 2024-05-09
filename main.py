from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    sexo = (request.form['sexo'])

    if sexo == "M" or sexo == "m":
        sexo = "Masculino"
    if sexo == "F" or sexo == "f":
        sexo = "Feminino"

    idade = int(request.form['idade'])

    if idade >= 0 and idade <= 5:
        resultado = "Bebê"
    elif idade >= 6 and idade <= 15:
        resultado = "Criança"
    elif idade >= 16 and idade <= 18:
        resultado = "Marmanjo, hora de trabalhar"
    elif idade >= 10 and idade >= 60:
        resultado = "Acorda pra vida, que você tem boletos para pagar"
    else:
        resultado = "Daqui pra frente é só para trás"

    return render_template('index.html', resultado=f'{resultado}, O sexo é {sexo}')

if __name__ == '__main__':
    app.run(debug=True)



