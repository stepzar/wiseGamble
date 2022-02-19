from flask import Flask, render_template, url_for
from data.dao.memoryImpl.PartitaDaoSofascore import PartitaDaoSofascore
from predictions.PredictionMakerSingleton import predictionMaker
from datetime import datetime

app = Flask(__name__)
dao = PartitaDaoSofascore()

@app.route('/')
def index():
    date = datetime.today().strftime('%Y-%m-%d')
    return render_template('index.html', date=date)

@app.route('/documentazione')
def documentazionePage():
    date = datetime.today().strftime('%Y-%m-%d')
    return render_template('documentazione.html', date=date)

@app.route('/partite/<date>&<league>')
def partitePage(date, league):
    if league == "all":
        return render_template('partite.html', datetime=datetime, date=date, partite = dao.doRetrieveAll())
    else:
        return render_template('partite.html', datetime=datetime, date=date, partite = dao.doRetrieveByLeague(league))

@app.route('/partita/<date>&<id>')
def partitaPage(date, id):
    partita = dao.doRetrieveById(int(id))
    predictions = predictionMaker.makePredictions(partita)
    return render_template('partita.html', date=date, datetime=datetime, partita = partita,predictions = predictions)

if __name__ == "__main__":
    app.run(debug=True)