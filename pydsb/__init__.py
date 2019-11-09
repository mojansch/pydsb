import base64
import datetime
import gzip
import io
import json
import uuid

import requests


class PyDSB:
    URL = "https://app.dsbcontrol.de/JsonHandler.ashx/GetData"

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def fetch_data(self):
        time = datetime.datetime.now().isoformat()
        time = time.split(".")[0] + "." + time.split(".")[1][:3] + "Z"

        data = {
            "UserId": self.username,
            "UserPw": self.password,
            "AppVersion": "2.5.9",
            "Language": "de",
            "OsVersion": "27 8.1.0",
            "AppId": str(uuid.uuid4()),
            "Device": "Pixel 3",
            "BundleId": "de.heinekingmedia.dsbmobile",
            "Date": time,
            "LastUpdate": time,
        }

        stream = io.BytesIO()
        with gzip.open(filename=stream, mode="wt") as stream_gz:
            stream_gz.write(json.dumps(data))
        req = requests.post(
            "https://app.dsbcontrol.de/JsonHandler.ashx/GetData",
            json={
                "req": {
                    "Data": base64.encodebytes(stream.getvalue()).decode("utf-8"),
                    "DataType": 1,
                }
            },
        )

        returndata = json.loads(
            gzip.decompress(base64.b64decode(json.loads(req.text)["d"]))
        )

        plans = [
            item
            for item in returndata["ResultMenuItems"][0]["Childs"]
            if item["Title"] == "Pläne"
        ]
        news = [
            item
            for item in returndata["ResultMenuItems"][0]["Childs"]
            if item["Title"] == "News"
        ]

        return {"plans": plans, "news": news}

    def get_plans(self):
        try:
            raw_plans = self.fetch_data()["plans"][0]["Root"]["Childs"]
        except IndexError:
            return []
        plans = []
        for plan in raw_plans:
            for i in plan["Childs"]:
                plans.append(
                    {
                        "is_html": True if i["ConType"] == 3 else False,
                        "uploaded_date": i["Date"],
                        "title": i["Title"],
                        "url": i["Detail"],
                        "preview_url": "https://app.dsbcontrol.de/data/" + i["Preview"],
                    }
                )

        return plans

    def get_news(self):
        try:
            raw_news = self.fetch_data()["news"][0]["Root"]["Childs"]
        except IndexError:
            return []
        news = []
        for i in raw_news:
            news.append(
                {"title": i["Title"], "date": i["Date"], "content": i["Detail"]}
            )

        return news

