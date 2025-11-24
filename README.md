# PrenotazioneExercice

Anna F, Giuseppe D, Gianamarco S
Sorrentino Gianmarco: 
Crezione di una classe base chiamata Utente , che racchiude degli attributi privati , come nome , cognome , cellulare e allergie.
Ho definito i metodi get e set per ogni attributo, e varo metodi come crea_utente , visualizza_utente , modifica_utente , rimuovi_utente.

Crea Utente : chiedi di inserire in input nome , cognome , cellulare ed allergie. Una volta fatto salva tutto su file
Visualizza Utente : Che ci permette di visualizzare gli utenti con i rispettivi attributi
Modifica Utente : Permette di modificare i dati utente inseriti
Rimuovi utente : Rimuove i dati utente dalla prenotazione

Il metodo salva_su_file : Scrive su un file chiamati "utenti.txt" , tutti gli attributi di utente.

Firinu Anna: 
Creazione della classe Prenotazione. Alla classe prenotazione ho passato l'utente già creato, e ho aggiunto gli attributi privati data, ora e numero persone. Dopo aver definito i get e set ho definito i seguenti metodi:
-salva su file: mi permette di aggiungere nuove righe al file andando a inserire il numero di cellulare dell'utente, data, ora e numero posti.
-crea prenotazioe: Permette di inserire i dati della prenotazione e attraverso il metodo salva su file li aggiunge al file prenotazion.txt.
-modifica prenotazione: Permette di modificare una prenotazione esistente e riscriverla sul file
-visualizza prenotazione: Mostra la prenotazione singola leggendo i dati dell'utente associato
-lettura prenotazinni: Mostra tutte le prenotazioni presenti.

D'Avanzo Giuseppe:

# Controller.py

Il file `controller.py` gestisce il menu principale del progetto PrenotazioneExercice.  
Permette di interagire con gli utenti e le prenotazioni tramite un'interfaccia testuale.

## Funzioni principali
- `leggi_utenti_da_file()`: legge gli utenti da `utente.txt`.
- `leggi_prenotazioni_da_file()`: legge le prenotazioni da `prenotazione.txt`.
- `check_crea_prenotazione()`: controlla se un utente ha già una prenotazione e, se no, la crea.
- `menu()`: mostra le opzioni e gestisce l'interazione.

