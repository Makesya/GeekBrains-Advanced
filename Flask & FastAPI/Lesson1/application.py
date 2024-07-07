from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>')
@app.route('/')
def hello_world(name='незнакомец'):
    return render_template('index.html', name=name)


app.run()
