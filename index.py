from flask import Flask, render_template, jsonify, request,redirect
import time


#.venv\Scripts\activate
#python app.py


app = Flask(__name__)

@app.route("/")
def index():
    #aqui ponemos la carga? 
    #se necesita poner el envio y eso de lo que se recolecte
    return render_template("loading.html")

@app.route("/process-task")
def process_task():
    #aqui ponemos la carta que se abre?
    time.sleep(3)
    return jsonify(status="complete")



@app.route("/pagina", methods=["POST","GET"])
def pagina():
    #aqui ponemos la carta que se abre?
    if request.method == "POST": 
        return render_template("index.html")
    else: 
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)