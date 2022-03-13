import requests


def load(url):
    req = requests.get(url)
    return req.content