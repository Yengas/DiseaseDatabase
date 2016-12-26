import json
import sys
import os

# Adds given part to a list.
def add_part(parts, part):
    parts.append(part)

# Finds the given part from a list of parts.
def find_by_id(parts, id):
    return next(filter(lambda part: part.id == id, parts))

# Read a file in the data folder and parse as json.
def readData(file):
    with open('./data/%s' % (file)) as file:
        return json.loads(file.read())

# returns bodypart and id by parsing filename
def getBodyPart(filename):
    split = os.path.splitext(filename)[0].split('-')
    return {'id': int(split[-1]), 'name': ' '.join(split[:-1]) }

def downloadSymptoms(api, directory='./output/symptoms'):
    body_parts = readData('body_parts.json')
    # Create the folder recursively if it doesn't exists
    os.makedirs(directory, exist_ok=True)

    # Download data for each of the body part.
    for id, part in body_parts.items():
        # Convert id to int.
        id = int(id)

        sys.stdout.write("Downloading symptom data for %s(%d): " % (part, id))
        response = api.symptoms(id)
        if response.status_code != 200:
            print("Failed.")
        else:
            file = open(os.sep.join((directory, "%s-%d.json" % (part, id))), "w");
            file.write(response.text)
            print("Ok.")

def downloadConditions(api, directory='./data/symptoms', outDirectory='./output/conditions'):
    # Create output directory if not exists
    os.makedirs(outDirectory, exist_ok=True)
    # Read each of the ffiles in the symptoms directory
    for file in os.listdir(directory):
        # Pass if not a file
        if not os.path.isfile(os.path.join(directory, file)):
            continue
        # Read the symptoms file as json
        data = readData(os.sep.join(('symptoms', file)))
        # Get the body part from the file name
        bodypart = getBodyPart(file)

        # Download conditions for each body part.
        for symptom in data['data']['symptoms']:
            sys.stdout.write('Downloading condition data for %s(%d) with `%s`(%d): ' % (bodypart['name'], bodypart['id'], symptom['nm'], symptom['id']))
            response = api.conditions([ api.make_symptom(bodypart['id'], [int(symptom['id'])]) ])

            if response.status_code != 200:
                print("Failed.");
            else:
                result = response.json()
                result['meta'] = { 'bodypart': { 'name': bodypart['name'], 'id': bodypart['id'] }, 'symptom': [{ 'name': symptom['nm'], 'id': symptom['id'] }]}
                with open(os.path.join(outDirectory, "%d-%d.json" % (bodypart['id'], symptom['id'])), "w") as outFile:
                    json.dump(result, outFile)
                print("Ok.");