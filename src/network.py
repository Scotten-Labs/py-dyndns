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
    
    ID = "id"
    TYPE = "type"
    NAME = "name"
    CONTENT = "content"
    PROXIABLE = "proxiable"
    PROXIED = "proxied"
    TTL = "ttl"
    LOCKED = "locked"
    ZONE_ID = "zone_id"
    ZONE_NAME = "zone_name"
    CREATED_ON = "created_on"
    MODIFIED_ON = "modified_on"
    DATA = "data"
    META = "meta"
    PRIORITY = "priority"
    
    BASE_URL = "https://api.cloudflare.com/client/v4/zones"

    def __init__(self, token: str, domain: str):
        """Minimalized Cloudflare API connection.

        Args:
            key (str): API Token
            domain (str): Domain
        """   
        
        self.session = requests.Session()
        self.session.headers.update({"Authorization":f"Bearer {token}", "Content-Type": "application/json"})
        
        req = self.session.get(self.BASE_URL)
        zones = req.json()["result"]
        
        self._token: str = f"Bearer {token}"
        self._zoneID: str = {z['name']:z['id'] for z in zones}[domain]
        self.records: list[dict] = []
        
        self.BASE_URL += f"/{self._zoneID}"
        
        ### Cleanup
        del(req)
        del(zones)

    def updateLocalRecords(self) -> bool:
        COMMAND = "dns_records"
        try:
            req = self.session.get(f"{self.BASE_URL}/{COMMAND}")
            if req.json()["errors"] == []:
                self.records = [i for i in req.json()["result"]]
                return True
        except:
            return False

    def getRecord(self, name: str) -> dict:
        try:
            for record in self.getRecords():
                if record[self.NAME] == name:
                    return record
        except KeyError:
            return {}
    
    def getRecordID(self, name: str) -> str:
        return self.getRecord(name)[self.ID]
    
    def getRecords(self) -> list:
        return self.records
    
    def createRecord(self, type: str, name: str, content: str, ttl: int = 1, priority: int = 10, proxied: bool = False) -> bool:
        COMMAND = "dns_records"
        data = {self.TYPE: type, self.NAME:name, self.CONTENT: content, self.TTL: ttl, self.PRIORITY: priority, self.PROXIED: proxied}
        try:
            req = self.session.post(f"{self.BASE_URL}/{COMMAND}", json=data).json()
            if req["success"] == True:
                return True
            else:
                return False
        except:
            return False
        finally:
            self.updateLocalRecords()
    
    def updateRecord(self, type: str, name: str, content: str, ttl: int = 1, proxied: bool = False) -> bool:
        COMMAND = "dns_records"
        data = {self.TYPE: type, self.NAME:name, self.CONTENT: content, self.TTL: ttl, self.PROXIED:proxied}
        record_id = self.getRecord(name)[self.ID]
        try:
            req = self.session.put(f"{self.BASE_URL}/{COMMAND}/{record_id}", json=data).json()
            if req["success"] == True:
                return True
            else:
                return False
        except:
            return False
        finally:
            self.updateLocalRecords()
    
    def deleteRecord(self, name: str) -> bool:
        COMMAND = "dns_records"
        record_id = self.getRecord(name)[self.ID]
        try:
            req = self.session.delete(f"{self.BASE_URL}/{COMMAND}/{record_id}").json()
            # print(req)
            if req["success"] == True:
                return True
            else:
                return False
        except:
            return False
        finally:
            self.updateLocalRecords()