# Vulnerable pattern - exec() with command-line arguments
# This should be detected as TRUE POSITIVE

import sys
import argparse

def execute_from_argv():
    # VULNERABLE: Command line arguments are external input
    if len(sys.argv) > 1:
        code_to_execute = sys.argv[1]
        exec(code_to_execute)


def execute_from_argparse():
    # VULNERABLE: Argparse arguments are external input
    parser = argparse.ArgumentParser()
    parser.add_argument('--code', help='Python code to execute')
    parser.add_argument('--expression', help='Mathematical expression')
    
    args = parser.parse_args()
    
    if args.code:
        exec(args.code)
    
    if args.expression:
        exec(f"result = {args.expression}")
        print(f"Result: {locals().get('result')}")


def batch_execute_args():
    # VULNERABLE: Processing multiple command line arguments
    for arg in sys.argv[1:]:
        print(f"Executing: {arg}")
        exec(arg)


def main():
    # VULNERABLE: Different ways to use command line args
    if "--execute" in sys.argv:
        idx = sys.argv.index("--execute")
        if idx + 1 < len(sys.argv):
            code = sys.argv[idx + 1]
            exec(code)
    
    # Another vulnerable pattern
    commands = " ".join(sys.argv[1:])
    if commands:
        exec(commands)


if __name__ == "__main__":
    # All of these are vulnerable to command injection
    execute_from_argv()
    execute_from_argparse()
    main() 
