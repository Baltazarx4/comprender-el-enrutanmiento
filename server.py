from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET'])
def mensaje():
    return '<h1>hola mundo</h1>'

@app.route('/dojo')
def dojo():
    return '<h1>Dojo</h1>'

@app.route('/say/<nombre>')
def say(nombre):
    return f'Hola, {nombre}'

@app.route('/repeat/<int:num>/<string>')
def repeat(num,string):
    resultado = ""
    for i in range(num):
        resultado += string
    return resultado

if __name__ == '__main__':
    app.run(debug=True)