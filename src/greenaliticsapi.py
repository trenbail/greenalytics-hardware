"""
Here is where the the interface for the API will be.
"""
import requests


class APIInterface:
    def __init__(self):
        self.url = None
        self.session = requests.Session()

    def post(self, url, data):
        self.session.post(url, json=data)

    def get_session(self):
        return self.session
