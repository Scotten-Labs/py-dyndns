from src import *

def test_open():
    path = "data/config_template.csv"
    c = Config()
    assert c.open(path)

def test_get():
    path = "data/config_template.csv"
    c = Config()
    c.open(path)
    key = c.get("cloudflare", "api_key")
    assert key == "<api_key>"