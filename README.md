# btcpricecoingecko
Prints out cryptocurrency prices to a text file. Uses USD,EUR and Bitcoin as FIAT


Needs the goingecko api!
https://github.com/man-c/pycoingecko

Prints apicoins.txt
Bitcoinprices.txt
coins.txt file is read on usage. Copy coins from apicoins.txt to coins.txt one per line to specify which coin prices to print. Default is Bitcoin


USAGE:
python3 ccprices.py

as a cronjob
38 13 * * * cd /path/to/directory/btcpricecoingecko/ && /usr/bin/python3 ccprices.py > /tmp/ccprices.log 2>&1

everyday at 13:38. Prints console output to /tmp/ccprices.log

Output from the program can be imported to a spreadsheet
Output: JSON with 3 pairs + DATE TIME. Pairs: coinname,FIAT,coinprice

TODO/WISHLIST
anything in ccprices.log
clean JSON output to 3x COIN FIAT PRICE + DATE TIME 
fix the happy accident in the last for each -loop
