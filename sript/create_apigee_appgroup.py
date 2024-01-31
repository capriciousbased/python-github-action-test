import subprocess
import json

def create_apigee_appgroup(api_url, organization, env, appgroup_name, apigee_token):
    api_endpoint = f'{api_url}/organizations/{organization}/environments/{env}/appgroups'

    headers = {
        'Authorization': f'Bearer {apigee_token}',
        'Content-Type': 'application/json',
    }

    data = {
        'name': appgroup_name,
    }

    cmd = [
        'curl',
        '-X', 'POST',
        api_endpoint,
        '-H', f'Authorization: {headers["Authorization"]}',
        '-H', f'Content-Type: {headers["Content-Type"]}',
        '-d', json.dumps(data),
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        response_json = json.loads(result.stdout)
        print(f'Appgroup "{appgroup_name}" created successfully with ID: {response_json["id"]}')
    except subprocess.CalledProcessError as e:
        print(f'Error creating Appgroup: {e}')

if __name__ == "__main__":
    # Replace the value
    apigee_api_url = 'https://api.enterprise.apigee.com/v1/o'
    organization = 'your_organization'
    env = 'your_environment'
    appgroup_name = 'new_appgroup_name'
    apigee_token = 'your_apigee_access_token'

    create_apigee_appgroup(apigee_api_url, organization, env, appgroup_name, apigee_token)
