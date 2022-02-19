<img src="https://user-images.githubusercontent.com/20650309/154808592-a7f936d2-5d9e-49c8-9fba-790b5263d531.png" alt="WiseGamble" width="200">

# WiseGamble
### Pronostici calcistici
WiseGamble è una web-app realizzata in python, tramite il framework **Flask**, che permette di ricevere pronostici calstici riguardanti due esiti in particolare:
- Over/Under Cartellini Gialli 5.5
- Over/Under Corner 7.5

I pronostici vengono *calcolati* tramite due modelli di *Machine Learning* addestati su un dataset di 20.000+ partite.
Il dataset utilizzato per l'addestramento contiene le partite dal 2015 al 2021 dei seguenti campionati:
- UEFA Champions League
- UEFA Europa League
- Premier League
- LaLiga
- Bundesliga
- Serie A
- Ligue 1
- Eredivise
- Premiership (scozia)
- Serie B
- Pro League (belgio)
- Superliga (danimarca)
- Championship
- Eliteserien
- Lech pozann (polonia)
Quindi sarà possibile accedere ai pronostici solo per le partite dei campionati sopra elencati.


https://user-images.githubusercontent.com/20650309/154808824-d0f44b08-026d-4420-9295-0d9900dad7d4.mov



## Struttura
Avviando la web-app *WiseGamble* si accede alla pagina *Home* dove è possibile visualizzare una breve descrizione di cosa offre il sito, una breve descrizione dei passi seguiti per la realizzazione dei modelli, alcune FAQ e la lista dei membri del team di WiseGamble.
Dalla Home si ha accesso alla pagina dove si possono visualizzare tutte le partite che si disputerranno nell'arco della giornata e per le quali si può ricevere un pronostico,
selezionando una partita si accede alla pagina in cui vengono riportati i pronostici della partita con relative percentuali di fiducia delle predizioni.

Inoltre nell'header è possibile trovare:
- il link per accedere alla pagina html dove viene riportata la documentazione completa;
- il link per accedere alla cartella drive in cui sono presenti i jupyter notebook, dove è possibile visualizzare tutta la pipeline seguita per la costruzione dei modelli predittivi.

---

## Tecnologie utilizzate
Le tecnologie utilizzate per la realizzazione del seguente progetto sono state:
- [**Flask**](https://flask.palletsprojects.com/en/2.0.x/)
- [**Pandas**](https://pandas.pydata.org/)
- [**Scikit-learn**](https://scikit-learn.org/stable/)

## Contributi
La realizzazione della web-app *WiseGamble* è stata possibile tramite il contributo di:<br>
- [Cannavale Alfonso](https://github.com/alfcan)<br>
- [Sepe Aurelio](https://github.com/AurySepe)<br>
- [Zarro Stefano](https://github.com/stepzar)<br>
