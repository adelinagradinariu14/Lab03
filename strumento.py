class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        # salvo i dati ricevuti negli attributi dell'oggetto
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        # chiamato in automatico da print(strumento) nel main
        # :.2f = valore con 2 decimali (250.0 -> 250.00)
        return f"{self.codice}, {self.tipo}, {self.marca}, {self.anno_acquisto}, {self.valore:.2f}"