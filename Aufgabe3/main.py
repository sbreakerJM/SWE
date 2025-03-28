if  __name__ =="__main__":
    
    from Aufgabe3.my_functions import build_person, build_experiment
    supervisor = build_person("Walter", "White", "Male", 50)
    subject = build_person("Jesse", "Pinkman", "Male", 27)
    experiment = build_experiment("Experiment 1", "2025-03-21", supervisor, subject)

    print(experiment)
    print("Test1")