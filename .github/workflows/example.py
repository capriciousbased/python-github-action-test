import os
import yaml
import json

def get_azure_token():
    token = os.environ.get("AZURE_SECRET_TOKEN")
    if not token:
        raise RuntimeError("AZURE_SECRET_TOKEN env var is not set!")
    return token

def load_yaml_file(file_path):
    with open(file_path, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)

def export_as_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

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

    # Prepare data for export
    export_data = {
        'server_info': server_info,
        'database_info': database_info,
        'table_info': table_info
    }

    # Export as JSON
    output_json_file = 'exported_data.json'
    export_as_json(export_data, output_json_file)
    print(f"Exported data to {output_json_file}")

if __name__ == '__main__':
    main()
