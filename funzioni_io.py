def leggi_rilevazioni(nome_file):
    """Legge un file .csv e lo trasforma in una lista di rilevazioni."""

    rilevazioni = []

    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            for numero_riga, riga in enumerate(file, start=1):
                riga = riga.strip()

                # Salta eventuali righe vuote presenti nel CSV.
                if riga == "":
                    continue

                campi = riga.split(",")

                # Permette di usare anche un CSV con intestazione.
                if numero_riga == 1 and campi[0].lower() in ("id", "id_rilevazione"):
                    continue

                try:
                    if len(campi) != 7:
                        raise ValueError("numero di campi non corretto")

                    data_split = campi[1].split("-")
                    if len(data_split) != 3:
                        raise ValueError("data non valida")

                    data_tupla = (int(data_split[0]), int(data_split[1]), int(data_split[2]))
                    if data_tupla[0] < 1 or data_tupla[0] > 31 or data_tupla[1] < 1 or data_tupla[1] > 12:
                        raise ValueError("data fuori intervallo")

                    if campi[2].strip() == "":
                        raise ValueError("stazione mancante")

                    rilevazione = {
                        "id_rilevazione": int(campi[0]),
                        "data": data_tupla,
                        "stazione_di_rilevamento": campi[2],
                        "temperatura": float(campi[3]),
                        "umidita": float(campi[4]),
                        "pressione": float(campi[5]),
                        "concentrazione_co2": float(campi[6]),
                    }
                    rilevazioni.append(rilevazione)

                except ValueError as errore:
                    print(f"Errore: riga {numero_riga} del file {nome_file} non valida ({errore}).")

    except FileNotFoundError:
        print(f"Errore: il file {nome_file} e' mancante.")
    except PermissionError:
        print(f"Errore: permesso negato durante la lettura del file {nome_file}.")

    return rilevazioni

def crea_lista_stazioni(rilevazioni):
    """Crea una lista di stazioni."""
    lista_stazioni = []
    # Controlla ogni rilevazione e salva ogni stazione unica nella lista
    for rilevazione in rilevazioni:
        stazione = rilevazione["stazione_di_rilevamento"]
        if stazione not in lista_stazioni:
            lista_stazioni.append(stazione)
    return lista_stazioni

def aggiungi_rilevazione(rilevazioni):
    """Aggiunge una rilevazione in append al file delle rilevazioni nella cartella corrente.
    L'id viene auto-incrementato rispetto all'ultimo presente."""
    id_rilevazione = rilevazioni[-1]["id_rilevazione"] + 1
    data = input("Inserisci la data in formato DD-MM-YYYY: ")
    stazione = input("Inserisci il nome della stazione: ")
    temperatura = float(input("Inserisci la temperatura: "))
    umidita = float(input("Inserisci l'umidità: "))
    pressione = float(input("Inserisci la pressione: "))
    co2 = float(input("Inserisci la concentrazione di CO2: "))

    try:
        with open("./rilevazioni.csv", "a") as file:
            file.write(f"{id_rilevazione},{data},{stazione},{temperatura},{umidita},{pressione},{co2}\n")
        return True
    except (FileNotFoundError, PermissionError):
        return False
