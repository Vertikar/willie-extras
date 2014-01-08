__author__ = 'sylvain'

from willie.module import commands, example
import urllib2
import json
import datetime

@commands('btce')
@example('.btce')
def btce(bot, trigger):

    for i in ('ltc_btc','btc_usd',"ltc_usd"):
        try:
            file_read = urllib2.urlopen("https://btc-e.com/api/2/%s/ticker"%i)
            file_read = json.load(file_read)
            bot.reply("BTC-e: %s  buy=%f sell=%f  last=%f  high=%f low=%f  vol=%f %s"%(i,file_read['ticker']['buy'],
                                                                                        file_read['ticker']['sell'],
                                                                                        file_read['ticker']['last'],
                                                                                        file_read['ticker']['high'],
                                                                                        file_read['ticker']['low'],
                                                                                        file_read['ticker']['vol'],
                                                                                        datetime.datetime.fromtimestamp(file_read['ticker']['updated']).strftime('%Y-%m-%d %H:%M:%S')
            ))

        except:
            bot.reply("Can't contact API.")
            return


# https://btc-e.com/api/2/ltc_btc/ticker
#
#

#BTC-e: BTCUSD  buy=713.84 sell=713.254  last=713.68  high=hi low=689.90002  vol=8285207.49093  Sun 2013-Dec-29 01:37:23 UTC
#BTC-e: LTCUSD  buy=22.12 sell=22.1  last=22.1  high=hi low=21.52  vol=8397176.7123  Sun 2013-Dec-29 01:37:23 UTC
#BTC-e: LTCBTC  buy=0.03082 sell=0.03081  last=0.03082  high=hi low=0.03065  vol=1797.77271  Sun 2013-Dec-29 01:37:23 UTC