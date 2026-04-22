import argparse
from operator import invert
from typing import List

from utils.dump_pkl import dump_pkl
from .tokenizer import tokenize
from utils.load_json import load_json
class InvertedIndex:
    def __init__(self) -> None:
        self.index:dict[str, set[int]] = {}
        self.docmap = {}
    
    def __add_documents(self,doc_id, text):
        tokenized_text = tokenize(text)
        for token in tokenized_text:
            if token not in self.index:
                self.index[token] = set()
            
            self.index[token].add(doc_id)
    
    def get_documents(self, term):
        term = term.lower()
        if term not in self.index:
            return []
            
        return sorted(self.index[term])
    
    def build(self):
        movies = load_json()
        for m in movies['movies']:
            doc_id = m['id']
            self.docmap[doc_id] = m
            self.__add_documents(doc_id, f"{m["title"]} {m["description"]}")
    
    def save(self):
        dump_pkl(path="cache/index.pkl", data=self.index)
        dump_pkl(path="cache/docmap.pkl", data=self.docmap)
            
        

def has_similarity(query, text):
    query_tokens:List[str] = tokenize(query)
    text_tokens:List[str] = tokenize(text)
    for q in query_tokens:
        for t in text_tokens:
            if q in t:
                return True
    return False
    
   
def search(keyword: str):
    result = []
    movies = load_json()
    for i in movies["movies"]:
        if(has_similarity(keyword, i['title'])):
            result.append(i['title'])
        
    print(result)

def build():
    inverted_index = InvertedIndex()
    inverted_index.build()
    inverted_index.save()
    docs = inverted_index.get_documents('merida')
    print(f"First document for token 'merida' = {docs[0]}")

def main():
    parser = argparse.ArgumentParser(description="Keyword search tool")
    sub_parsers = parser.add_subparsers(
        dest="command", description="Store the command on args.commands"
    )
    search_command = sub_parsers.add_parser(name="search", help="Search movies")
    build_command = sub_parsers.add_parser(name="build", help="Build inverted index")

    search_command.add_argument("query", type=str, help="Movie name")

    args = parser.parse_args()

    match args.command:
        case "search":
            search(args.query)
            pass
        case "build":
            build()
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
