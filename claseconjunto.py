class Conjunto:
    def __init__(self, elementos):
        self.elementos = set(elementos)

    def __add__(self, otro):
        return Conjunto(self.elementos.union(otro.elementos))

    def __sub__(self, otro):
        return Conjunto(self.elementos.difference(otro.elementos))

    def __eq__(self, otro):
        return self.elementos == otro.elementos

    def __str__(self):
        return str(self.elementos)
    