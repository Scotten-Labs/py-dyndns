import csv
from src import *
import requests

if __name__ == "__main__":
    wan = network.Local.getWAN()
    print(wan)

    c = Config()
    c.open("data/config.csv")
    token = c.get("cloudflare", "api_token")
    domain = c.get("cloudflare", "domain")

    rem = network.Remote(token, domain)
    zoneid = rem._zoneID
    print(zoneid)
    
    r = rem.updateLocalRecords()
    
    print(r)
    
    for i in rem.getRecords():
        print(i["name"])

    # x = requests.get(url=f"https://api.cloudflare.com/client/v4/zones/{zoneid}/dns_records",
    #                  headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    # response = x.json()
    # print(type(response))
    
    # fnames = set()
    
    # print(response)
    
    # for o in response:
    #     fnames.add(o)
    
    # with open("data/store2.csv", "w") as f:
    #     writer = csv.DictWriter(f, fnames)
    #     writer.writeheader()
    #     writer.writerows(response)


    # store = [i for i in response["result"]]
    
    # print(type(store))
    
    # for o in store: print(str(o) + "\n")
    
    # print(type(response["result"]))
    
    # fnames = set()
    
    # for o in store:
    #     for n in o:
    #         fnames.add(n)

    # with open("data/store.csv", "w") as f:
    #     writer = csv.DictWriter(f, fnames)
    #     writer.writeheader()
    #     writer.writerows(store)
