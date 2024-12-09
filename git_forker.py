import requests
import time
# GitHub credentials
def git_repo_fork(GITHUB_TOKEN_VAL,REPO_NAME_VAL):
    GITHUB_TOKEN = GITHUB_TOKEN_VAL # Replace with your actual token
    REPO_OWNER = 'suprithvasista'  # Replace with the repository owner's username
    REPO_NAME = 'SuprithM_Portfolio'  # Replace with the repository you want to fork
    API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/forks'
    NEW_REPO_NAME=REPO_NAME_VAL #"project_1_trial"
    # Headers for authentication
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Send a POST request to fork the repository
    response = requests.post(API_URL, headers=headers)

    # Check if the fork was successful
    if response.status_code == 202:
        print(f"Repository {REPO_OWNER}/{REPO_NAME} forked successfully!")

        # The URL of the newly forked repository
        forked_repo_url = response.json()['html_url']
        print(f"Forked repository URL: {forked_repo_url}")
        return True
    else:
        print(f"Error forking repository: {response.json()['message']}")
        return False
def rename_git_repo(GITHUB_TOKEN_VAL,git_user_name,NEW_REPO_NAME):
    # Step 1: Rename the forked repository
    # Extract the username from the forked repository URL (after the slash)
    GITHUB_TOKEN=GITHUB_TOKEN_VAL
    user_name = git_user_name
    forked_repo_name = 'SuprithM_Portfolio'  # Default forked name

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    # GitHub API URL to rename the repository
    rename_url = f'https://api.github.com/repos/{user_name}/{forked_repo_name}'

    # Data for renaming the repository
    rename_data = {
        'name': NEW_REPO_NAME  # New name for the repository
    }

    # Send a PATCH request to rename the forked repository
    rename_response = requests.patch(rename_url, headers=headers, json=rename_data)
    print(rename_url)
    print(headers)
    print(rename_data)
    print("Response ",rename_response)
    if rename_response.status_code == 200:
        print(f"Repository renamed successfully to {NEW_REPO_NAME}!")
        print(f"Renamed repository URL: {rename_response.json()['html_url']}")
    else:
        print(f"Error renaming repository: {rename_response.json()['message']}")
        error_message = rename_response.json().get('message', 'No error message provided')
        print(error_message)

def wait_for_fork_ready(GITHUB_TOKEN_VAL, git_user_name, max_retries=30, delay=5):
    """
    Waits for the forked repository to be fully available for renaming.
    Repeatedly checks the repository URL until it becomes accessible.
    """
    headers = {
        'Authorization': f'token {GITHUB_TOKEN_VAL}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Extract the repository name from the forked repo URL
    repo_name = 'SuprithM_Portfolio'
    repo_url = f"https://api.github.com/repos/{git_user_name}/{repo_name}"

    retries = 0
    while retries < max_retries:
        response = requests.get(repo_url, headers=headers)

        if response.status_code == 200:  # Repository is available
            print(f"Forked repository {repo_name} is ready.")
            return True

        # Repository not ready, wait and retry
        print(f"Waiting for the forked repository to be available... Retry {retries + 1}/{max_retries}")
        time.sleep(delay)
        retries += 1

    # If we reach the max retries, print a message and return False
    print(f"Error: Forked repository not ready after {max_retries} retries.")
    return False