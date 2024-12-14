from bs4 import BeautifulSoup
import requests
import re


#Coin Market Cap

def CoinMarketCapInfo():
    coinmarketcap = requests.get("https://coinmarketcap.com/")
    coinmarketcapSoup = BeautifulSoup(coinmarketcap.text, "html.parser")

    coinmarketcapCoinNames = coinmarketcapSoup.findAll("p", attrs={"class" : "sc-65e7f566-0 iPbTJf coin-item-name"})
    coinmarketcapCoinPrices = coinmarketcapSoup.findAll("div", attrs={"class" : re.compile(r"sc-b3fc6b7-0 dzgUIj( rise| fall)?" )})
    txt = ""
    for coinName, price in zip(coinmarketcapCoinNames, coinmarketcapCoinPrices):
        txt += f"{coinName.text}:{price.text}\n"
    return txt
