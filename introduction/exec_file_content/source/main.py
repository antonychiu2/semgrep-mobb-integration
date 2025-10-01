# Vulnerable pattern - exec() with file content
# This should be detected as TRUE POSITIVE

import os

def execute_python_file(filepath):
    # VULNERABLE: Executing content from a file
    with open(filepath, 'r') as f:
        file_content = f.read()
    exec(file_content)


def execute_user_uploaded_script(upload_path):
    # VULNERABLE: User uploaded files are untrusted
    if os.path.exists(upload_path):
        with open(upload_path, 'r') as f:
            script = f.read()
        
        # Try to execute the uploaded script
        exec(script)


def load_and_execute_config(config_file):
    # VULNERABLE: Config files might be modified by attackers
    config_code = ""
    with open(config_file, 'r') as f:
        for line in f:
            if line.startswith("EXEC:"):
                config_code += line[5:]  # Remove "EXEC:" prefix
    
    if config_code:
        exec(config_code)


def process_template_file(template_path, variables):
    # VULNERABLE: Template injection
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Replace variables in template
    for var, value in variables.items():
        template = template.replace(f"{{{var}}}", str(value))
    
    # Execute the processed template
    exec(template)


class PluginLoader:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
    
    def load_plugin(self, plugin_name):
        # VULNERABLE: Loading and executing plugins
        plugin_path = os.path.join(self.plugin_dir, f"{plugin_name}.py")
        
        if os.path.exists(plugin_path):
            with open(plugin_path, 'r') as f:
                plugin_code = f.read()
            
            # Execute plugin code
            exec(plugin_code)


def execute_from_url(url):
    # VULNERABLE: Downloading and executing code from URL
    import urllib.request
    
    response = urllib.request.urlopen(url)
    remote_code = response.read().decode('utf-8')
    
    exec(remote_code)


if __name__ == "__main__":
    # Examples of vulnerable file-based exec
    execute_python_file("user_script.py")
    execute_user_uploaded_script("/tmp/uploaded_script.py")
    load_and_execute_config("app.config") 
