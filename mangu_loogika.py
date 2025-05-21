from karakterid import Karakter, Vaenlane
import easygui

laburint = {
    "start": {"edasi": "koht1"},
    "koht1": {"tagasi": "start", "vasakule": "koht2", "paremale": "koht3"},
    #Vasak
        "koht2": {"edasi": "koht4", "paremale": "koht5"},
        "koht4": {"tagasi": "koht2"},
        "koht5": {"paremale": "koht8"},
        "koht8": {"edasi": "koht9"},
        "koht9": {"edasi": "koht10"},
        "koht10": {"tagasi": "koht9"},
    #Parem
        "koht3": {"vasakule": "koht10", "edasi": "koht11"},
        "koht11": {"vasakule": "koht13", "paremale": "koht12"},
        "koht13": {"tagasi": "koht11"},
        "koht12": {"tagasi": "koht11"}

}

def alusta_mang():
    tegelane = Karakter("Mängija", elud=10, tugevus=3)
    vaenlased = {
        "koht4": Vaenlane(elud=10, tugevus=5),
        "koht10": Vaenlane(elud=10, tugevus=5),
        "koht12": Vaenlane(elud=10, tugevus=5),
        "koht13": Vaenlane(elud=3, tugevus=2),

    }
    
    positsioon = "start"
    while True:
        valikud = laburint[positsioon].keys()
        valik = easygui.buttonbox(
            "Oled kohas: {positsioon}\nMida teed?",
            choices=list(valikud),
        )

        if not valik:
            break  
        uus_positsioon = laburint[positsioon].get(valik)
        if uus_positsioon:
            positsioon = uus_positsioon
            easygui.msgbox("Liikusid {uus_positsioon}.")
        else:
            easygui.msgbox("Sinna ei saa minna!")

        if positsioon in vaenlased:
            vaenlane = vaenlased[positsioon]
            easygui.msgbox("Kohtusid vaenlasega! Ta ründab sind!")
            
            tegelane.kaotaElusi(vaenlane.tugevus)
            vaenlane.kaotaElusi(tegelane.tugevus)
            
            if tegelane.elud <= 0:
                easygui.msgbox("Sa surid!")
                exit()
            
            if vaenlane.elud <= 0:
                easygui.msgbox("Vaenlane suri! Palju õnne oled pääsenud")
                del vaenlased[positsioon]
if __name__ == "__main__":
    try:
        alusta_mang()
    finally:
        import easygui
        easygui.msgbox("Mäng lõppes. Vajuta OK, et sulgeda.")
