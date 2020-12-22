from pycoingecko import CoinGeckoAPI
import json
from datetime import datetime
import os

cg = CoinGeckoAPI() #tehdaan cg apista
t = datetime.now() #otetaan aika
t_string = t.strftime("%d/%m/%Y %H:%M:%S") #formatoidaan aika
usd = "usd"
#writecoins -aliohjelma kirjoittaa kaikki mahd. kolikot apicoins.txt tiedostoon
#ei tulosta mitaan jos txt olemassa
def writecoins():
    coins = open("apicoins.txt", "a")
    if(os.path.getsize("apicoins.txt") > 0):
        coins.close()
    else:
        supportedcoins = cg.get_coins_list() #otetaan lista kolikoita
        for scoins in supportedcoins: #kaydaan lapi listaa yksi kerrallaan
            coins.write(scoins['name']+"\n") #kirjoitetaan kolikon nimi + newline
        coins.close() #suljetaan txt-tiedosto
#writetofile kirjoittaa coins.txt -tiedostossa olevat kolikot erillisin tiedostoihin kolikko+prices.txt muodossa
#tulostaa kolikon nimen, hinnan(usd) ja ajan
def writetofile(coin, tradedcoin):
    coinname = coin+'prices.txt' #annetaan kolikkotiedostolle nimi
    cointext = open(coinname, "a") #avataan tiedosto
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
writecoins()
