import uuid
from typing import Dict
import re
import requests
from dataclasses import dataclass, field
from bs4 import BeautifulSoup
from models.model import Model


@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default="items")
    url: str
    tag_name: str
    query: Dict
    price: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def load_price(self) -> float:
        request = requests.get(self.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"})
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        elem = element.text
        print(elem)
        expression = "([0-9,.]+)"
        matches = re.search(expression, elem)
        print(matches)
        found_price = matches.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)

        return self.price

    """
    def load_price(self):
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d*\.\d\d)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)

        return self.price
    """

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query,
            "price": self.price
        }
