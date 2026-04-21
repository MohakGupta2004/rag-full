from utils.load_stopwords import load_stopwords
import re
from typing import List
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()


def tokenize(text: str) -> List[str]:
    lower_case_text = text.lower()
    clean = re.sub(r"[^a-zA-Z0-9]", " ", lower_case_text)
    words = list(filter(None, clean.split(" ")))
    stopwords = set(load_stopwords())
    filtered_words = [w for w in words if w not in stopwords]
    filtered_words = [stemmer.stem(w) for w in filtered_words]
    return filtered_words