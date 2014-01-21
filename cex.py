__author__ = 'sylvain'

from willie.module import commands, example
import urllib2
import json

@commands('cex')
@example('.cex')
@willie.module.commands('cex')
def cex(bot, trigger):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    try:
        req = urllib2.Request('http://cex.io/api/ticker/GHS/BTC', None, hdr)

        resp = urllib2.urlopen(req)
        file_read = json.load(resp)
        bot.reply("CEX GHS/BTC %s UTC: low=%s high=%s last=%s volume=%s bid=%s ask=%s"%
                  (file_read['timestamp'],file_read['low'],file_read['high'],file_read['last'],file_read['volume'],file_read['bid'],file_read['ask'])
        )
    except:
        bot.reply("Can't contact API.")


