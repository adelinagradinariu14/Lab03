class Prestito:
    def __init__(self, codice, data, strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.strumento = strumento # è l'OGGETTO Strumento intero, non solo il suo codice
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        # {self.strumento} usa in automatico il __str__ di Strumento
        return f"{self.codice}, {self.data}, {self.strumento}, {self.cognome_allievo}"
