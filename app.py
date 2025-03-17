from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    nome = request.form['nome']
    email = request.form['email']
    return f"<h1>Dados recebidos:</h1><p>Nome: {nome}</p><p>Email: {email}</p>"

if __name__ == '__main__':
    app.run(debug=True)
