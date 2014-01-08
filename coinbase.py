__author__ = 'sylvain'

from willie.module import commands, example
import urllib2
import json


def configure(config):
    if not config.has_section('coinbase'):
        config.add_section('coinbase')

    config.interactive_add('coinbase', 'api_key', 'API KEY', 'none')


@commands('coinbase','cb')
@example('.coinbase')
def coinbase(bot, trigger):

    if not bot.config.has_option('coinbase', 'api_key'):
        return

    api_key = bot.config.coinbase.api_key
    curr = trigger.group(2)
    if curr is None:
        curr="USD"

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    try:
        req = urllib2.Request("https://coinbase.com/api/v1/currencies/exchange_rates?api_key=%s"%api_key, None, hdr)

        resp = urllib2.urlopen(req)
        file_read = json.load(resp)
        print file_read

        bot.reply("BTC%s=%s %sBTC=%s %sUSD=%s USD%s=%s"%
                  (curr.upper(),file_read['btc_to_%s'%curr.lower()],curr.upper(),file_read['%s_to_btc'%curr.lower()],
                   curr.upper(),file_read['%s_to_usd'%curr.lower()],curr,file_read['usd_to_%s'%curr.lower()])
        )
    except:
        bot.reply("Can't contact API.")
