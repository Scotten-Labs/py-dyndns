from src import *
import time

if __name__ == "__main__":
    c = Config()
    c.open("data/config.csv")
    token = c.get("cloudflare", "api_token")
    domain = c.get("cloudflare", "domain")

    cf = network.Remote(token, domain)
    cf.updateLocalRecords()
    
    records = [rec.strip() for rec in open("data/records.txt")]
    
    ### This is written to adjust A records and point them towards the local WAN address.
    while True:
        wan = network.Local.getWAN()
        for name in records:
            try:
                if cf.getRecord(f"{name}.{domain}")[cf.CONTENT] != wan:
                    cf.updateRecord("A", f"{name}.{domain}", wan)
                    print(f"Record {name}.{domain} Updated to {wan}")
                else:
                    print(f"Record {name}.{domain} Correct")
            except TypeError:
                print(f"Record {name}.{domain} not Found")
        time.sleep(60)