from flask import Flask, render_template

app = Flask(__name__)

produtos = [("https://cdn.pixabay.com/photo/2016/01/11/14/40/blouse-1133696_1280.png", "blusa", "uma blusa legal pra vestir"), ("https://cdn.pixabay.com/photo/2016/01/11/14/40/blouse-1133696_1280.png", "blusa", "uma blusa legal pra vestir"),("https://cdn.pixabay.com/photo/2016/01/11/14/40/blouse-1133696_1280.png", "blusa", "uma blusa legal pra vestir")]

@app.route("/produtos")
def produtosloja():
  return render_template("produtos.html", produtos=produtos)

if __name__ == "__main__":
  app.run()
