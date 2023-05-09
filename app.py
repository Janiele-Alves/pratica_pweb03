from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listProdut')
def sobre():
    return render_template('listProdut.html')

@app.route('/descProduto')
def experiencia():
    return render_template('descProduto.html')

@app.route('/carrinho')
def formacao():
    return render_template('carrinho.html')

@app.route('/confirmacao')
def contato():
    return render_template('condirmacao.html')

if __name__ == '__main__':
    app.run(debug=True)
