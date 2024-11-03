import os

from .parse_code import ParseCode
from src.utils import read_file


class ParseAllCodes:
    @staticmethod
    def _process_method_ref(ref: str) -> list[str]:
        processed_ref = [r for r in ref.split(".") if r not in ["new()"]]
        return {
            "parent": processed_ref[0],
            "method": processed_ref[1]
        }

    def _parse_references_for_app_folder(self, data: dict[str, list]) -> dict[str, list]:
        for file_path, items in data.items():
            for i, item in enumerate(items):
                if item["type"] == "Class":
                    pass
                elif item["type"] == "Method":
                    for ref in item["ref"]:
                        processed_ref = self._process_method_ref(ref)
                        for another_file_path, another_items in data.items():
                            if another_file_path != file_path:
                                for another_item in another_items:
                                    for parent in another_item["parent"]:
                                        if parent == processed_ref["parent"] and another_item["name"] == processed_ref["method"]:
                                            items[i]["ref_items"].append(another_item)
                else:
                    pass
        return data

    @staticmethod
    def _parse_references_for_db_folder(data: dict[str, list]) -> dict[str, list]:
        pass

    @staticmethod
    def _file_name_to_class_name(file_path: str) -> str:
        file_name = file_path.split("/")[-1].replace(".rb", "")
        file_name_split = "_"
        for i, item in enumerate(file_name_split):
            item = item[0].upper() + item[1:]
            file_name_split[i] = item
        return "".join(file_name_split)

    @staticmethod
    def _find_all_ruby_files(dir: str) -> list[str]:
        ruby_files = []
        for root, _, files in os.walk(dir):
            for file in files:
                if file.endswith('.rb'):
                    ruby_files.append(os.path.join(root, file).replace("\\", "/"))
        return ruby_files

    @staticmethod
    def _read_all_files(file_paths: list[str]) -> list[str]:
        return [
            read_file(file_path)
            for file_path in file_paths
        ]

    def parse(self, dir: str) -> list[dict]:
        ruby_files = self._find_all_ruby_files(dir)
        code_parser = ParseCode()

        items = {}
        for ruby_file in ruby_files:
            ruby_code = read_file(ruby_file)

            items[ruby_file] = code_parser.parse(ruby_code)

        items = self._parse_references_for_app_folder(items)

        return items