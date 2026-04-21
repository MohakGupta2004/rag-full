import json

def load_json():
    with open("data/movies.json", "r") as movies_data:
        d = json.load(movies_data)
    
    return d 