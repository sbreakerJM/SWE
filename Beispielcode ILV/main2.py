class Sensor():
    
    #Konstruktor

    def __init__(self, id : str):
        self.id = id
        self.messwert = None
        self.messwerte = []
        self.__passwort = "123456"

    def measure(self, messwert):
        self.messwert = messwert
        self.messwerte.append(self.messwert)

    def calc_mean(self):
        self.mittelwert = sum(self.messwerte) / len(self.messwerte)
        return self.mittelwert
    
    def get_passwort(self, superpasswort):
        if superpasswort == "bier":
            return self.__passwort
        
    def set_passwort(self, neues_passwort, superpasswort):
        if superpasswort == "bier":
            self.__passwort = neues_passwort

        return self.__passwort
    
    def reset(self, passwort):
        if passwort == self.__passwort:
            print("Auf Werkeinstellungen zurückgesetzt")
            self.messwert = None
            self.messwerte = []
        else:
            print("Passwort falsch")

if __name__ == "__main__":
    s1 = Sensor("123")
    print(s1.id)
    s1.measure(10)
    s1.measure(20)
    s1.measure(30)
    s1.calc_mean()
    das_passwort = s1.__passwort
    print(s1.__dict__)
    s1.reset(das_passwort)
    s1.set_passwort("bier", "test")
    print(s1.get_passwort("bier"))