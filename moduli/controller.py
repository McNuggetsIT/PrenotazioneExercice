<<<<<<< Updated upstream
import moduli.utente as utenti
import moduli.prenotazione as prenotazioni



=======
from moduli.utente import Utente
from moduli.prenotazione import Prenotazione

utenti = open("utenti.txt", "r")
prenotazioni = open("prenotazione.txt", "r")

def leggi_utenti_da_file():
    utenti = []
    with open("utenti.txt","r", encoding="utf-8") as file:
        for line in line:
            nome,cognome,cellulare,allergie = line.strip().split(",")
            utenti.append(Utente(nome,cognome,cellulare,allergie))
        return utenti
    
def leggi_prenotazioni_da_file():
    prenotazioni = []
    with open("prenotazioni.txt","r", encoding="utf-8") as file:
        for line in line:
            cellulare,data,ora,numero_persone = line.strip().split(",")
            utente = None
            for i in leggi_utenti_da_file():
                if i.get_cellulare() == cellulare:
                    utente = i
                    break
                i
            
def check_crea_prenotazione(utente, data, ora, numero_persone):
    prenotazioni = leggi_prenotazioni_da_file()
    if any(p._Prenotazione__utente.get_cellulare() == utente.get_cellulare() for p in prenotazioni):
        print("Non puoi prenotare di nuovo!")
    else:
        nuova = Prenotazione(utente, data, ora, numero_persone)
        nuova.salva_su_file()
        print("Prenotazione creata con successo.")
>>>>>>> Stashed changes
