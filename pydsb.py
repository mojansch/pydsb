class PyDSB:
    URL = "https://iphone.dsbcontrol.de/iPhoneService.svc/DSB"

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.token = None
