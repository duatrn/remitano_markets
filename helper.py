from functools import total_ordering
from typing import Dict, Any
import json
import platform
import locale

class Helper:
    @classmethod
    def loadConfig(cls) -> Dict: # load json configuration file
        with open("configs.json") as f:
            return json.load(f)

    @classmethod
    def localeSetting(cls) -> None:
        if platform.system() == "Windows":
            locale.setlocale(locale.LC_ALL, "vi_VN") # for windows only
        else:
            locale.setlocale(locale.LC_ALL, "vi_VN.TVCN") # for other OS

    @classmethod
    def menuChoiceInputValidation(cls) -> Any: # Validation choice input
        config = Helper.loadConfig()
        totalAppFunctions = config["TOTAL_APP_FUNCTIONS"]
        exitShortcut = config["EXIT_SHORTCUT"]
        while True:
            try:
                choice = input("Your choice: ")
                if int(choice) > totalAppFunctions or int(choice) <= 0:
                    print(f"Pls input from 1 to {totalAppFunctions}")
                else:
                    return choice
            except ValueError:
                if choice == exitShortcut:
                    return choice
                print("ERROR!!! INVALID INPUT")

    @classmethod
    def cryptoInputValidation(cls) -> str: # Validation crypto input
        config = Helper.loadConfig()
        cryptoValid = False
        while not cryptoValid:
            print("Crypto are now available: BTC, ETH, BCH, LTC, XRP, USDT")
            crypto = input("Your crypto currency: ").upper()
            if crypto not in config["LIST_CRYPTO_CURRENCIES"]:
                print("Invalid crypto")
            else:
                cryptoValid = True
        return crypto

    @classmethod
    def tradeActionInputValidation(cls) -> bool: # validation trading action input (buy or sell)
        while True:
            try: 
                action = int(input("Do you want to buy(1) or sell(0)? "))
                if action < 0 or action > 1:
                    print("Must be 0 or 1...")
                else:
                    return bool(action)
            except ValueError:
                print("Must be integer...")

    @classmethod
    def quantityInputValidation(cls) -> float: # validation quan input
        while True:
            try:
                return float(input("How much do you want to trade? "))
            except ValueError:
                print("Must be number...")