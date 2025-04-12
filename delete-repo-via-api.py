import requests

base_url = "https://api.github.com"

def delete_repo(access_token, username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}"
   
    headers = {
        "Authorization": f"token {access_token}",
    }
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Repository has been deleted successfully. Status code: {response.status_code}")
    elif response.status_code == 404:
        print(f"Repository not found or already deleted. Status code: {response.status_code}")
    else:
        print(f"Failed to delete repository. Status code: {response.status_code}")

access_token = "YOUR  ACCESS TOKEN"
username = "YOUR GITHUB USERNAME"
repo_name = "apify_testing"

delete_repo(access_token, username, repo_name)