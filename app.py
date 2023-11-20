from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

clientes = []
produtos = []

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes, produtos=produtos)

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    nome = request.form['nome']
    endereco = request.form['endereco']
    contato = request.form['contato']
    
    clientes.append({'nome': nome, 'endereco': endereco, 'contato': contato})
    
    return redirect(url_for('index'))

@app.route('/cadastrar_produto', methods=['POST'])
def cadastrar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = float(request.form['preco'])
    quantidade_estoque = int(request.form['quantidade_estoque'])
    
    produtos.append({'nome': nome, 'descricao': descricao, 'preco': preco, 'quantidade_estoque': quantidade_estoque})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

