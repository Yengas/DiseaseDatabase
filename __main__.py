from WebMD.webmd import API

if __name__ == "__main__":
    api = API()
    #print(api.conditions([api.make_symptom(14, [244, 45])]).text)
    #downloadConditions(api)
    print(api)
