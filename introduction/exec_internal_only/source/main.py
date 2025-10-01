# Pattern with variables but only internal data - FALSE POSITIVE
# These patterns look vulnerable but don't use external input

def calculate_internal():
    # Safe: Variable is internally defined
    operation = "2 + 2"
    exec(f"result = {operation}")
    return locals()['result']


def predefined_operations():
    # Safe: All values are predefined internally
    operations = {
        'add': 'result = 5 + 3',
        'multiply': 'result = 4 * 7',
        'divide': 'result = 10 / 2'
    }
    
    chosen_op = 'add'  # Hardcoded choice
    exec(operations[chosen_op])


class InternalCodeGenerator:
    def __init__(self):
        self.templates = {
            'init': 'x = 0; y = 0',
            'increment': 'x += 1; y += 1',
            'reset': 'x = 0; y = 0'
        }
    
    def execute_template(self, template_name):
        # Safe: Only executes predefined templates
        if template_name in self.templates:
            exec(self.templates[template_name])


def build_internal_function():
    # Safe: Building function from internal components only
    func_name = "calculate_area"
    func_body = "return width * height"
    
    exec(f"""
def {func_name}(width, height):
    {func_body}
""")


def configuration_based_exec():
    # Safe: Configuration is hardcoded, not from external source
    config = {
        'setup': 'import math',
        'calculation': 'pi_value = math.pi'
    }
    
    for step in ['setup', 'calculation']:
        exec(config[step])


def safe_dynamic_import():
    # Safe: Module name is hardcoded
    module_name = "datetime"
    exec(f"import {module_name}")
    

if __name__ == "__main__":
    # All of these should be false positives
    calculate_internal()
    predefined_operations()
    
    generator = InternalCodeGenerator()
    generator.execute_template('init')
    
    build_internal_function()
    configuration_based_exec()
    safe_dynamic_import() 
