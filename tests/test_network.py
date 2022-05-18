from src import network
import requests

def test_getWAN():
    assert network.Local.getWAN() == requests.get("https://api.my-ip.io/ip").text
