import argparse
import json

def has_similarity(query, text):
    q = set(query.lower().split())
    t = set(text.lower().split())
    
    return len(q & t)>0


def search(keyword: str):
    result = []
    with open("data/movies.json", "r") as movies_data:
        d = json.load(movies_data)
    for i in d["movies"]:
        if(has_similarity(i["title"], keyword)):
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
