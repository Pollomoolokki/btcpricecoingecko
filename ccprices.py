from pycoingecko import CoinGeckoAPI
import json
import time
from datetime import datetime
import os


cg = CoinGeckoAPI() #cg-object from the CoinGeckoAPI
t = datetime.now() #t-object for time
t_string = t.strftime("%d/%m/%Y %H:%M:%S") #format time d/m/Y H:M:S
#three fiats
usd = "usd"
eur = "eur"
btc = "Bitcoin"
#writecoins -subprogram asks the api for all available coins and writes them to apicoins.txt
#does nothing if apicoins.txt is found
#
def writecoins():
    coins = open("apicoins.txt", "a") #open apicoins.txt
    if(os.path.getsize("apicoins.txt") > 0): #check length, close if > 0
        coins.close()
    else:
        supportedcoins = cg.get_coins_list() #list of coins the api "supports"
        for scoins in supportedcoins: #do a for each loop over the coins
            coins.write(scoins['name']+"\n") #write coinname + newline
        coins.close() #close the .txt
#writetofile -subprogram writes coins,fiat,prices and date time
#reads the coins.txt one coin per line and writes "coinnameprices.txt" to disk
#adds to already found coinnameprices.txt -file
#coin - coinname from coins.txt
#usd - usd 
#euro - euro
#btc - btc
def writetofile(coin, usd, euro, btc):
    coinname = coin+'prices.txt' #name .txt for coinprices
    cointext = open(coinname, "a") #open .txt for coinprices
    if(os.path.getsize(coinname) > 0): #continue already found coinprices.txt 
#prints prices for 3 pairs. coin:usd coin:euro coin:btc
            cointext.write("\n"+str(cg.get_price(ids=coin, vs_currencies=usd))) #newline + coin:usd
            cointext.write(str(cg.get_price(ids=coin, vs_currencies=euro))) #coin:eur
            cointext.write(str(cg.get_price(ids=coin, vs_currencies="btc")) + " " + t_string) #coin:btc + date time
            cointext.close() #always close open io-streams
    else: #make a new coinprices.txt
#prints prices for 3 pairs. coin:usd coin:euro coin:btc
            cointext.write(str(cg.get_price(ids=coin, vs_currencies=usd)))
            cointext.write(str(cg.get_price(ids=coin, vs_currencies=euro)))
            cointext.write(str(cg.get_price(ids=coin, vs_currencies="btc"))+ " " + t_string)
            cointext.close() #always close open io-streams
#call writecoins to check/get apicoins.txt
writecoins()
#open coins.txt and remove newlines. makes empty prices.txt by 'accident'
temp = open("coins.txt",'r').read().split('\n')
#write all found coins from coins.txt to separate prices.txt files
for line in temp:
    writetofile(line, usd, eur, btc)
    time.sleep(10) #prevent timeout from api request
