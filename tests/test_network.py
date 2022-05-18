from src import *
import requests

def test_getWAN():
    assert Network.Local.getWAN() == requests.get("https://api.my-ip.io/ip").text
