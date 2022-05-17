from xmlrpc.client import ResponseError
import requests
import CloudFlare

class Local:

    def getWAN():
        wan = requests.get("https://api.ipify.org/").text
        return wan

class Remote(CloudFlare.CloudFlare):

    def __init__(self, key: str):
        super().__init__(token=key)
        zones = self.zones.get()
        self.ID = {z['name']:z['id'] for z in zones}

    def getID(self) -> dict:
        return self.ID