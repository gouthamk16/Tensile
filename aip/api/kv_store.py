# Simple json file based key-value store (should have the same functionalty as the previous sqlite based key-value store).

import json

class KVStore:
    def __init__(self):
        self.data = []

    def get(self, key):
        result = []
        for _data in self.data:
            result.append(_data.get(key, None))
        return result

    def set(self, key, value):
        _dict = {}
        _dict[key] = value
        self.data.append(_dict)

    def delete(self, key):
        for _data in self.data:
            if key in _data:
                self.data.remove(_data)

    def to_json(self):
        return self.data

    def from_json(self, data):
        self.data.append(data)

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f)

    def load(self, filename):
        with open(filename) as f:
            self.data.append(json.load(f))

