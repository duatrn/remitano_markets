from typing import Any, Dict

import requests
from helper import Helper

class Api:
    def __init__(self) -> None:
        self.config = Helper.loadConfig()
        
    def getOrders(self, crypto: str) -> Any:
        # config = Helper.loadConfig()
        endPoint = f"{self.config['API_URL']}markets/{crypto}VND/order_book"
        return requests.get(endPoint).json()