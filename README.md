[![Pytest](https://github.com/Scotten-Labs/python-template/actions/workflows/pytest.yml/badge.svg)](https://github.com/Scotten-Labs/python-template/actions/workflows/pytest.yml)

# Py DYN DNS

Dynamic DNS using the Cloudflare API.

## Supported Python Versions / Requirements

Python 3.10.x or greater

## Setup

1. Download the lastest version to wherever you like.
2. Edit config_template.csv in the data folder.
    - Add your api token from Cloudflare
    - Add the domain name you want to update ex. (github.com)
3. Rename config_template.csv to config.csv
4. Edit records.txt in the data folder.
    - Add in the subdomain(s) you want to point towards the local WAN
5. Start main.py
6. (Optional) Setup main.py to run at boot.
