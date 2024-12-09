import requests
import base64
import json

# GitHub credentials
def git_file_updation(GITHUB_TOKEN_VAL,REPO_OWNER_VAL,REPO_NAME_VAL,FILE_PATH_VAL,Content_from_ui):
    GITHUB_TOKEN = GITHUB_TOKEN_VAL  # Replace with your actual token
    REPO_OWNER = REPO_OWNER_VAL # Replace with your GitHub username or organization name
    REPO_NAME = REPO_NAME_VAL#'project_1_trial'  # Replace with your repository name
    FILE_PATH = FILE_PATH_VAL#'README.md'  # The file you want to upload or update
    BRANCH = 'main'  # Branch to update (e.g., 'main', 'master', etc.)
    # GitHub API URL
    API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}'

    # New content for the file
    new_content = Content_from_ui

    # Step 1: Check if the file already exists
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }

    # Fetch the current file details (including SHA) if it exists
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        # If the file exists, get the sha from the response (required for update)
        file_data = response.json()
        current_sha = file_data['sha']
        print(f"File found, SHA: {current_sha}")
    else:
        # If the file does not exist, no sha is required
        current_sha = None
        print("File not found, will create a new file.")

    # Step 2: Encode the new content in base64 (GitHub API requires base64 encoding)
    encoded_content = base64.b64encode(new_content.encode()).decode()

    # Step 3: Prepare the request payload
    data = {
        "message": "Update or create file via GitHub API",  # Commit message
        "content": encoded_content,  # Base64 encoded content of the file
        "branch": BRANCH  # Specify the branch to commit to
    }

    # Include the sha only if the file exists (for update)
    if current_sha:
        data["sha"] = current_sha

    # Step 4: Send the PUT request to GitHub API to create/update the file
    update_response = requests.put(API_URL, headers=headers, data=json.dumps(data))

    # Step 5: Check if the update was successful
    if update_response.status_code == 200:
        print("File updated successfully!")
        print("Commit URL:", update_response.json()['commit']['html_url'])
    else:
        print(f"Error updating file: {update_response.json()['message']}")
