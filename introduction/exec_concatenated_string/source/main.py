# Vulnerable pattern - exec() with string concatenation
# This should be detected as TRUE POSITIVE

def execute_with_concatenation(user_value):
    # VULNERABLE: String concatenation with user input
    exec("result = " + user_value)
    return locals().get('result')


def build_code_incrementally(parts):
    # VULNERABLE: Building code through concatenation
    code = ""
    for part in parts:
        code += part + "\n"
    exec(code)


def concat_with_prefix(command):
    # VULNERABLE: Concatenating with seemingly safe prefix
    safe_prefix = "import math; "
    exec(safe_prefix + command)


def multi_concat(var_name, operator, value):
    # VULNERABLE: Multiple concatenations
    code = var_name + " " + operator + " " + str(value)
    exec(code)


class DynamicExecutor:
    def __init__(self):
        self.base_code = "x = 10\n"
    
    def add_and_execute(self, additional_code):
        # VULNERABLE: Concatenating with instance variable
        full_code = self.base_code + additional_code
        exec(full_code)


def join_code_parts(code_parts):
    # VULNERABLE: Using join to concatenate
    full_code = "\n".join(code_parts)
    exec(full_code)


if __name__ == "__main__":
    # Example vulnerable calls
    execute_with_concatenation("__import__('os').system('ls')")
    build_code_incrementally(["import os", "os.system('pwd')"])
    concat_with_prefix("os.system('whoami')")
    multi_concat("y", "=", "50") 
