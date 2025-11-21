from moduli.utente import Utente  

class Prenotazione():
    def __init__(self, utente, data="", ora="", numero_persone=0):
        # L'oggetto utente viene passato già creato (composizione, non ereditarietà)
        # È privato così la prenotazione può accedere all'utente solo tramite get/set
        self.__utente = utente

        # Attributi privati della prenotazione
        self.__data = data        
        self.__ora = ora             
        self.__numero_persone = numero_persone 
        

    # ------------------------- GETTER -------------------------

    # Restituisce la data della prenotazione
    def get_data(self):
        return self.__data

    # Restituisce l'ora della prenotazione
    def get_ora(self):
        return self.__ora

    # Restituisce il numero di persone della prenotazione
    def get_numero_persone(self):
        return self.__numero_persone


    # ------------------------- SETTER -------------------------

    # Modifica la data della prenotazione
    def set_data(self, data):
        self.__data = data

    # Modifica l'ora della prenotazione
    def set_ora(self, ora):
        self.__ora = ora

    # Modifica il numero di persone della prenotazione
    def set_numero_persone(self, numero):
        self.__numero_persone = numero
  

    # ------------------ CREAZIONE PRENOTAZIONE ------------------

    # Imposta i dati principali della prenotazione
    # e salva tutto sul file prenotazione.txt
    def crea_prenotazione(self, data, ora, numero_persone):
        self.__data = data
        self.__ora = ora
        self.__numero_persone = numero_persone

        # Salva immediatamente la prenotazione su file
        self.salva_su_file()
        print("Prenotazione creata con successo.")

    # ------------------ MODIFICA PRENOTAZIONE ------------------

    # Modifica solo i campi passati come argomento
    # (se non li passo, restano invariati)
    def modifica_prenotazione(self, data="", ora="", numero_persone=0):
        if data:
            self.__data = data
        if ora:
            self.__ora = ora
        if numero_persone > 0:
            self.__numero_persone = numero_persone

        # Dopo la modifica, riscrive sul file
        self.salva_su_file()
        print("Prenotazione modificata con successo.")

    # ------------------ VISUALIZZAZIONE ------------------

    # Mostra la prenotazione leggendo i dati dall'utente associato
    def visualizza_prenotazione(self):
        print(f"Prenotazione di {self.__utente.get_nome()} {self.__utente.get_cognome()}:")
        print(f"Data: {self.__data}")
        print(f"Ora: {self.__ora}")
        print(f"Numero persone: {self.__numero_persone}")


    def salva_su_file(self):

    # Apro (o creo) il file prenotazione.txt in modalità "a"
    # "a" significa "append": aggiungi nuove righe senza cancellare quelle già presenti.
     with open("prenotazione.txt", "a") as file:

        # Scrivo una riga contenente:
        # - il cellulare dell'utente (che funge da identificatore univoco)
        # - la data della prenotazione
        # - l'ora della prenotazione
        # - il numero di persone
        #
        # I campi sono separati da virgole per ottenere un formato simile al CSV.
        # Il carattere "\n" alla fine serve per andare a capo e iniziare una nuova riga.
        file.write(
            f"{self.__utente.get_cellulare()},"
            f"{self.__data},"
            f"{self.__ora},"
            f"{self.__numero_persone}\n"
        )



    # ------------------ LETTURA PRENOTAZIONI ------------------

    # Legge e mostra tutte le prenotazioni presenti nel file
    def leggi_prenotazioni(self):
        # Apre il file in sola lettura
        file = open("prenotazione.txt", "r")

        # Cicla ogni riga del file
        for line in file:

            # Rimuove eventuali spazi o newline finali e separa i campi tramite virgola
            dati = line.strip().split(",")

            # Assegna ogni campo ad una variabile
            nome, cognome, cellulare, allergie, data, ora, numero_persone = dati

            # Stampa una prenotazione formattata
            print(
                f"{nome} {cognome} - Cell: {cellulare} - "
                f"Allergie: {allergie} - Data: {data} - "
                f"Ora: {ora} - Persone: {numero_persone}"
            )

        # Chiudo il file al termine
        file.close()
