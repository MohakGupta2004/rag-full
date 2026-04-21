

def load_stopwords():
    with open("data/stop_words.txt", "r") as d:
        words = d.read().splitlines()
    
    return words
        
load_stopwords()