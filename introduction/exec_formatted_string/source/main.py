# Vulnerable pattern - exec() with formatted strings
# This should be detected as TRUE POSITIVE

import sys

def dynamic_variable_assignment(var_name, value):
    # VULNERABLE: f-string with user-controlled content
    exec(f"{var_name} = {value}")
    
    
def create_function_dynamically(func_name, func_body):
    # VULNERABLE: f-string formatting
    exec(f"""
def {func_name}():
    {func_body}
""")
    

def old_style_formatting(operation, operand1, operand2):
    # VULNERABLE: % formatting
    exec("result = %s %s %s" % (operand1, operation, operand2))
    return locals().get('result')


def format_method_injection(attr_name):
    # VULNERABLE: .format() method
    code_template = "value = obj.{}"
    exec(code_template.format(attr_name))
    

def template_execution(template, **kwargs):
    # VULNERABLE: Template with user data
    filled_template = template.format(**kwargs)
    exec(filled_template)


if __name__ == "__main__":
    # Example vulnerable calls
    dynamic_variable_assignment("user_var", "42")
    create_function_dynamically("evil_func", "import os; os.system('ls')")
    result = old_style_formatting("+", "10", "20")
    format_method_injection("__class__.__bases__") 
