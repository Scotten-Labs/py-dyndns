import pytest
from src import config

def test_open():
    path = "data/config_template.csv"
    c = config.Config()
    assert c.open(path)

def test_get():
    path = "data/config_template.csv"
    c = config.Config()
    c.open(path)
    key = c.get("cloudflare", "api_token")
    assert key == "<api_token>"
    
def test_get_error():
    c = config.Config()
    with pytest.raises(TypeError):
        c.get("cloudflare", "api_token")
        
def test_open_error():
    c = config.Config()
    with pytest.raises(FileNotFoundError):
        c.open("fake/path/to/config/file.csv")
