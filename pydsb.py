import requests


class PyDSB:
    URL = "https://iphone.dsbcontrol.de/iPhoneService.svc/DSB"

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.token = None

    def login(self):
        req = requests.get(f"{self.URL}/authid/{self.username}/{self.password}")
        token = req.text.strip("\"")

        if token == "00000000-0000-0000-0000-000000000000":
            raise LoginError("Wrong username or password")

        self.token = token


class LoginError(Exception):
    pass
