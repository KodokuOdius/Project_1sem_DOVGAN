import requests as req
import json
from main import DB as db
from random import randint as rnd, \
                    choice as ch


with open("./DB/countries.json", "r", encoding="utf-8") as _json:
    countries = json.load(_json)

for i in range(100):
    country = ch(countries)

    data_person = req.get(
        "https://api.randomdatatools.ru",
        params={
            "unescaped": "false",
            "typeName": "all",
            "params" : "LastName,Phone"
        }
    ).json()

    db().insert_data(
        surname=data_person["LastName"],
        phone=data_person["Phone"].replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("+", ""),
        country=country["country"],
        region=country["continent"],
        duration=rnd(30, 365*2),
        cost=rnd(10000, 500000)
    )

    print(f"Insert {i+1} datum")