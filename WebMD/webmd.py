# -*- coding: utf-8 -*-
import json
import requests
import urllib.parse


class API(object):
    def __init__(self, protocol='http', host="symptoms.webmd.com", service="scapp/SymptomCheckerAPI.svc"):
        self.protocol = protocol
        self.host = host
        self.service = service

    def symptoms(self, bodypartid, age=20, gender="M"):
        url = self.make_endpoint('symptoms');
        payload = API.make_request_body({ "bodypartid": bodypartid }, age, gender)
        return API.make_request(url, payload);

    def conditions(self, symptoms):
        pass

    def make_endpoint(self, endpoint):
        self.base = urllib.parse.urljoin("%s://%s/" % (self.protocol, self.host), self.service)
        return self.base + '/' + endpoint;

    @staticmethod
    def make_request_body(dict, age, gender):
       body = { "locale": "us", "user": { "age": age, "gender": gender }}
       body.update(dict)
       return { "request": body }

    @staticmethod
    def make_request(url, payload):
        response = requests.post(url, json=payload)
        response.encoding = "utf-8-sig"
        return response

