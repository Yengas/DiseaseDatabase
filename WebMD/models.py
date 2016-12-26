class Symptom(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def conditions(self):
        self.mConditions()

    def addCondition(self, condition):
        self.mConditions.append(condition)

class BodyPart(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mSymptoms = []

    def symptoms(self):
        return self.mSymptoms
    def addSymptom(self, symptom):
        self.mSymptoms.append(symptom)

class Condition(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
