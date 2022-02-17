from flask import Flask, render_template, url_for
from data.dao.memoryImpl.PartitaDaoSofascore import PartitaDaoSofascore
from predictions.PredictionMakerSingleton import predictionMaker
import sqlite3

app = Flask(__name__)
dao = PartitaDaoSofascore()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/documentazione')
def documentazionePage():
    return render_template('documentazione.html')

@app.route('/partite/<date>')
def partitePage(date):
    return render_template('partite.html',partite = dao.doRetriveAll())

@app.route('/partita/<id>')
def partitaPage(id):
    partita = dao.doRetrieveById(int(id))
    predictions = predictionMaker.makePredictions(partita)
    return render_template('partita.html',partita = partita,predictions = predictions)

if __name__ == "__main__":
    app.run(debug=True)