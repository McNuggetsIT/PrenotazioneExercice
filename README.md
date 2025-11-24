# PrenotazioneExercice

## Utente.py
Definisce la classe `Utente` con attributi privati (nome, cognome, cellulare, allergie).  
Funzioni principali:
- `crea_utente()`: crea un nuovo utente e lo salva su file.
- `visualizza_utente()`: mostra i dati dell’utente.
- `modifica_utente()`: aggiorna i dati.
- `rimuovi_utente()`: elimina i dati (solo in memoria).
- `salva_su_file()`: scrive i dati in `utente.txt`.

**Autore: Gianmarco Sorrentino**

---

## Prenotazione.py
Definisce la classe `Prenotazione` associata a un utente.  
Funzioni principali:
- `crea_prenotazione()`: crea e salva una prenotazione.
- `modifica_prenotazione()`: aggiorna i dati e riscrive su file.
- `visualizza_prenotazione()`: mostra i dettagli della prenotazione.
- `salva_su_file()`: scrive i dati in `prenotazione.txt`.
- `leggi_prenotazioni()`: legge e mostra tutte le prenotazioni.

**Autore: Anna Firinu**

---

## Controller.py
Gestisce il menu principale e l’interazione con l’utente.  
Funzioni principali:
- `leggi_utenti_da_file()`: legge gli utenti da file.
- `leggi_prenotazioni_da_file()`: legge le prenotazioni da file.
- `check_crea_prenotazione()`: controlla duplicati e crea prenotazioni.
- `menu()`: interfaccia testuale con opzioni:
  1. Aggiungi utente  
  2. Visualizza utenti  
  3. Aggiungi prenotazione  
  4. Visualizza prenotazioni  
  5. Esci

**Autore: Giuseppe D’Avanzo**
