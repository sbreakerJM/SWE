from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    # Erstellen eines Leistungstests
    supervisor = Supervisor("Max", "Mustermann", "1980-05-15")
    subject = Subject("Anna", "Musterfrau", "female", "1995-04-07")
    
    # Schätzen der maximalen Herzfrequenz
    max_hr = subject.estimate_max_hr()
    print(f"Geschätzte maximale Herzfrequenz für {subject.first_name} {subject.last_name}: {max_hr}")

    experiment = Experiment("Leistungstest", "2025-04-07")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    # Experiment anzeigen
    print(experiment)