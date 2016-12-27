import os
import json
from .models import *
from .helpers import getBodyPart, add_part, find_by_id

# Reads a given database of json files to retrieve a oop database
def readDatabase(folder):
    symptomPath = os.path.sep.join((folder, 'symptoms'))
    conditionPath = os.path.sep.join((folder, 'conditions'))
    partsPath = os.path.sep.join((folder, 'body_parts.json'))
    parts = []

    # Open the parts file.
    with open(partsPath) as partsFile:
        partsObject = json.load(partsFile)
        # Put each part to the parts arr by parsing to an object
        for k, v in partsObject.items():
            add_part(parts, BodyPart(id=int(k), name=v))

    # List symptoms directory to get each symptom
    for symptomFilePath in os.listdir(symptomPath):
        # Find the body part name and id from the file name
        part = getBodyPart(symptomFilePath)
        # Find the part from the parts array by the id defined in file
        part = find_by_id(parts, int(part['id']))

        # Open the file
        with open(os.sep.join((symptomPath, symptomFilePath))) as symptomFile:
            symptomsObject = json.load(symptomFile)
            # Put each symptom to its corresponding body part.
            for symptom in symptomsObject['data']['symptoms']:
                part.add_symptom(Symptom(id=symptom['id'], name=symptom['nm']))

    # List each condition and put them to the corresponding symptoms
    for conditionsFilePath in os.listdir(conditionPath):
        with open(os.sep.join((conditionPath, conditionsFilePath))) as conditionFile:
            conditions = json.load(conditionFile)
            if len(conditions['data']['conditions']) <= 0:
                continue
            # Find symptom by finding the body part first.
            symptoms = find_by_id(parts, int(conditions['meta']['bodypart']['id'])).symptoms()
            # Then call the same function to find symptom from that body part's symptoms.
            symptom = find_by_id(symptoms, int(conditions['meta']['symptom'][0]['id']))
            for condition in conditions['data']['conditions']:
                if not condition is None:
                    symptom.add_condition(Condition(id=condition['id'],name=condition['name'],about=condition['curl']))

    return parts
