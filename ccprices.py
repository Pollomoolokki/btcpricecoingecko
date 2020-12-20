from pycoingecko import CoinGeckoAPI
import json
from datetime import datetime
import os

cg = CoinGeckoAPI()
t = datetime.now()
t_string = t.strftime("%d/%m/%Y %H:%M:%S")
def writetofile():
    btcprice = open("btcprices.txt", "a")
    if(os.path.getsize("btcprices.txt") > 0):
            btcprice.write("\n"+str(cg.get_price(ids='bitcoin', vs_currencies='usd')) + " "+ t_string)
    else:
            btcprice.write(str(cg.get_price(ids='bitcoin', vs_currencies='usd')) + " "+ t_string)


writetofile()
