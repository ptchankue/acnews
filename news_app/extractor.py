from typing import Any, Dict

import requests
from bs4 import BeautifulSoup


class Extractor:
    def __init__(self, **kwargs: Dict[str:Any]) -> None:
        print("Extractor Constructor...")

    def parse_radio_okapi(self) -> None:
        url = "http://www.radiookapi.net/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, convertEntities=BeautifulSoup.HTML_ENTITIES)

        print("Parsing http://radiookapi.net")

        blocks = soup.findAll("h2")

        for a in blocks:
            for item in a.findAll("a"):
                print(item["href"])
                # print item.get('href') + "," + item.string
