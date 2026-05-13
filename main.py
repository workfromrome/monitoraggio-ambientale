import filtri
import funzioni_io
import analisi
import report


def stampa_rilevazioni(rilevazioni):
    """Funzione per visualizzare meglio le rilevazioni da stampare."""
    print(
        f"{'ID':<5} | {'DATA':<11} | {'STAZIONE':<15} | {'TEMP':<8} | {'UMIDITA':<8} | {'PRESSIONE':<10} | {'CO2':<10}")
    print("-" * 82)
    for rilevazione in rilevazioni:
        giorno, mese, anno = rilevazione['data']
        print(f"{rilevazione['id_rilevazione']:<5} | "
              f"{giorno:02d}/{mese:02d}/{anno}  | "
              f"{rilevazione['stazione_di_rilevamento']:<15} | "
              f"{rilevazione['temperatura']:<8} | "
              f"{rilevazione['umidita']:<8} | "
              f"{rilevazione['pressione']:<10} | "
              f"{rilevazione['concentrazione_co2']:<10}")
    print("-" * 82)
    print(f"\n")

def stampa_analisi(rilevazioni):
    """Funzione che stampa un dizionario di analisi."""
    dati = analisi.analisi_descr_stazioni(rilevazioni)
    print(f"{'STAZIONE':<14} | {'TEMP_MEDIA':<10} | {'TEMP_MAX':<10} | {'TEMP_MIN':<10} | {'UMIDITA_MEDIA':<14} | "
          f"{'PRESSIONE_MEDIA':<16} | {'CO2_MAX':<10}")
    print("-" * 99)
    for stazione, valori in dati.items():
        print(f"{stazione:<14} | "
              f"{valori['temp_media']:<10} | "
              f"{valori['temp_max']:<10} | "
              f"{valori['temp_min']:<10} | "
              f"{valori['umidita_media']:<14} | "
              f"{valori['pressione_media']:<16} | "
              f"{valori['co2_max']:<10}")
    print("-" * 99)
    print(f"\n")

def stampa_simulazione(sorted_incrementi, variazione):
    """Stampa gli incrementi medi per stazione risultanti dalla funzione di simulazione."""
    print(f"\nSimulazione con variazione: {variazione:+}%")
    print("-" * 35)
    for stazione, incremento in sorted_incrementi.items():
        print(f"  {stazione:<20} {incremento:+.2f}°C")
    print("-" * 35)

########
# MAIN #
########

def main():
    rilevazioni = funzioni_io.leggi_rilevazioni("./rilevazioni.csv")
    if len(rilevazioni) == 0:
        print("Errore: nessuna rilevazione caricata. Controlla il file rilevazioni.csv.")
        return

    while True:
        scelta = input("""
Scegli una delle seguenti funzioni.
1) Analisi descrittiva stazioni
2) Rileva anomalie
3) Variabilità termica massima
4) Produci report
5) Simulazione temperatura
6) Filtra per data
7) Filtra per stazione
8) Filtra per temperatura
9) Filtra per pressione
10) Filtra per CO2
11) Aggiungi una rilevazione
Oppure inserisci "exit" per uscire:
> """)

        match scelta:

            case "1":
                stampa_analisi(rilevazioni)

            case "2":
                soglia_temp, soglia_co2 = analisi.richiesta_soglie_utente()
                anomalie_temp, anomalie_co2 = analisi.rileva_anomalie(rilevazioni, soglia_temp, soglia_co2)
                print("Anomalie di temperatura rilevate: (ordinate per gravità):")
                stampa_rilevazioni(anomalie_temp)
                print("Anomalie di concentrazione CO2 rilevate: (ordinate per gravità):")
                stampa_rilevazioni(anomalie_co2)

            case "3":
                stazione, variabilita = analisi.max_variabilita_termica(rilevazioni)
                print(f"La variabilità termica massima appartiene a {stazione} ed è di {variabilita}.")

            case "4":
                soglia_temp, soglia_co2 = analisi.richiesta_soglie_utente()
                testo = report.produci_report(rilevazioni, soglia_temp, soglia_co2)
                for elemento in testo:
                    print(elemento)

            case "5":
                variazione = float(input("Immetti la variazione della temperatura in percentuale (es. +5 o -5): "))
                sorted_incrementi = analisi.simulazione(rilevazioni, variazione)
                stampa_simulazione(sorted_incrementi, variazione)

            case "6":
                stampa_rilevazioni(filtri.filtra_per_date(rilevazioni))

            case "7":
                stampa_rilevazioni(filtri.filtra_per_stazione(rilevazioni))

            case "8":
                stampa_rilevazioni(filtri.filtra_per_temp(rilevazioni))

            case "9":
                stampa_rilevazioni(filtri.filtra_per_pressione(rilevazioni))

            case "10":
                stampa_rilevazioni(filtri.filtra_per_co2(rilevazioni))

            case "11":
                if funzioni_io.aggiungi_rilevazione(rilevazioni):
                    print("Rilevazione aggiunta con successo.")
                else:
                    print("Errore durante l'aggiunta della rilevazione.")
                rilevazioni = funzioni_io.leggi_rilevazioni("./rilevazioni.csv")

            case "exit":
                print("Arrivederci!")
                break

            case _:
                print("Scelta non valida, riprova.")
    

if __name__ == "__main__":
    main()
