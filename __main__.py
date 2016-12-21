import json
import sys
import os
from WebMD import webmd

def readData(file):
   with open('./data/%s.json' % (file)) as file:
       return json.loads(file.read())

def downloadSymptoms(api, directory='./output/symptoms'):
    body_parts = readData('body_parts')
    # Create the folder recursively if it doesn't exists
    os.makedirs(directory, exist_ok=True)

    # Download data for each of the body part.
    for id, part in body_parts.items():
        # Convert id to int.
        id = int(id)

        sys.stdout.write("Downloading data for %s(%d): " % (part, id))
        response = api.symptoms(id)
        if response.status_code != 200:
            print("Failed.")
        else:
            file = open(os.sep.join((directory, "%s-%d.json" % (part, id))), "w");
            file.write(response.text)
            print("Ok.")


if __name__ == "__main__":
    api = webmd.API()
    downloadSymptoms(api)
