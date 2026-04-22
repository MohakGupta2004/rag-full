import pickle

def dump_pkl(path: str, data):
    with open(path, "wb") as file:
        pickle.dump(data, file)