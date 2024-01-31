import subprocess
import json

def create_apigee_app(api_url, organization, env, appgroup_name, app_name, apigee_token):
    appgroup_id = get_appgroup_id(api_url, organization, env, appgroup_name, apigee_token)

    if not appgroup_id:
        print(f"Appgroup '{appgroup_name}' not found.")
        return

    api_endpoint = f'{api_url}/organizations/{organization}/environments/{env}/appgroups/{appgroup_id}/apps'

    headers = {
        'Authorization': f'Bearer {apigee_token}',
        'Content-Type': 'application/json',
    }

    data = {
        'name': app_name,
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
        print(f'App "{app_name}" created successfully with ID: {response_json["id"]}')
    except subprocess.CalledProcessError as e:
        print(f'Error creating App: {e}')

def get_appgroup_id(api_url, organization, env, appgroup_name, apigee_token):
    api_endpoint = f'{api_url}/organizations/{organization}/environments/{env}/appgroups'

    headers = {
        'Authorization': f'Bearer {apigee_token}',
    }

    cmd = [
        'curl',
        '-X', 'GET',
        api_endpoint,
        '-H', f'Authorization: {headers["Authorization"]}',
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        appgroups = json.loads(result.stdout)

        for appgroup in appgroups:
            if appgroup['name'] == appgroup_name:
                return appgroup['id']

        print(f"Appgroup '{appgroup_name}' not found.")
        return None
    except subprocess.CalledProcessError as e:
        print(f'Error retrieving Appgroups: {e}')
        return None

if __name__ == "__main__":
    # Replace these values 
    apigee_api_url = 'https://api.enterprise.apigee.com/v1/o'
    organization = 'your_organization'
    env = 'your_environment'
    appgroup_name = 'your_appgroup_name'
    app_name = 'new_app_name'
    apigee_token = 'your_apigee_access_token'

    create_apigee_app(apigee_api_url, organization, env, appgroup_name, app_name, apigee_token)
