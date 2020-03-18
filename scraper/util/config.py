import os
import json

settings = None


def load_settings():
    global settings
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(path) as f:
        settings = json.load(f)


load_settings()
