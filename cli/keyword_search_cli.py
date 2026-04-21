import argparse
from typing import List
from .tokenizer import tokenize
from utils.load_json import load_json
class InvertedIndex:
    def __init__(self) -> None:
        self.index:dict[str, int] = {}
        self.docmap = {}
    
    def __add_documents(self, term):
        pass
    
    def get_documents(self, term):
        pass
    
    def build():
        pass


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

def main():
    parser = argparse.ArgumentParser(description="Keyword search tool")
    sub_parsers = parser.add_subparsers(
        dest="command", description="Store the command on args.commands"
    )
    search_command = sub_parsers.add_parser(name="search", help="Search movies")

    search_command.add_argument("query", type=str, help="Movie name")

    args = parser.parse_args()

    match args.command:
        case "search":
            search(args.query)
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
