__author__ = 'sylvain'

from willie.module import commands, example
import urllib2
import json
import string

@commands('cryptsy')
@example('.cryptsy')
def cryptsy(bot, trigger):

    curr = trigger.group(2)
    curr.upper()
    if curr is None:
        curr="LTC"

    marketid={"94":"ADT/LTC","113":"ADT/XPM", "57":"ALF/BTC", "43":"AMC/BTC", "66":"ANC/BTC", "121":"ANC/LTC", "48":"ARG/BTC", "111":"ASC/LTC", "112":"ASC/XPM", "129":"BET/BTC", "10":"BQC/BTC", "23":"BTB/BTC", "49":"BTE/BTC", "50":"BTG/BTC", "102":"BUK/BTC", "53":"CAP/BTC", "136":"CAT/BTC", "97":"CENT/LTC", "118":"CENT/XPM", "70":"CGB/BTC", "123":"CGB/LTC", "95":"CLR/BTC", "74":"CMC/BTC", "8":"CNC/BTC", "17":"CNC/LTC", "109":"COL/LTC", "110":"COL/XPM", "91":"CPR/LTC", "58":"CRC/BTC", "68":"CSC/BTC", "46":"DBL/LTC", "131":"DEM/BTC", "26":"DGC/BTC", "96":"DGC/LTC", "72":"DMD/BTC", "132":"DOGE/BTC", "135":"DOGE/LTC", "52":"DVC/LTC", "122":"DVC/XPM", "12":"ELC/BTC", "93":"ELP/LTC", "69":"EMD/BTC", "55":"EZC/LTC", "138":"FFC/BTC", "61":"FLO/LTC", "39":"FRC/BTC", "33":"FRK/BTC", "44":"FST/BTC", "124":"FST/LTC", "5":"FTC/BTC", "82":"GDC/BTC", "76":"GLC/BTC", "30":"GLD/BTC", "36":"GLD/LTC", "78":"GLX/BTC", "84":"GME/LTC", "80":"HBN/BTC", "60":"IFC/LTC", "105":"IFC/XPM", "38":"IXC/BTC", "35":"JKC/LTC", "65":"KGC/BTC", "34":"LKY/BTC", "137":"LOT/BTC", "3":"LTC/BTC", "45":"MEC/BTC", "100":"MEC/LTC", "56":"MEM/LTC", "7":"MNC/BTC", "62":"MST/LTC", "32":"NBL/BTC", "90":"NEC/BTC", "134":"NET/BTC", "108":"NET/LTC", "104":"NET/XPM", "29":"NMC/BTC", "54":"NRB/BTC", "13":"NVC/BTC", "75":"ORB/BTC", "86":"PHS/BTC", "120":"Points/BTC", "28":"PPC/BTC", "125":"PPC/LTC", "119":"PTS/BTC", "31":"PXC/BTC", "101":"PXC/LTC", "92":"PYC/BTC", "71":"QRK/BTC", "126":"QRK/LTC", "87":"RED/LTC", "37":"RYC/LTC", "51":"SBC/BTC", "128":"SBC/LTC", "81":"SPT/BTC", "88":"SRC/BTC", "98":"SXC/LTC", "117":"TAG/BTC", "114":"TEK/BTC", "130":"TGC/BTC", "107":"TIX/LTC", "103":"TIX/XPM", "27":"TRC/BTC", "133":"UNO/BTC", "14":"WDC/BTC", "21":"WDC/LTC", "115":"XJO/BTC", "67":"XNC/LTC", "63":"XPM/BTC", "106":"XPM/LTC", "73":"YBC/BTC", "85":"ZET/BTC", "127":"ZET/LTC", "132":"DOGE/BTC"}

    markets=[]
    for i,j in marketid.iteritems():
        print "%s %s"%(i,j)
        if j.find(curr) != -1:
            markets.append(i)

    if markets == []:
        bot.reply("Currency not found.")
        return

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    try:

        for i in markets:
            req = urllib2.Request('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=%s'%i, None, hdr)

            resp = urllib2.urlopen(req)
            file_read = json.load(resp)
            print file_read


            for c,m in file_read['return']['markets'].iteritems():
                print c
                print m
                m=m['recenttrades'][0]
                bot.reply("%s price=%s quantity=%s total=%s %s"%
                     (c,m['price'],m['quantity'],m['total'],m['time']))
    except:
        bot.reply("Can't contact API.")
