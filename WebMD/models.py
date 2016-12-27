class Symptom(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mConditions = []

    def conditions(self):
        return self.mConditions

    def add_condition(self, condition):
        self.mConditions.append(condition)

    def __eq__(self, other):
        return self.id == other.id

class BodyPart(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mSymptoms = []

    def symptoms(self):
        return self.mSymptoms
    def add_symptom(self, symptom):
        self.mSymptoms.append(symptom)

    def __eq__(self, other):
        return self.id == other.id;

class Condition(object):
    def __init__(self, id, name, about):
        self.id = id
        self.name = name
        self.about = about
        self.weight = 0

    def add_weight(self):
        self.weight += 1

    def __eq__(self, other):
        return self.id == other.id;