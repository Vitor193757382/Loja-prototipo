from flask import Flask, render_template, request

app = Flask(__name__)

produtos = [("https://cdn.pixabay.com/photo/2016/01/11/14/40/blouse-1133696_1280.png", "blusa", "uma blusa legal pra vestir"), ("https://cdn.pixabay.com/photo/2016/01/11/14/40/blouse-1133696_1280.png", "blusa", "uma blusa legal pra vestir"),("https://cdn.pixabay.com/photo/2016/01/11/14/40/blouse-1133696_1280.png", "blusa", "uma blusa legal pra vestir")]

@app.route('/')
def principal():
  return render_template('index.html')

@app.route('/criar', methods=['GET', 'POST'])
def criar():
  if request.method == 'POST':
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    imagem = request.form['imagem']
    if len(titulo) > 10:
      return render_template('criar.html', situacao=False, texto='Título muito grande')
    elif len(descricao) > 26:
      return render_template('criar.html', situacao=False, texto='Descrição muito grande')
    else:
      produtos.append((imagem, titulo, descricao))
      return render_template('criar.html', situacao=True, texto='Produto adicionado')
  return render_template('criar.html')

@app.route("/produtos")
def produtosloja():
  return render_template("produtos.html", produtos=produtos)

if __name__ == "__main__":
  app.run(debug=True)
