from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    # Erstellen eines Leistungstests
    supervisor = Supervisor("Max", "Mustermann")
    subject = Subject("Anna", "Musterfrau", "female", 30)
    
    # Schätzen der maximalen Herzfrequenz
    max_hr = subject.estimate_max_hr()
    print(f"Geschätzte maximale Herzfrequenz für {subject.first_name} {subject.last_name}: {max_hr}")

    experiment = Experiment("Leistungstest", "2025-04-07")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    # Experiment anzeigen
    print(experiment)
