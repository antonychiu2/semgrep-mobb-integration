# Pattern with variables - may be vulnerable depending on data flow
# Detection depends on tracing variable origins

import json
import os

def process_config_file(config_path):
    # POTENTIALLY VULNERABLE: Depends on config file content
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    initialization_code = config.get('init_code', '')
    exec(initialization_code)


def execute_from_env():
    # VULNERABLE: Environment variable could be controlled by attacker
    code_from_env = os.environ.get('EXEC_CODE', 'pass')
    exec(code_from_env)


def safe_looking_but_vulnerable():
    # This looks safe but the variable comes from user input
    user_input = input("Enter value: ")
    code_to_run = f"value = {user_input}"
    
    # VULNERABLE: Variable contains user input
    exec(code_to_run)


def complex_variable_flow(data_source):
    # Complex flow where vulnerability depends on data_source
    processed = data_source.strip()
    sanitized = processed.replace(";", "")  # Inadequate sanitization
    
    command = f"result = {sanitized}"
    
    # VULNERABLE: Inadequate sanitization
    exec(command)


class CodeStorage:
    def __init__(self):
        self.stored_code = None
    
    def store_code(self, code):
        self.stored_code = code
    
    def execute_stored(self):
        # VULNERABLE: Depends on what was stored
        if self.stored_code:
            exec(self.stored_code)


def indirect_exec(code_dict):
    # VULNERABLE: Indirect variable assignment
    selected_code = code_dict.get('user_choice', 'pass')
    exec(selected_code)


if __name__ == "__main__":
    # Examples that might be vulnerable
    process_config_file("config.json")
    execute_from_env()
    safe_looking_but_vulnerable() 
