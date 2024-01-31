import yaml

# Specify the path to your complex YAML file
yaml_file_path = '/Users/mdanisulhoquekhan/Desktop/python-github-action-test/testData.yml'

# Open the YAML file and load its content
with open(yaml_file_path, 'r') as yaml_file:
    complex_yaml_content = yaml.safe_load(yaml_file)

# Now you can work with the loaded YAML content as a Python data structure
server_info = complex_yaml_content['server']
database_info = complex_yaml_content['database']
table_info = database_info['tables']

print("Server Information:")

print(f"Host: {server_info['host']}")
print(f"Port: {server_info['port']}")

print("\nDatabase Information:")

print(f"Name: {database_info['name']}")
print(f"Username: {database_info['credentials']['username']}")
print(f"Password: {database_info['credentials']['password']}")

print("\nTable Information:")
print(f"Hello")
for table in table_info:
    print(f"Table Name: {table['name']}")
    print(f"Columns: {', '.join(table['columns'])}")
    print("\n")