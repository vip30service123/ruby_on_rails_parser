class ParseCode:
    def __init__(self, code: str):
        self._code = code

    def _parse_ast(self, code: str):
        pass

    def _tree_sitter_parser():
        pass

    @staticmethod
    def _parse_class_function_module_info(root: any) -> list[dict]:
        pass

    @staticmethod
    def _is_parent(potential_parent, potential_child) -> bool:
        pass

    @staticmethod
    def _fill_all_parents(items: list) -> list:
        pass

    @staticmethod
    def get_class_function_module_info() -> list[dict]:
        pass
    
    @staticmethod
    def _file_name_to_class_name(file_name: str) -> str:
        pass

    @staticmethod
    def _is_file_name_matchs_class_name(file_name: str, class_name: str) -> bool:
        pass

    def __call__(self, code: str):
        pass