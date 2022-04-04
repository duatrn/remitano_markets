import locale
import sys
import platform

from helper import Helper
from appFunctions import AppFunctions

class Menu:
    def __init__(self) -> None:
        Helper.localeSetting()
        self.config = Helper.loadConfig()
        self.choice = -1

    def menuIntro(self) -> None:
        print("--- OFFER FROM REMITANO ---")
        print("1 - Show best offers")
        print("2 - Offer crypto quantity")
        print("Press e to exit")
    
    def menuChoice(self) -> str:
        self.choice = Helper.menuChoiceInputValidation()

    def menuFunctions(self) -> None:
        # exit app
        if self.choice == "e":
            sys.exit("Bye")

        # Validation crypto input
        crypto = Helper.cryptoInputValidation()

        if self.choice == "1":
            bestOffers = AppFunctions.getBestOffer(crypto=crypto)
            print(f"Bid: {locale.currency(bestOffers[crypto][0], grouping=True)}")
            print(f"Ask: {locale.currency(bestOffers[crypto][1], grouping=True)}")
        elif self.choice == "2":
            # validation trading action input (buy or sell)
            action = Helper.tradeActionInputValidation()
            # validation quan input
            quan = Helper.quantityInputValidation()
            price = AppFunctions.offerPrice(action=action, crypto=crypto, quan=quan)
            print(locale.currency(price, grouping=True))

    @classmethod
    def show(cls) -> None:
        menu = Menu()
        while True:
            menu.menuIntro()
            menu.menuChoice()
            menu.menuFunctions()