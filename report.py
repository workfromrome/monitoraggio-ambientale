import analisi
import funzioni_io


def generatore_report(rilevazioni, soglia_temp, soglia_co2):
    """
    Generatore di report strutturato per stazione di rilevamento contenente:
        Il numero totale delle rilevazioni;
        La media globale delle temperature;
        Il numero totale delle anomalie per la temperatura;
        Il numero totale delle anomalie per la concentrazione di CO2;
        Il giorno più critico in base al valore della concentrazione della CO2.
    """
    for stazione in funzioni_io.crea_lista_stazioni(rilevazioni):
        dati_stazione = [
            rilevazione for rilevazione in rilevazioni if rilevazione["stazione_di_rilevamento"] == stazione
        ]
        analisi_stazione = analisi.analisi_descr_stazioni(dati_stazione)
        anomalie_temp, anomalie_co2 = analisi.rileva_anomalie(dati_stazione, soglia_temp, soglia_co2)

        yield {
            "stazione": stazione,
            "numero_rilevazioni": len(dati_stazione),
            "temp_media": analisi_stazione[stazione]["temp_media"],
            "anomalie_temp": len(anomalie_temp),
            "anomalie_co2": len(anomalie_co2),
            "co2_max_data": analisi.trova_co2_max(dati_stazione)["data"]
        }


def produci_report(rilevazioni, soglia_temp, soglia_co2):
    """Scrive il report generato dalla funzione interna su un file .txt nella cartella dello script."""
    testo = []
    for blocco_stazione in generatore_report(rilevazioni, soglia_temp, soglia_co2):
        testo.append(f"--- {blocco_stazione['stazione']} ---")
        testo.append(f"Numero rilevazioni: {blocco_stazione['numero_rilevazioni']}")
        testo.append(f"Temperatura media: {blocco_stazione['temp_media']}")
        testo.append(f"Anomalie temperatura: {blocco_stazione['anomalie_temp']}")
        testo.append(f"Anomalie CO2: {blocco_stazione['anomalie_co2']}")
        giorno, mese, anno = blocco_stazione['co2_max_data']
        testo.append(f"Giorno più critico CO2: {giorno:02d}/{mese:02d}/{anno}")
        testo.append("")

    with open("./report.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(testo))
    print(f"\nReport generato nella cartella dello script.")

    return testo