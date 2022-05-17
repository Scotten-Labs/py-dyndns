from src import *
import CloudFlare

if __name__ == "__main__":
    wan = Network.Local.getWAN()
    print(wan)

    c = Config()
    c.open("data/config.csv")
    key = c.get("cloudflare", "api_key")
    print(key)

    rem = Network.Remote(key)
    id = rem.getID()
    print(id)

    # cf = CloudFlare.CloudFlare(token=key)
    # zones = cf.zones.get()
    # for zone in zones:
    #     zone_id = zone['id']
    #     zone_name = zone['name']
    #     print("zone_id=%s zone_name=%s" % (zone_id, zone_name))