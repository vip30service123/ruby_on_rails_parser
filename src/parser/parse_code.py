from tree_sitter import Language, Parser


class ParseCode:
    def _parse_ast(self, code: str):
        pass

    @staticmethod
    def _tree_sitter_parser():
        Language.build_library(
            'build/my-languages.so',
            [
                'data/tree-sitter-ruby'  # Replace with your cloned path
            ]
        )
        RUBY_LANGUAGE = Language('build/my-languages.so', 'ruby')
        parser = Parser()
        parser.set_language(RUBY_LANGUAGE)
        return parser

    @staticmethod
    def _is_parent(potential_parent, potential_child) -> bool:
        pass

    @staticmethod
    def _fill_all_parents(items: list) -> list:
        pass

    @staticmethod
    def _parse_class_function_module_info(node: any, code: bytes) -> list[dict]:
        items = []

        def parse_class(node):
            if node.type == "class":
                item = {
                    "name": None,
                    "code": code[node.start_byte:node.end_byte].decode("utf-8"),
                    "type": "Class",
                    "start_point": node.start_point,
                    "end_point": node.end_point,
                    "ref": [] 
                }
                if node.children:
                    for child in node.children:
                        if child.type == "scope_resolution":
                            item["name"] = code[child.start_byte:child.end_byte].decode("utf-8")
                        if child.type == "superclass":
                            item["ref"].append(code[child.start_byte:child.end_byte].decode("utf-8"))

                    items.append(item)
                    return None
                else:
                    return None
            else:
                for child in node.children:
                    parse_class(child)

        def parse_function(node):
            if node.type == "method":
                item = {
                    "name": None,
                    "code": code[node.start_byte:node.end_byte].decode("utf-8"),
                    "type": "Method",
                    "start_point": node.start_point,
                    "end_point": node.end_point,
                    "ref": [] 
                }
                if node.children:
                    for child in node.children:
                        if child.type == "identifier":
                            item["name"] = code[child.start_byte:child.end_byte].decode("utf-8")
                        if child.type == "body_statement":
                            child = child.children[0] # It should be assignment
                            for grand_child in child.children:
                                if grand_child.type == "call":
                                    item["ref"].append(code[grand_child.start_byte:grand_child.end_byte].decode("utf-8"))
                        
                    items.append(item)
                    return None
                else:
                    return None
            else:
                for child in node.children:
                    parse_function(child)

        def parse_module(node):
            if node.type == "module":
                item = {
                    "name": None,
                    "code": code[node.start_byte:node.end_byte].decode("utf-8"),
                    "type": "Module",
                    "start_point": node.start_point,
                    "end_point": node.end_point,
                    "ref": [] 
                }
                if node.children:
                    for child in node.children:
                        if child.type == "constant":
                            item["name"] = code[child.start_byte:child.end_byte].decode("utf-8")
                        if child.type == "body_statement":
                            for grand_child in child.children:
                                if grand_child.type == "call":
                                    item["ref"].append(code[grand_child.start_byte:grand_child.end_byte].decode("utf-8"))
                    items.append(item)
                    return None
                else:
                    return None
            else:
                for child in node.children:
                    parse_module(child)

        parse_module(node)
        parse_class(node)
        parse_function(node)

        return items
    
    @staticmethod
    def _file_name_to_class_name(file_name: str) -> str:
        pass

    @staticmethod
    def _is_file_name_matchs_class_name(file_name: str, class_name: str) -> bool:
        pass

    @staticmethod
    def _to_byte(code: str) -> str:
        return bytes(code, "utf-8")
    
    def _print_tree(self, node, code, indent=""):
        print(indent + node.type + " | " + str(code[node.start_byte:node.end_byte]))
        for child in node.children:
            self._print_tree(child, code, indent + "  ")

    def parse(self, code: str):
        code = self._to_byte(code=code)

        parser = self._tree_sitter_parser()

        code_ast = parser.parse(code)

        root = code_ast.root_node

        print(self._print_tree(root, code))

        items = self._parse_class_function_module_info(root, code)

        return items