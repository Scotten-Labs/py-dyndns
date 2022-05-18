from src import config

def test_open():
    path = "data/config_template.csv"
    c = config.Config()
    assert c.open(path)

def test_get():
    path = "data/config_template.csv"
    c = config.Config()
    c.open(path)
    key = c.get("cloudflare", "api_key")
    assert key == "<api_key>"