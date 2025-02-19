from app import store

class Test():
    def __init__(self):
        pass
    def get(self):
        return store.to_json()
    def set(self, data):
        store.from_json(data)