from strumento import Strumento
from prestito import Prestito
from operator import attrgetter
import csv

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome # self mi indica quell'oggetto stesso
        self.responsabile = responsabile

        # inizializzo le liste con self.
        self.strumenti = []
        self.prestiti = [] # solo prestiti ATTIVI
        self.contatore_prestiti = 0
        # numero dell'ultimo prestito creato, serve per dare codici

    #altre funzioni della classe deposito
    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # se il file non esiste, open() scatena da solo FileNotFoundError, gestito dal main
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            righe = csv.reader(file) # ogni riga arriva già 'spezzata'

            for riga in righe: # riga = ["S1", "Chitarra", "Yamaha", "2019", "250.00"]
                # creo nuovo oggetto che chiama l'init
                strumento = Strumento(riga[0], riga[1], riga[2], int(riga[3]), float(riga[4]))
                self.strumenti.append(strumento)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        ultimo_numero = 0

        for s in self.strumenti:
            numero = int(s.codice[1:])
            if numero > ultimo_numero:
                ultimo_numero = numero

        codice = "S" + str(ultimo_numero + 1)
        nuovo = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovo)

        return nuovo

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti, key=attrgetter("marca"))  # sorted() crea una nuova lista ordinata
        # non modifica self.strumenti

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""

        # CONTROLLO 1: lo strumento esiste?
        strumento_trovato = None # = niente, vuoto

        for s in self.strumenti:
            if s.codice == id_strumento:
                strumento_trovato = s

        if strumento_trovato is None:
            raise Exception(f"Strumento {id_strumento} non esistente")

        # CONTROLLO 2: lo strumento è già in prestito?
        for p in self.prestiti:
            if p.strumento.codice == id_strumento: # p.strumento è un oggetto Strumento, .codice è il suo codice
                raise Exception(f"Strumento {id_strumento} già in prestito")

        # se i controlli sono ok, creo il prestito
        self.contatore_prestiti += 1
        codice = "P" + str(self.contatore_prestiti)
        prestito = Prestito(codice, data, strumento_trovato, cognome_allievo)
        self.prestiti.append(prestito)
        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for p in self.prestiti:
            if p.codice == id_prestito: # tolgo il prestito dalla lista, lo strumento torna libero
                self.prestiti.remove(p)
                return

        # se il ciclo finisce senza aver trovato nulla, il codice non esiste
        raise Exception(f"Prestito {id_prestito} non trovato")
