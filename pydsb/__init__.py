import requests

BASE_URL = "https://mobileapi.dsbcontrol.de"


class PyDSB:
    def __init__(self, username: str = None, password: str = None):

        params = {
            "bundleid": "de.heinekingmedia.dsbmobile",
            "appversion": "35",
            "osversion": "22",
            "pushid": "",
            "user": username,
            "password": password
        }
        
        r = requests.get(BASE_URL + "/authid", params=params)

        if r.text == "\"\"": # Me when http status code is always 200 :trollface:
            raise Exception("Invalid Credentials")
        else:
          self.token = r.text.replace("\"", "")

    def get_plans(self) -> list:
        raw_plans = requests.get(BASE_URL + "/dsbtimetables", params={"authid": self.token}).json()
        plans = []

        for plan in raw_plans:
            for i in plan["Childs"]:
                  plans.append({
                        "id": i["Id"],
                        "is_html": True if i["ConType"] == 6 else False,
                        "uploaded_date": i["Date"],
                        "title": i["Title"],
                        "url": i["Detail"],
                        "preview_url": "https://light.dsbcontrol.de/DSBlightWebsite/Data/" + i["Preview"],
                    }
                )

        return plans

    def get_news(self) -> list:
        raw_news = requests.get(BASE_URL + "/newstab", params={"authid": self.token}).json()
        news = []
        for i in raw_news:
            news.append({
                "title": i["Title"], "date": i["Date"], "content": i["Detail"]
            })
        return news

    def get_postings(self) -> list:
        raw_postings = requests.get(BASE_URL + "/dsbdocuments", params={"authid": self.token}).json()
        postings = []
        for posting in raw_postings:
            for i in posting["Childs"]:
                postings.append({
                        "id": i["Id"],
                        "uploaded_date": i["Date"],
                        "title": i["Title"],
                        "url": i["Detail"],
                        "preview_url": "https://light.dsbcontrol.de/DSBlightWebsite/Data/" + i["Preview"],
                    }
                )

        return postings
