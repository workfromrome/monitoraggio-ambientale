from funzioni_io import crea_lista_stazioni


def richiesta_soglie_utente():
    """Richiede in input le soglie temperatura e co2 da utilizzare in analisi e reportistica."""
    while True:
        try:
            soglia_temp = float(input("Immetti la soglia d'allarme della temperatura (es. 35.5): "))
            soglia_co2 = float(input("Immetti la soglia d'allarme della concentrazione di CO2 (es. 1000): "))
            return soglia_temp, soglia_co2
        except ValueError:
            print("Errore, inserisci un numero valido.")


def analisi_descr_stazioni(rilevazioni):
    """Crea un dizionario con le statistiche descrittive raggruppate per stazione."""

    analisi = {}

    for stazione in crea_lista_stazioni(rilevazioni):
        dati = [rilevazione for rilevazione in rilevazioni if rilevazione["stazione_di_rilevamento"] == stazione]
        temperature = [r["temperatura"] for r in dati]
        analisi[stazione] = {
            "temp_media": round(sum(temperature) / len(dati), 2),
            "temp_max": max(temperature),
            "temp_min": min(temperature),
            "umidita_media": round(sum(r["umidita"] for r in dati) / len(dati), 2),
            "pressione_media": round(sum(r["pressione"] for r in dati) / len(dati), 2),
            "co2_max": max(r["concentrazione_co2"] for r in dati),
        }

    return analisi


def rileva_anomalie(rilevazioni, soglia_temp, soglia_co2):
    """Rileva e restituisce anomalie co2 e temperatura a seconda della soglia impostata ordinate per gravità."""
    anomalie_temp = []
    anomalie_co2 = []
    for rilevazione in rilevazioni:
        if rilevazione["temperatura"] > soglia_temp:
            anomalie_temp.append(rilevazione)
        if rilevazione["concentrazione_co2"] > soglia_co2:
            anomalie_co2.append(rilevazione)
    anomalie_co2 = sorted(anomalie_co2, key=lambda r: r["concentrazione_co2"], reverse=True)
    anomalie_temp = sorted(anomalie_temp, key=lambda r: r["temperatura"], reverse=True)
    return anomalie_temp, anomalie_co2


def trova_temp_max(rilevazioni):
    """Restituisce la rilevazione con la temperatura massima."""

    rilevazione = max(rilevazioni, key=lambda r: r["temperatura"])
    return rilevazione


def trova_co2_max(rilevazioni):
    """Restituisce la rilevazione con la concentrazione co2 più alta."""

    rilevazione = max(rilevazioni, key=lambda r: r["concentrazione_co2"])
    return rilevazione


def max_variabilita_termica(rilevazioni):
    """Restituisce la stazione con la maggiore variabilità termica."""

    dati = analisi_descr_stazioni(rilevazioni)

    lista_variabilita = []
    for stazione, analisi in dati.items():
        temp_max = dati[stazione]["temp_max"]
        temp_min = dati[stazione]["temp_min"]
        variabilita = temp_max - temp_min
        lista_variabilita.append((stazione, variabilita))
    return max(lista_variabilita, key=lambda r: r[1])


def simulazione(rilevazioni, variazione):
    """
        Funzione di simulazione che:
        Riceve in input una variazione percentuale della temperatura;
        La applica a tutte le temperature esistenti;
        Ricalcola la nuova media globale delle temperature per stazione di rilevamento;
        Calcola l’incremento medio rispetto alla media originale;
        Restituisce i dati ordinati per incremento medio.
    """

    # Converte la variazione percentuale in un moltiplicatore
    variazione = 1 + variazione / 100

    new_rilevazioni = [rilevazione.copy() for rilevazione in rilevazioni]

    for rilevazione in new_rilevazioni:
        rilevazione["temperatura"] *= variazione

    analisi = analisi_descr_stazioni(rilevazioni)
    new_analisi = analisi_descr_stazioni(new_rilevazioni)

    diz_incrementi = {}

    for stazione, dati in new_analisi.items():
        incremento = round(dati["temp_media"] - analisi[stazione]["temp_media"], 2)
        diz_incrementi[stazione] = incremento

    sorted_incrementi = {stazione: incremento for stazione, incremento in
                         sorted(diz_incrementi.items(), key=lambda item: item[1], reverse=True)}


    return sorted_incrementi