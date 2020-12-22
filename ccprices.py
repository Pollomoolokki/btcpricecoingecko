from pycoingecko import CoinGeckoAPI
import json
from datetime import datetime
import os

cg = CoinGeckoAPI() #tehdaan cg apista
t = datetime.now() #otetaan aika
t_string = t.strftime("%d/%m/%Y %H:%M:%S") #formatoidaan aika
#trackedcoins = ["bitcoin", "litecoin", "iota"]
#bitcoin = "bitcoin"
#litecoin = "litecoin"
usd = "usd"
#writecoins -aliohjelma kirjoittaa mahd. kolikot lyhenteina apicoins.txt tiedostoon
#ei tulosta mitaan jos txt olemassa
def writecoins():
    coins = open("apicoins.txt", "a")
    if(os.path.getsize("apicoins.txt") > 0):
        coins.close()
    else:
        supportedcoins = cg.get_coins_list()
        for scoins in supportedcoins:
            coins.write(scoins['name']+"\n")
            #print(scoins['name'])
        #print(supportedcoins[0])
        #coins.write(str(cg.get_supported_vs_currencies()))
        coins.close()
#writetofile kirjoittaa coins.txt -tiedostossa olevat kolikot erillisin tiedostoihin kolikko+prices.txt muodossa
#tulostaa kolikon nimen, hinnan(usd) ja ajan
def writetofile(coin, tradedcoin):
    coinname = coin+'prices.txt'
    cointext = open(coinname, "a")
    if(os.path.getsize(coinname) > 0):
            cointext.write("\n"+str(cg.get_price(ids=coin, vs_currencies=tradedcoin)) + " "+ t_string)
            cointext.close()
    else:
            cointext.write(str(cg.get_price(ids=coin, vs_currencies=tradedcoin)) + " "+ t_string)
            cointext.close()
#avaa coins.txt tiedoston ja poistaa newlinet
temp = open("coins.txt",'r').read().split('\n')
#kay lapi kolikot
for line in temp:
    writetofile(line, usd)
#writetofile(bitcoin, usd)
#writetofile(litecoin, usd)
writecoins()
