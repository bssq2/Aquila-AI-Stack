def fetch_dummy():
    # simulate fetching from an external source
    return {"foo": "bar", "timestamp": __import__("time").time()}