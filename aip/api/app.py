from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from kv_store import KVStore
import json

app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
store = KVStore()

import routes

# with app.app_context():
#     store = KVStore()

if __name__ == '__main__':
    app.run(debug=True)