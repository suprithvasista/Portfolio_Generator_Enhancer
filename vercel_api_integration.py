import requests

def vercel_project_deployment(VERCEL_TOKEN_VAL,repo_name_project_nam_val,VERCEL_PROJECT_NAME_VAL):
    GITHUB_BRANCH = 'main'  # Replace with your branch name (e.g., "main", "master")
    VERCEL_TOKEN = VERCEL_TOKEN_VAL  # Vercel API token
    repo_name_project_name=repo_name_project_nam_val
    git_repo_id_url=requests.get("https://api.github.com/repos/"+ repo_name_project_name)
    if git_repo_id_url.status_code == 200:
        deployment_info = git_repo_id_url.json()
        print(f"Fetching repo id: {git_repo_id_url}")
    else:
        print(f"Error while fetch repo id: {git_repo_id_url.status_code}")
        print(git_repo_id_url.text)
    GITHUB_REPO_ID=git_repo_id_url.json()['id']# GitHub repository URL
    VERCEL_PROJECT_NAME = VERCEL_PROJECT_NAME_VAL  # The name of your project on Vercel
    # Vercel API URL
    url = "https://api.vercel.com/v12/deployments"

    # Headers to authenticate the request
    headers = {
        "Authorization": f"Bearer {VERCEL_TOKEN}",
        "Content-Type": "application/json"
    }

    # Deployment payload
    payload = {
        "name": VERCEL_PROJECT_NAME,  # Vercel project name
        "gitSource": {
            "type": "github",  # Specify GitHub as the source
            "repoId": GITHUB_REPO_ID,
            "ref": GITHUB_BRANCH,
        },
        "projectSettings": {
            "framework": None,  # Specify "Other" as the platform framework
            "buildCommand": "flutter/bin/flutter build web --release",
            "outputDirectory": "build/web",
            "installCommand":
                "if cd flutter; then git pull && cd .. ; else "
                "git clone https://github.com/flutter/flutter.git; fi && "
                "flutter/bin/flutter doctor && flutter/bin/flutter clean && "
                "flutter/bin/flutter config --enable-web",
        },
    }

    # Make the API request to deploy
    response = requests.post(url, headers=headers, json=payload)
    
    # Check and print the response
    if response.status_code == 200:
        deployment_info = response.json()
        print(f"Deployment triggered successfully! View it at: {deployment_info['url']}")
        print(deployment_info)
        return [0,deployment_info['alias'][0]]
    else:
        print(f"Error triggering deployment: {response.status_code}")
        print(response.text)
        return [1,response.text]


