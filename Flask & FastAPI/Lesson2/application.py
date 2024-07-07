from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    cards = [
        {
            "title": "Card 1",
            "content": "Some text about card 1"
        },
        {
            "title": "Card 2",
            "content": "Some text about card 2"
        },
        {
            "title": "Card 3",
            "content": "Some text about card 3"}
    ]
    return render_template("index.html", context=cards)


if __name__ == "__main__":
    app.run(debug=True)
