import json

from src.parser.parser import Parser
from src.parser.parse_code import ParseCode
from src.parser.parse_all_codes import ParseAllCodes
from src.config import Config
from src.utils import (
    read_json, 
    write_json, 
    read_file, 
    write_file
)


if __name__ == "__main__":
    config = Config.repo_path

    # code_path = Config.specific_file_path

    # code = read_file(code_path)

    # items = ParseCode().parse(code)

    # for item in items:
    #     print(json.dumps(item, indent=2))



    dir = Config.repo_path

    items = ParseAllCodes().parse(dir=dir)

    print(json.dumps(items, indent=2))
