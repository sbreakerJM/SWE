#Klassen übergeben
class Pferd():
    #Konstruktor
    def __init__(self, meine_größe, mein_name):
        print("Hier wird ein Pferd erstellt")
        print("Das Pferd ist ", meine_größe, " groß")

        #Das erste Attribut hinzufügen
        self.größe = meine_größe
        self.name = mein_name

    def sich_vorstellen(self):
        print("Hallo, ich bin ", self.name, " und bin ", self.größe, " groß")

    def laufen(self, meine_geschwindigkeit):
        self.geschwindigkeit = meine_geschwindigkeit
        return "Ich laufe mit ", self.geschwindigkeit, " km/h"
        

#Instanzierung eines Objekts
#Self müssen wir nie übergeben, das macht Python automatisch
pf1 = Pferd("1,70 m", "Niki")
pf2 = Pferd("1,30 m", "Mo")

pf1.sich_vorstellen()
pf2.sich_vorstellen()

print(pf1.laufen("30"))
print(pf2.laufen("40"))