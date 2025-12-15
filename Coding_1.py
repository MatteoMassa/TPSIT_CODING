import re

class EsprReg:
    """
    Classe che gestisce una espressione regolare
    e verifica se una stringa la rispetta.
    """

    def __init__(self, espressione_regolare: str):
        # Attributo privato
        self.espressione_regolare = espressione_regolare

    def set_regex(self, espressione_regolare: str):
        """
        Metodo che riceve in input l'espressione regolare
        """
        self.espressione_regolare = espressione_regolare

    def valida(self, stringa: str) -> str:
        """
        Metodo che verifica se la stringa rispetta la regex
        e restituisce 'match' o 'mismatch'
        """
        if re.fullmatch(self.espressione_regolare, stringa):
            return "match"
        else:
            return "mismatch"


def main():
    # Input da tastiera
    regex = input("Inserisci un'espressione regolare: ")
    testo = input("Inserisci una stringa da testare: ")

    # Istanza della classe
    espr = EsprReg(regex)

    # Test e stampa risultato
    risultato = espr.valida(testo)
    print(risultato)


if __name__ == 