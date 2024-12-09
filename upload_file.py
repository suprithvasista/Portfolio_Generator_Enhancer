import streamlit as st
import requests
import json

def photo_upload(GITHUB_TOKEN_VAL,REPO_OWNER_VAL,REPO_NAME_VAL,FILE_PATH_VAL,encoded_content):
    # GitHub credentials
    GITHUB_TOKEN = GITHUB_TOKEN_VAL# Replace with your actual token
    REPO_OWNER = REPO_OWNER_VAL# Your GitHub username (forked repo owner)
    REPO_NAME = REPO_NAME_VAL# Name of the forked repository
    BRANCH = 'main'  # Git branch to commit the file to, e.g., 'main' or 'master'
    file_path=FILE_PATH_VAL
    # GitHub API URL for uploading the file
    API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/'



  # Use the uploaded file's name as the file path in the repo
    data = {
        "message": f"Upload {file_path} via Streamlit",  # Commit message
        "content": encoded_content,  # Base64 encoded image content
        "branch": BRANCH  # The branch to commit the file to
    }

    # GitHub API headers for authentication
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Send the PUT request to upload the image to the repository
    response = requests.put(API_URL + file_path, headers=headers, data=json.dumps(data))
    # Handle the response
    if response.status_code == 201:
        st.success(f"File uploaded successfully! View it here: {response.json()['content']['html_url']}")
    else:
        st.error(f"Error uploading file: {response.json()['message']}")
