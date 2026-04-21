import re
from typing import List

from utils.load_stopwords import load_stopwords


def tokenize(text: str) -> List[str]:
    lower_case_text = text.lower()
    clean = re.sub(r"[^a-zA-Z0-9]", " ", lower_case_text)
    words = list(filter(None, clean.split(" ")))
    stopwords = set(load_stopwords())
    filtered_words = [w for w in words if w not in stopwords] 
    return filtered_words
    
