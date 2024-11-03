import os

from .parse_code import ParseCode
from src.utils import read_file


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

    @staticmethod
    def _find_all_ruby_files(dir: str) -> list[str]:
        ruby_files = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith('.rb'):
                    ruby_files.append(os.path.join(root, file))
        return ruby_files

    @staticmethod
    def _read_all_files(file_paths: list[str]) -> list[str]:
        return [
            read_file(file_path)
            for file_path in file_paths
        ]

    def parse(self, dir: str) -> list[dict]:
        ruby_files = self._find_all_ruby_files(dir)
        ruby_codes = self._read_all_files(dir)

        code_parser = ParseCode()