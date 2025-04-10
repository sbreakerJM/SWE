from datetime import datetime


class Person:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = datetime.strptime(birthdate, '%Y-%m-%d')

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.__birthdate.year - ((today.month, today.day) < (self.__birthdate.month, self.__birthdate.day))
        return age


class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate):
        super().__init__(first_name, last_name, birthdate)
        self.sex = sex

    def estimate_max_hr(self):
        age = self.calculate_age()
        if self.sex.lower() == 'male':
            self.max_hr = 220 - age
        elif self.sex.lower() == 'female':
            self.max_hr = 226 - age
        else:
            raise ValueError('Ungültiges Geschlecht. Bitte "male" oder "female" verwenden.')
        return self.max_hr


class Supervisor(Person):
    def __init__(self, first_name, last_name, birthdate):
        super().__init__(first_name, last_name, birthdate)


class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subjects = []
        self.supervisors = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_supervisor(self, supervisor):
        self.supervisors.append(supervisor)

    def __str__(self):
        return f"Experiment: {self.name} am {self.date}\nBetreuer: {[sup.first_name + ' ' + sup.last_name for sup in self.supervisors]}\nProbanden: {[sub.first_name + ' ' + sub.last_name for sub in self.subjects]}"
