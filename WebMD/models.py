class Symptom(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mConditions = []

    def conditions(self):
        return self.mConditions

    def add_condition(self, condition):
        self.mConditions.append(condition)

class BodyPart(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mSymptoms = []

    def symptoms(self):
        return self.mSymptoms
    def add_symptom(self, symptom):
        self.mSymptoms.append(symptom)

class Condition(object):
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url
