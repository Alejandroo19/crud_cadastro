from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "chave-secreta"  # Substitua por algo seguro

# Lista de produtos (armazenamento em memória)
products = []

@app.route("/")
def index():
    # Ordenar os produtos pelo valor (do menor para o maior)
    sorted_products = sorted(products, key=lambda x: x["price"])
    return render_template("index.html", products=sorted_products)

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        # Obter os dados do formulário
        name = request.form["name"]
        description = request.form["description"]
        price = float(request.form["price"])
        available = request.form["available"] == "yes"

        # Adicionar o produto à lista
        products.append({"name": name, "description": description, "price": price, "available": available})

        # Redirecionar para a página inicial
        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for("index"))

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
