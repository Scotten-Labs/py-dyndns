import urllib.request

def getWAN():
    wan = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return wan