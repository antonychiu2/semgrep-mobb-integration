import subprocess
import sys

def delete_user_folder(name):
    """Simulates deleting a user's folder — vulnerable to injection"""
    delete_cmd = ['rm', '-rf', f'/home/{name}']
    subprocess.run(delete_cmd, shell=True)

def create_user_file_safe(name):
    """Safe: uses list of args"""
    subprocess.run(["touch", f"/tmp/{name}.txt"], shell=True)

default_admin_action = "whoami"
subprocess.run(default_admin_action, shell=True)

def run_admin_command():
    subprocess.run(default_admin_action, shell=True)

if __name__ == "__main__":
    delete_user_folder(sys.argv[1])
    create_user_file_safe(sys.argv[1])
