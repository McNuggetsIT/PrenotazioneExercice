class Utente:
    def __init__(self,nome,cognome,cellulare,allergie):
        self.__nome = nome
        self.__cognome = cognome
        self.__cellulare = cellulare
        self.__allergie = allergie
        
    
    #Metodi get per attributi
    
    def get_nome(self):
        return self.__nome

    def get_cognome(self):
        return self.__cognome
    
    def get_cellulare(self):
        return self.__cellulare

    def get_allergie(self):
        return self.__allergie
    
    #metodi set per attributi
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_cognome(self, cognome):
        self.__cognome = cognome

    def set_cellulare(self, cellulare):
        self.__cellulare = cellulare

    def set_allergie(self, allergie):
        self.__allergie = allergie
        
    def crea_utente():
        nome = input("Inserisci un nome: ")
        cognome = input("Inserisci cognome: ")
        cellulare = input("Inserisci cellulare: ")
        allergie = input("Inserisci allergie: ")
        nuovo = Utente(nome, cognome, cellulare, allergie)
        nuovo.salva_su_file()
        return nuovo
        
    
    def visualizza_utente(self):
        print(f"Nome: {self.__nome}")
        print(f"Cognome: {self.__cognome}")
        print(f"Cellulare: {self.__cellulare}")
        print(f"Allergie: {self.__allergie}")
    
    def modifica_utente(self):
        print("Si prega di non scrivere nulla se non si vuole modificare il campo!")
        nuovo_nome = input(f"Modificare nome {self.__nome}: ")
        nuovo_cognome = input(f"Modificare cognome {self.__cognome}: ")
        nuovo_cellulare = input(f"Modificare cellulare {self.__cellulare}: ")
        nuovo_allergie = input(f"Inserisci allergie {self.__allergie}: ")
        
        if nuovo_nome.strip():
            self.__nome = nuovo_nome
        if nuovo_cognome.strip():
            self.__cognome = nuovo_cognome
        if nuovo_cellulare.strip():
            self.__cellulare = nuovo_cellulare
        if nuovo_allergie.strip():
            self.__allergie = nuovo_allergie
        self.salva_su_file()

    
    def rimuovi_utente(self):
        nome_scelta = input("Che nome vuoi eliminare? ")
        cognome_scelta = input("Che cognome vuoi eliminare? ")
        if nome_scelta == self.get_nome() and cognome_scelta == self.get_cognome():
            conferma = input(f"Sicuro di voler eliminare {self.__nome} {self.__cognome} dalle prenotazioni?" '(s/n)')
            if conferma == 's':
                self.__nome = None
                self.__cognome = None
                self.__cellulare = None
                self.__allergie = None
                print("Utente eliminato")
                
            else:
                print("Cancellazione annullata")
                
        else:
            print("Nome e Cognome non trovati!")
                
    def salva_su_file(self):
        with open("utenti.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{self.get_nome()},"
                f"{self.get_cognome()},"
                f"{self.get_cellulare()},"
                f"{';'.join(self.get_allergie())}\n"
            )
    