__author__ = 'sylvain'

from willie.module import commands, example
import urllib2
from cStringIO import StringIO
import gnupg


def configure(config):
    if not config.has_section('gpg'):
        config.add_section('gpg')

    config.interactive_add('gpg', 'gpg_keys_path', 'GPG key directory:', '~/.gnupg')
    config.interactive_add('gpg', 'gpg_key_id', 'GPG key id:', '')
    config.interactive_add('gpg', 'gpg_key_passphrase', 'GPG key passphrase:', 'none')

@commands('clearsign')
@example('.clearsign http://perdu.com')
def clearsign(bot, trigger):

    #download url
    url = trigger.group(2)

    if url[:4] is not "http":
        bot.reply("URL protocol not supported, only http and https")
        return

    try:
        resp = urllib2.urlopen(url)
    except:
        bot.reply("Wrong URL")
        return

    file_read = resp.read(9999999)

    if bot.config.has_option('gpg', 'gpg_keys_path') and bot.config.has_option('gpg', 'gpg_key_id'):
        gpg_keys_path = bot.config.gpg.gpg_keys_path
        gpg_key_id = bot.config.gpg.gpg_key_id
        if bot.config.has_option('gpg', 'gpg_keys_path') and bot.config.has_option('gpg', 'gpg_keys_path') is not 'none':
            gpg_key_passphrase = bot.config.gpg.gpg_key_passphrase
        else:
            gpg_key_passphrase = None
    else:
        bot.reply("GPG not setup correctly")
        return
    #gpg = gnupg.GPG(gnupghome=gpg_keys_path)
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    #set good key

    #sign
    #signed_data = gpg.sign(file_read,passphrase=gpg_key_passphrase,keyid=gpg_key_id,clearsign=True,)
    signed_data = gpg.sign(file_read,passphrase=gpg_key_passphrase,clearsign=True,)
    #fingerprint
    if signed_data is not None :
        bot.reply("fingerprint: "+signed_data.fingerprint)
    else:
        bot.reply("clearsign failed")
