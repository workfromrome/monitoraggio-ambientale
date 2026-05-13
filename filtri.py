from funzioni_io import crea_lista_stazioni

def filtra_per_date(rilevazioni):
    """Filtra le rilevazioni per un intervallo di date selezionato dall'utente."""
    data_min = input("Inserisci la data di partenza in formato DD-MM-YYYY: ")
    data_max = input("Inserisci la data di fine in formato DD-MM-YYYY: ")

    min_split = data_min.split("-")
    data_min = (int(min_split[0]), int(min_split[1]), int(min_split[2]))
    max_split = data_max.split("-")
    data_max = (int(max_split[0]), int(max_split[1]), int(max_split[2]))

    filtrata = []
    for rilevazione in rilevazioni:
        if data_min[::-1] <= rilevazione["data"][::-1] <= data_max[::-1]:
            filtrata.append(rilevazione)

    return filtrata


def filtra_per_stazione(rilevazioni):
    """Filtra tutte le rilevazioni a seconda della stazione scelta dall'utente."""
    stazioni = crea_lista_stazioni(rilevazioni)

    for i, stazione in enumerate(stazioni):
        print(f"{i + 1}) {stazione}")
    n = int(input("Scegli una delle stazioni elencate: "))
    stazione_scelta = stazioni[n - 1]

    filtrata = []
    for rilevazione in rilevazioni:
        if rilevazione["stazione_di_rilevamento"] == stazione_scelta:
            filtrata.append(rilevazione)

    return filtrata


def filtra_per_temp(rilevazioni):
    """Filtra tutte le rilevazioni per l'intervallo di temperatura scelto dall'utente."""
    temp_min = float(input("Inserisci la temperatura minima: "))
    temp_max = float(input("Inserisci la temperatura massima: "))

    filtrata = []
    for rilevazione in rilevazioni:
        if temp_min <= rilevazione["temperatura"] <= temp_max:
            filtrata.append(rilevazione)

    return filtrata


def filtra_per_pressione(rilevazioni):
    """Filtra tutte le rilevazioni per l'intervallo di pressione scelto dall'utente."""
    press_min = float(input("Inserisci la pressione minima: "))
    press_max = float(input("Inserisci la pressione massima: "))

    filtrata = []
    for rilevazione in rilevazioni:
        if press_min <= rilevazione["pressione"] <= press_max:
            filtrata.append(rilevazione)

    return filtrata


def filtra_per_co2(rilevazioni):
    """Filtra tutte le rilevazioni per l'intervallo di concentrazione CO2 scelto dall'utente."""
    co2_min = float(input("Inserisci la concentrazione CO2 minima: "))
    co2_max = float(input("Inserisci la concentrazione CO2 massima: "))

    filtrata = []
    for rilevazione in rilevazioni:
        if co2_min <= rilevazione["concentrazione_co2"] <= co2_max:
            filtrata.append(rilevazione)

    return filtrata