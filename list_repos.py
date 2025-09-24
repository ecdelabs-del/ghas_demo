import requests
import os
from os import environ
from datetime import *
import os

# GitHub token is used for demo purposes and is not real
GITHUB_TOKEN = os.environ.get("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N") 
ORGANIZATION_NAME = "YOUR_ORGANIZATION_NAME" # Replace with your organization's name

def list_organization_repositories(org_name, token):
    """
    Lists all repositories for a given GitHub organization.
    Handles pagination to retrieve all repositories.
    """
    repositories = []
    page = 1
    per_page = 100  # Max allowed by GitHub API

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    while True:
        url = f"https://api.github.com/orgs/{org_name}/repos?page={page}&per_page={per_page}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error fetching repositories: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            break

        data = response.json()
        if not data:
            break  # No more repositories to fetch

        repositories.extend(data)
        page += 1

    return repositories

if __name__ == "__main__":
    if GITHUB_TOKEN == "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN" or ORGANIZATION_NAME == "YOUR_ORGANIZATION_NAME":
        print("Please update GITHUB_TOKEN and ORGANIZATION_NAME in the script.")
    else:
        print(f"Fetching repositories for organization: {ORGANIZATION_NAME}...")
        all_repos = list_organization_repositories(ORGANIZATION_NAME, GITHUB_TOKEN)

        if all_repos:
            print(f"Found {len(all_repos)} repositories:")
            for repo in all_repos:
                print(f"- {repo['name']} (Private: {repo['private']})")
        else:
            print("No repositories found or an error occurred.")

# insecure code for demo purposes. Keys are not real.

github_personal_token = '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'
