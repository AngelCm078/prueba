#La biblioteca render_template nos permite renderizar los archivos html

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #Decorador
def hello_world():
    return render_template("index.html")

@app.route('/news')
def news():
    return render_template("news.html")

if __name__ == '__main__':
    app.run(debug=True)