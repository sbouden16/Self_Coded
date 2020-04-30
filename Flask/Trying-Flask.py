from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Ejercicio con toma datos.html")

@app.route("/hellooo")
def hellooo():
    return "<h2>Some information for Marek</h2>"+"<p><strong> Some lines of paraghrap</strong></p>"
if __name__ == "__main__":
    app.run(debug=True)
    
