from typing import Dict
import requests
import locale
import platform
import sys
import json

def loadConfig() -> Dict:
    with open("configs.json") as f:
        return json.load(f)

def runSetings() -> None:
    print("Running settings...")
    # config locale 
    if platform.system() == "Windows":
        locale.setlocale(locale.LC_ALL, "vi_VN") # for windows only
    else:
        locale.setlocale(locale.LC_ALL, "vi_VN.TVCN") # for other OS
    print("Settings end...")

def getBestOffer(crypto: str) -> Dict:
    config = loadConfig()
    endPoint = f"{config['API_URL']}markets/{crypto}VND/order_book"
    r = requests.get(endPoint).json()
    bestBid = r["bids"][0][0]
    bestAsk = r["asks"][0][0]
    return {crypto: [bestBid, bestAsk]}

# action: True - buy (using ask price), False - sell (using bid price)
def offerPrice(action: bool, crypto: str, quan: float) -> float:
    bestOffer = getBestOffer(crypto)
    if action:
        return quan * bestOffer[crypto][1] # buy price
    else:
        return quan * bestOffer[crypto][0] # sell price

def menu() -> None:
    while True:
        config = loadConfig()
        print("--- OFFER FROM REMITANO ---")
        print("1 - Show best offers")
        print("2 - Offer price")
        print("Press e to exit")
        choice = input("Your choice: ")
        # exit app
        if choice == "e":
            sys.exit("Bye")

        cryptoValid = False
        while not cryptoValid:
            print("Crypto are now available: BTC, ETH, BCH, LTC, XRP, USDT")
            crypto = input("Your crypto currency: ")
            if crypto not in config["LIST_CRYPTO_CURRENCIES"]:
                print("Invalid crypto")
            else:
                cryptoValid = True
        if choice == "1":
            bestOffers = getBestOffer(crypto=crypto)
            print(f"Bid: {locale.currency(bestOffers[crypto][0], grouping=True)}")
            print(f"Ask: {locale.currency(bestOffers[crypto][1], grouping=True)}")
        elif choice == "2":
            actionValid = False
            while not actionValid:
                try: 
                    action = int(input("Do you want to buy(1) or sell(0)? "))
                    if action < 0 or action > 1:
                        print("Must be 0 or 1...")
                    else:
                        action = bool(action)
                        actionValid = True
                except ValueError:
                    print("Must be integer...")
            quan = float(input("How much do you want to trade? "))
            price = offerPrice(action=action, crypto=crypto, quan=quan)
            print(locale.currency(price, grouping=True))
        

def run() -> None:
    runSetings()
    menu()

if __name__ == "__main__":
    run()
    