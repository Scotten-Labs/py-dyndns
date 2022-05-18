import requests
import CloudFlare

class Local:

    def getWAN() -> str:
        """Returns the WAN IP address.

        Returns:
            str: WAN IP
        """
        wan = requests.get("https://api.ipify.org/").text
        return wan

class Remote(CloudFlare.CloudFlare):

    def __init__(self, key: str):
        """Minimalized Cloudflare API connection.

        Args:
            key (str): API Key
        """
        super().__init__(token=key)
        zones = self.zones.get()
        self.ID = {z['name']:z['id'] for z in zones}

    def getID(self) -> dict:
        return self.ID
