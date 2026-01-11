from Flask import flask, render_template

app = Flask(__name__)

produtos = [()()()]

@app.route("/produtos")
def produtos():
  return render_template("produtos.html", produtos=produtos)

if __name__ == "__main__":
  app.run()