import subprocess
import sys

def greet_user_direct(name):
    """Run greeting command directly as string"""
    subprocess.run(f"echo 'Hello, {name}!'", shell=True)

def greet_user_from_template(name):
    """Build greeting command from variable"""
    greeting_cmd = f"echo 'Hello, {name}!'"
    subprocess.run(greeting_cmd, shell=True)

def greet_user_safe(name):
    subprocess.run(["echo", f"Hello, {name}!"], shell=True)

system_default_cmd = "cmd"
subprocess.run(system_default_cmd, shell=True)

def run_global_command():
    subprocess.run(system_default_cmd, shell=True)

if __name__ == "__main__":
    greet_user_direct(sys.argv[1])
    greet_user_from_template(sys.argv[1])
    greet_user_safe(sys.argv[1])
