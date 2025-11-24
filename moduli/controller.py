from utente import Utente 
from prenotazione import Prenotazione as p

# ------------------ LETTURA UTENTI ------------------
# Legge gli utenti dal file utente.txt e restituisce una lista di oggetti Utente
def leggi_utenti_da_file():
    utenti = []
    with open("moduli/utente.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():  # ignora righe vuote
                nome, cognome, cellulare, allergie = line.strip().split(",")
                utenti.append(Utente(nome, cognome, cellulare, allergie))
    return utenti

# ------------------ LETTURA PRENOTAZIONI ------------------
# Legge le prenotazioni dal file prenotazione.txt e restituisce una lista di oggetti Prenotazione
def leggi_prenotazioni_da_file():
    prenotazioni = []
    with open("moduli/prenotazione.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():  # ignora righe vuote
                cellulare, data, ora, numero_persone = line.strip().split(",")
                utente = None
                # cerca l'utente corrispondente al cellulare
                for i in leggi_utenti_da_file():
                    if i.get_cellulare() == cellulare:
                        utente = i
                        break
                if utente:
                    prenotazioni.append(p(utente, data, ora, int(numero_persone)))
    return prenotazioni

# ------------------ CREAZIONE PRENOTAZIONE ------------------
# Controlla se l'utente ha già una prenotazione, altrimenti ne crea una nuova
def check_crea_prenotazione(utente, data, ora, numero_persone):
    prenotazioni = leggi_prenotazioni_da_file()
    if any(pren._Prenotazione__utente.get_cellulare() == utente.get_cellulare() for pren in prenotazioni):
        print("Non puoi prenotare di nuovo!")  # utente già prenotato
    else:
        nuova = p(utente, data, ora, numero_persone)
        nuova.salva_su_file()
        print("Prenotazione creata con successo.")

# ------------------ MENU ------------------
# Menu principale con le varie opzioni
def menu():
    while True:
        print("\n=== MENU PRINCIPALE ===")
        print("1. Aggiungi utente")
        print("2. Visualizza utenti")
        print("3. Aggiungi prenotazione")
        print("4. Visualizza prenotazioni")
        print("5. Esci")

        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case "1":
                # crea un nuovo utente e lo salva su file
                Utente.crea_utente()
            case "2":
                # mostra tutti gli utenti registrati
                utenti = leggi_utenti_da_file()
                if utenti:
                    for u in utenti:
                        u.visualizza_utente()
                else:
                    print("Nessun utente registrato.")
            case "3":
                # aggiungi una prenotazione
                cellulare = input("Cellulare utente: ")
                data = input("Data: ")
                ora = input("Ora: ")
                numero = int(input("Numero persone: "))

                # cerca l'utente nel file
                utente = None
                for u in leggi_utenti_da_file():
                    if u.get_cellulare() == cellulare:
                        utente = u
                        break
                    
                # se non trovato, lo crea subito
                if not utente:
                    print("Utente non trovato. Creiamone uno nuovo...")
                    nome = input("Inserisci nome: ")
                    cognome = input("Inserisci cognome: ")
                    allergie = input("Inserisci allergie: ")
                    utente = Utente(nome, cognome, cellulare, allergie)
                    utente.salva_su_file()

                # crea la prenotazione (con controllo duplicati)
                check_crea_prenotazione(utente, data, ora, numero)

            case "4":
                # mostra tutte le prenotazioni registrate
                prenotazioni = leggi_prenotazioni_da_file()
                if prenotazioni:
                    for pren in prenotazioni:
                        pren.visualizza_prenotazione()
                else:
                    print("Nessuna prenotazione registrata.")
            case "5":
                # chiude il programma
                print("Chiusura programma...")
                break
            case _:
                print("Scelta non valida.")

# Avvio del menu
menu()
