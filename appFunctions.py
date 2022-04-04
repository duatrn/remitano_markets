from typing import Dict

from api import Api

class AppFunctions:
    @classmethod
    def getBestOffer(cls, crypto: str) -> Dict:
        r = Api().getOrders(crypto)
        bestBid = r["bids"][0][0]
        bestAsk = r["asks"][0][0]
        return {crypto: [bestBid, bestAsk]}

    @classmethod
    # action: True - buy (using ask price), False - sell (using bid price)
    def offerPrice(cls, action: bool, crypto: str, quan: float) -> float:
        bestOffer = AppFunctions.getBestOffer(crypto)
        if action:
            return quan * bestOffer[crypto][1] # buy price
        else:
            return quan * bestOffer[crypto][0] # sell price