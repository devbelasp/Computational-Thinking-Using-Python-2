# Crie uma pasta para o projeto
# Cria uma pasta chamado "templates" para os arquivos html

# (mini) Framework Flask
# instalar o Flask: 
#    - pip install Flask

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    #lógica da função...
    return 'Hello, 1TDSPH!'

@app.route('/hello/<nome>')
def hello_name(nome):
    return f'Hello, {nome}'

@app.route('/python')
def hello_python():
    return 'Hello, Python!'

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    #lógica da função
    #...
    return f'A soma de {n1} com {n2} é {n1+n2}'

@app.route('/rev/<float:rev_no>')
def revision(rev_no):
    return f'Revision number: {rev_no}'

@app.route('/home')
def homepage():
    #return {"status":"OK"}
    return jsonify({"status":"OK"})

@app.route('/todo')
def todo_list():
    return jsonify(
        {"Tarefa 1" : "Estudar Python"},
        {"Tarefa 2" : "Estudar Java"},
        {"Tarefa 3" : "Fazer o CP de Python"},
        {"Tarefa 4" : "Ir para o NEXT"},
        {"Tarefa 5" : "Quartouuuuu!"})

@app.route('/pagina1')
def pagina1():
    return render_template("pagina1.html")

#Programa Principal
if __name__ == '__main__':
    app.run() #executar a app no servidor Flask