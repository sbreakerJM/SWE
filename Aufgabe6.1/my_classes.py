class Subject:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def estimate_max_hr(self):
       
        if self.sex.lower() == 'male':
            self.max_hr = 220 - self.age
        elif self.sex.lower() == 'female':
            self.max_hr = 226 - self.age
        else:
            raise ValueError('Ungültiges Geschlecht. Bitte "male" oder "female" verwenden.')
        return self.max_hr


class Supervisor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


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