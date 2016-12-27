from WebMD.reader import readDatabase
from WebMD.diagnose import SimpleDiagnoser

if __name__ == "__main__":
    parts = readDatabase('./data')
    picked = [parts[0].symptoms()[1], parts[2].symptoms()[1]]
    diagnoser = SimpleDiagnoser()

    for symptom in picked:
        diagnoser.update(symptom)

    conditions = diagnoser.diagnose()
    for condition in conditions:
        print(condition.id, condition.name, condition.weight, condition.about)
