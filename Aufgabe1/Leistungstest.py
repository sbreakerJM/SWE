from datetime import date
from typing import List, Dict, Union

def create_experiments(first_experiment_id: Union[int, float, str]) -> List[Dict[str, Union[int, str]]]:
    experiments = []
    try:
        first_experiment_id = int(first_experiment_id)
        for i in range(10):
            experiment = {
                "ID": first_experiment_id + i,
                "Name": f"Experiment {i+1}",
                "Date": str(date.today()),
                "Researcher": "Samuel B."
            }
            experiments.append(experiment)
    except ValueError:
        print("Error")

    return experiments

first_experiment_id = 10
experiments = create_experiments(first_experiment_id)

for exp in experiments[:5]:
    print(exp)

even_id_count = sum(1 for exp in experiments if exp["ID"] % 2 == 0)
print(f"Anzahl gerade Experimente: {even_id_count}")
