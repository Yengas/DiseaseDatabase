from .helpers import find_by_id

class Diagnoser(object):
    '''
        Update the diagnoser with given symptom.
    '''
    def update(self, symptom):
       raise NotImplementedError('Diagnoser update not implemented!')

    '''
        Returns the current diagnoses for the updated Diagnoser instance.
    '''
    def diagnose(self):
        raise NotImplementedError('Diagnoser diagnose not implemented!')

class SimpleDiagnoser(Diagnoser):
    def __init__(self):
        super().__init__()
        self.conditions = []

    def update(self, symptom):
        for condition in symptom.conditions():
            try:
                other = self.conditions.index(condition)
                self.conditions[other].add_weight()
            except(ValueError):
                self.conditions.append(condition)
        self.conditions.sort(key=lambda x: x.weight, reverse=True)

    def diagnose(self):
        return self.conditions
