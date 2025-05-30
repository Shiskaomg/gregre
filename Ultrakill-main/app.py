from flask import Flask, render_template
from sql import get_all_weapons

app = Flask(__name__, static_folder='css')  # Якщо ви хочете підключати CSS з /css

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lore')
def lore():
    return render_template('index.html')  # Можливо, слід створити окрему lore.html?

@app.route('/weapon')
def weapons():
    return render_template('index1.html', weapons=get_all_weapons())
app.run(debug=True)