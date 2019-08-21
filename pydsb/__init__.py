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

    def get_plans(self):
        req = requests.get(f"{self.URL}/timetables/{self.token}")
        items = req.json()

        return [
            {"is_html": item["ishtml"],
             "uploaded_date": item["timetabledate"],
             "group": item["timetablegroupname"],
             "title": item["timetabletitle"],
             "url": item["timetableurl"]} for item in items
        ]

    def get_news(self):
        req = requests.get(f"{self.URL}/news/{self.token}")
        items = req.json()

        return [
            {
                "headline": item["headline"],
                "news_date": item["newsdate"],
                "id": item["newsid"],
                "image_url": item["imageurl"],
                "short_message": item["shortmessage"],
                "message": item["wholemessage"]
            } for item in items if item["newsid"] != "00000000-0000-0000-0000-000000000000"
        ]


class LoginError(Exception):
    pass
