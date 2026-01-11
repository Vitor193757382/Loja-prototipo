from flask import Flask, render_template

app = Flask(__name__)

produtos = [("https://pixabay.com/vectors/blouse-cloth-fashion-kids-1133696/", "blusa", "uma blusa legal pra vestir"), ("https://pixabay.com/vectors/blouse-cloth-fashion-kids-1133696/", "blusa", "uma blusa legal pra vestir"), ("https://pixabay.com/vectors/blouse-cloth-fashion-kids-1133696/", "blusa", "uma blusa legal pra vestir")]

@app.route("/produtos")
def produtosloja():
  return render_template("produtos.html", produtos=produtos)

if __name__ == "__main__":
  app.run()
