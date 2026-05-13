# Rilevazioni ambientali

Questo programma gestisce una piccola raccolta di rilevazioni ambientali.
Permette di leggere i dati, analizzarli per stazione, filtrare le rilevazioni,
individuare anomalie, simulare variazioni di temperatura e produrre un report.

Script per l'esercitazione per il corso, per visualizzare il testo dell'esercitazione cliccare [qui](./esercitazione_1.docx).

## Struttura dei file

- `main.py`: avvia il menu principale del programma.
- `funzioni_io.py`: contiene le funzioni per leggere i dati e gestire le stazioni.
- `analisi.py`: contiene le funzioni di analisi e simulazione.
- `filtri.py`: contiene le funzioni per filtrare le rilevazioni.
- `report.py`: genera il report testuale.
- `rilevazioni.csv`: contiene i dati di esempio delle rilevazioni.


## Formato del CSV

Ogni riga di `rilevazioni.csv` deve avere 7 campi separati da virgola:

```text
id_rilevazione,data,stazione,temperatura,umidita,pressione,concentrazione_co2
```

La data _deve_ essere scritta nel formato `GG-MM-AAAA`.

Esempio:

```text
1,16-02-2025,Stazione_Alfa,40.71,45.25,1012.08,1116.66
```

## Prerequisiti

- Python 3.10 o superiore.
- Tutti i file `.py` devono trovarsi nella stessa cartella.
- Il file `rilevazioni.csv` deve trovarsi nella stessa cartella da cui viene avviato il programma.

## Avvio

Da terminale, entrare nella cartella del progetto e avviare:

```text
python main.py
```
