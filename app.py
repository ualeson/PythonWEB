from flask import Flask, render_template, request

app = Flask(__name__)

nome = "Desenvolvedor Python"

@app.route('/')
def home():
    return render_template('index.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
