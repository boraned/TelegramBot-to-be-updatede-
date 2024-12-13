from bs4 import BeautifulSoup
import requests
import re

#Coin Market Cap
coinmarketcap = requests.get("https://coinmarketcap.com/")
coinmarketcapSoup = BeautifulSoup(coinmarketcap.text, "html.parser")


def CoinMarketCapInfo():
    coinmarketcapCoinNames = coinmarketcapSoup.findAll("p", attrs={"class" : "sc-65e7f566-0 iPbTJf coin-item-name"})
    coinmarketcapCoinPrices = coinmarketcapSoup.findAll("div", attrs={"class" : re.compile(r"sc-b3fc6b7-0 dzgUIj( rise| fall)?" )})

    txt = ""
    for coinName, price in zip(coinmarketcapCoinNames, coinmarketcapCoinPrices):
        txt += f"{coinName.text}:{price.text}\n"
    return txt


#Coin Desk
#coindesk = requests.get("https://www.coindesk.com/price")
#coindeskSoup = BeautifulSoup(coindesk.text, "html.parser")
#
#def CoinDeskInfo():
#    coindeskCoinNames = coindeskSoup.findAll("h5", attrs={"class": "Noto_Sans_sm_Sans-600-sm text-color-black "})
#    coindeskPrices = coindeskSoup.findAll("h5", attrs={"class": "Noto_Sans_Mono_sm_Mono-400-sm text-color-black "})
#
#
#    txt = ""
#    for coinName, price in zip(coindeskCoinNames, coindeskPrices):
#        txt += f"{coinName.text}:{price.text}\n"
#    return txt


def GatherAll() -> str:
    return f"CoinMarketCap Info:\n\n{CoinMarketCapInfo()}"

