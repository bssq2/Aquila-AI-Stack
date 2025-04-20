import requests

def fetch_dummy_data():
    """
    Fetch dummy data from dummyjson.com
    For example: https://dummyjson.com/products
    """
    resp = requests.get("https://dummyjson.com/products?limit=5")
    resp.raise_for_status()
    return resp.json()