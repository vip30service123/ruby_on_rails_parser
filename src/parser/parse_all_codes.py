from parse_code import ParseCode


class ParseAllCodes:
    def __init__(
        self, 
        repo_dir: str,
        code_parser: any = None
    ):
        self._repo_dir = repo_dir
        if code_parser:
            self._code_parser = code_parser
        else:
            self._code_parser = ParseCode()

    @staticmethod
    def _parse_references_for_app_folder(data: dict[str, list]) -> dict[str, list]:
        pass

    @staticmethod
    def _parse_references_for_db_folder(data: dict[str, list]) -> dict[str, list]:
        pass

    