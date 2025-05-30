from easygui import buttonbox, msgbox

# Tegelase ja vaenlase klassid
class Karakter:
    def __init__(self, nimi, elud, tugevus):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kogus):
        self.elud -= kogus
        if self.elud < 0:
            self.elud = 0

class Vaenlane(Karakter):
    pass

# Labürindi andmestruktuur
laburint = {
    "start": {"edasi": "koht1"},
    "koht1": {"tagasi": "start", "vasakule": "koht2", "paremale": "koht3"},
    # Vasak
    "koht2": {"edasi": "koht4", "paremale": "koht5"},
    "koht4": {"tagasi": "koht2"},
    "koht5": {"paremale": "koht8"},
    "koht8": {"edasi": "koht9"},
    "koht9": {"edasi": "koht10"},
    "koht10": {"tagasi": "koht9"},
    # Parem
    "koht3": {"vasakule": "koht10", "edasi": "koht11"},
    "koht11": {"vasakule": "koht13", "paremale": "koht12"},
    "koht13": {"tagasi": "koht11"},
    "koht12": {"tagasi": "koht11"},
}

# Peamine mängufunktsioon
def alusta_mang():
    # Mängija ja vaenlaste seadistamine
    tegelane = Karakter("Mängija", elud=10, tugevus=3)
    vaenlased = {
        "koht4": Vaenlane("Vaenlane1", elud=10, tugevus=5),
        "koht10": Vaenlane("Vaenlane2", elud=10, tugevus=5),
        "koht12": Vaenlane("Vaenlane3", elud=10, tugevus=5),
        "koht13": Vaenlane("Vaenlane4", elud=3, tugevus=2),
    }
    esemed = {"koht9": "võtmed", "koht13": "kaart"}

    positsioon = "start"
    while True:
        # Valikud ja sõnum
        valikud = laburint[positsioon].keys()
        valik = buttonbox(
            f"Oled kohas: {positsioon}\nElud: {tegelane.elud}\nMida soovid teha?",
            choices=list(valikud),
        )

        if not valik:
            break  # Mängija sulgeb akna

        uus_positsioon = laburint[positsioon].get(valik)
        if uus_positsioon:
            positsioon = uus_positsioon
            msgbox(f"Liikusid {positsioon}.")
        else:
            msgbox("Sinna ei saa minna!")
            continue

        # Esemete leidmine
        if positsioon in esemed:
            ese = esemed.pop(positsioon)
            msgbox(f"Leidsid eseme: {ese}!")

        # Vaenlasega kohtumine
        if positsioon in vaenlased:
            vaenlane = vaenlased[positsioon]
            msgbox(f"Kohtusid vaenlasega: {vaenlane.nimi}! Ta ründab sind!")
            
            # Võitlus
            tegelane.kaotaElusi(vaenlane.tugevus)
            vaenlane.kaotaElusi(tegelane.tugevus)
            if tegelane.elud <= 0:
                msgbox("Sa surid! Mäng on läbi.")
                break
            if vaenlane.elud <= 0:
                msgbox(f"Alistasid vaenlase: {vaenlane.nimi}!")
                del vaenlased[positsioon]

    msgbox("Mäng lõppes. Aitäh mängimast!")

# Programmi käivitamine
if __name__ == "__main__":
    try:
        alusta_mang()
    finally:
        msgbox("Mäng suletakse. Head aega!")
