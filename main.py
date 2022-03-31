from typing import Dict
import requests
import locale

API_URL = "https://api.remitano.com/api/v1/"
LIST_CRYPTO_CURRENCIES = ["BTC", "ETH", "XRP", "LTC", "BCH", "USDT"]
LOCALE = "vi_VN" #for windows only
locale.setlocale(locale.LC_ALL, LOCALE)

def getBestOffer(crypto: str) -> Dict:
    if crypto in LIST_CRYPTO_CURRENCIES:
        endPoint = f"{API_URL}markets/{crypto}VND/order_book"
        r = requests.get(endPoint).json()
        bestBid = r["bids"][0][0]
        bestAsk = r["asks"][0][0]
        # print(f"Best bid: {locale.currency(bestBid, grouping=True, international=True)} | Best ask: {locale.currency(bestAsk, grouping=True, international=True)}")
        return {crypto: [bestBid, bestAsk]}
    else:
        print("Invalid crypto currency")

# choice: True - buy (using ask price), False - sell (using bid price)
def offerPrice(choice: bool, crypto: str, quan: float) -> float:
    bestOffer = getBestOffer(crypto)
    if choice:
        return quan * bestOffer[crypto][1]
    else:
        return quan * bestOffer[crypto][0]

def menu() -> None:
    print("--- OFFER FROM REMITANO ---")
    print("1 - Show best offers")
    print("2 - Offer price")
    choice = input("Your choice: ")
    print("Crypto are now available: BTC, ETH, BCH, LTC, XRP, USDT")
    crypto = input("Your crypto currency: ")
    if choice == "1":
        bestOffers = getBestOffer(crypto=crypto)
        print(f"Bid: {locale.currency(bestOffers[crypto][0], grouping=True)}")
        print(f"Ask: {locale.currency(bestOffers[crypto][1], grouping=True)}")
    if choice == "2":
        action = input("Do you want to buy(1) or sell(2)? ")
        quan = float(input("How much do you want to trade? "))
        if action == "1":
            buyPrice = offerPrice(choice=True, crypto=crypto, quan=quan)
            print(locale.currency(buyPrice, grouping=True))
        else:
            sellPrice = offerPrice(choice=False, crypto=crypto, quan=quan)
            print(locale.currency(sellPrice, grouping=True))
    else:
        print("Bye")


if __name__ == "__main__":
    # print("running")
    # print(getBestOffer("BTC"))
    # offerPrice = locale.currency(offerPrice(True, "BTC", 1), grouping=True)
    # print(offerPrice)
    menu()