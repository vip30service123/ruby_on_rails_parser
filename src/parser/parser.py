from jedi_output_like import JediOutputLike
from parse_all_codes import ParseAllCodes


class Parser:
    def __init__(self):
        self._jedi_output_like = JediOutputLike()
        self._parse_all_codes = ParseAllCodes
    
    def __call__(
        self, 
        repo_dir: str
    ) -> list[dict]:
        pass