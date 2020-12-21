from pycoingecko import CoinGeckoAPI
import json
from datetime import datetime
import os

cg = CoinGeckoAPI()
t = datetime.now()
t_string = t.strftime("%d/%m/%Y %H:%M:%S")
bitcoin = "bitcoin"
litecoin = "litecoin"
usd = "usd"
def writecoins():
    coins = open("coins.txt", "a")
    done = open("coinsalreadywritten.txt", "a")
    if(os.path.getsize("coins.txt") > 0):
        donothing = 0
        #coinsalreadywritten.write("")
    else:
        coins.write(str(cg.get_supported_vs_currencies()))
def writetofile(coin, tradedcoin):
    coinname = coin+"prices.txt"
    cointext = open(coinname, "a")
    if(os.path.getsize(coinname) > 0):
            cointext.write("\n"+str(cg.get_price(ids=coin, vs_currencies=tradedcoin)) + " "+ t_string)
    else:
            cointext.write(str(cg.get_price(ids=coin, vs_currencies=tradedcoin)) + " "+ t_string)


writetofile(bitcoin, usd)
writetofile(litecoin, usd)

writecoins()
