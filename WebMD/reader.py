import os
import json
from .models import *
from .helpers import getBodyPart

# Adds given part to a list.
def addPart(parts, part):
    parts.append(part)

# Finds the given part from a list of parts.
def findPart(parts, id):
    return next(filter(lambda part: part.id == id, parts))

# Reads a given database of json files to retrieve a oop database
def readDatabase(folder):
    symptomPath = os.path.sep.join((folder, 'symptoms'))
    partsPath = os.path.sep.join((folder, 'body_parts.json'))
    parts = []

    # Open the parts file.
    with open(partsPath, "r") as partsFile:
        partsObject = json.load(partsFile)
        # Put each part to the parts arr by parsing to an object
        for k, v in partsObject.items():
            addPart(parts, BodyPart(id=int(k), name=v))

    # List symptoms directory to get each symptom
    for symptomFilePath in os.listdir(symptomPath):
        # Find the body part name and id from the file name
        part = getBodyPart(symptomFilePath)
        # Find the part from the parts array by the id defined in file
        part = findPart(parts, int(part['id']))

        # Open the file
        with open(os.sep.join((symptomPath, symptomFilePath))) as symptomFile:
            symptomsObject = json.load(symptomFile)
            # Put each symptom to its corresponding body part.
            for symptom in symptomsObject['data']['symptoms']:
                part.addSymptom(Symptom(id=symptom['id'], name=symptom['nm']))

    return parts
