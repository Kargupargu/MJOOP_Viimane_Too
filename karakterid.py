class Karakter:
    def __init__(self, nimi, elud, tugevus):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kaotus):
        self.elud -= kaotus
        if self.elud < 0:
            self.elud = 0

    def lisaElusi(self, juurde):
        self.elud += juurde


class Vaenlane:
    def __init__(self, elud, tugevus):
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kaotus):
        self.elud -= kaotus
        if self.elud < 0:
            self.elud = 0