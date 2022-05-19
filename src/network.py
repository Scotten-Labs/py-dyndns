import requests

class Local:

    def getWAN() -> str:
        """Returns the WAN IP address.

        Returns:
            str: WAN IP
        """
        wan = requests.get("https://api.ipify.org/").text
        return wan

class Remote():

    def __init__(self, token: str, domain: str):
        """Minimalized Cloudflare API connection.

        Args:
            key (str): API Token
            domain (str): Domain
        """   
        req = requests.get("https://api.cloudflare.com/client/v4/zones", headers={"Authorization":f"Bearer {token}", "Content-Type": "application/json"})
        zones = req.json()["result"]
        
        self._token: str = f"Bearer {token}"
        self._zoneID: str = {z['name']:z['id'] for z in zones}[domain]
        self.records: list[dict] = []
        
        ### Cleanup
        del(req)
        del(zones)

    def updateLocalRecords(self) -> bool:
        try:
            req = requests.get(url=f"https://api.cloudflare.com/client/v4/zones/{self._zoneID}/dns_records",
                                                    headers={"Authorization": self._token, "Content-Type": "application/json"})
            if req.json()["errors"] == []:
                self.records = [i for i in req.json()["result"]]
                return True
        except:
            return False

    def getRecord(self, name: str, type: str) -> str | int | bool:
        pass
    
    def getRecords(self) -> list:
        return self.records

    def updateRecord(self, type: str, name: str, content: str, ttl: int = 1) -> bool:
        pass