# Safe pattern - exec() with literal string constant
# This should be detected as FALSE POSITIVE

def initialize_variables():
    # Safe: literal string with no variables or interpolation
    exec("x = 1; y = 2; z = x + y")
    
    # Also safe: multiline literal
    exec("""
def helper_function():
    return 42
    
result = helper_function()
""")
    
    return True


def setup_constants():
    # Safe: another literal string example
    exec("CONSTANT_VALUE = 100")
    exec("DEBUG_MODE = False")
    

if __name__ == "__main__":
    initialize_variables()
    setup_constants() 
