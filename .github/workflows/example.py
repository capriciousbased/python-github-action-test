import os
import yaml

def get_azure_token():
    token = os.environ.get("AZURE_SECRET_TOKEN")
    if not token:
        raise RuntimeError("AZURE_SECRET_TOKEN env var is not set!")
    return token

def load_yaml_file(file_path):
    with open(file_path, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)

def print_server_info(server_info):
    print("Server Information:")
    print(f"Host: {server_info['host']}")
    print(f"Port: {server_info['port']}")

def print_database_info(database_info):
    print("\nDatabase Information:")
    print(f"Name: {database_info['name']}")
    credentials = database_info['credentials']
    print(f"Username: {credentials['username']}")
    print(f"Password: {credentials['password']}")

def print_table_info(table_info):
    print("\nTable Information:")
    print("Hello")
    for table in table_info:
        print(f"Table Name: {table['name']}")
        columns = ', '.join(table['columns'])
        print(f"Columns: {columns}\n")

def main():
    print("Hello from GitHub Actions!")
    azure_token = get_azure_token()
    print("All good! We found our env var")

    # Specify the path to your complex YAML file
    yaml_file_path = 'testData.yml'

    # Load the YAML file
    complex_yaml_content = load_yaml_file(yaml_file_path)

    # Extract information
    server_info = complex_yaml_content.get('server', {})
    database_info = complex_yaml_content.get('database', {})
    table_info = database_info.get('tables', [])

    # Print information
    print_server_info(server_info)
    print_database_info(database_info)
    print_table_info(table_info)

if __name__ == '__main__':
    main()
