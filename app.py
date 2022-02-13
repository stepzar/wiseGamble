from flask import Flask, render_template, url_for

from data.dao.memoryImpl.PartitaDaoMemory import PartitaDaoMemory
from predictions.PredictionMakerSingleton import predictionMaker

app = Flask(__name__)

# percorso url
# home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/partite')
def partitePage():
    partiteDao = PartitaDaoMemory()
    return render_template('partite.html',partite = partiteDao.doRetriveAll())

@app.route('/partita/<id>')
def partitaPage(id):
    partiteDao = PartitaDaoMemory()
    partita = partiteDao.doRetrieveById(int(id))
    predictions = predictionMaker.makePredictions(partita)
    return render_template('partita.html',partita = partita, predictions = predictions)

if __name__ == "__main__":
    app.run(debug=True)