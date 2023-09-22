import requests
import json

# GitLab API endpoint and access token
API_URL = "https://gitlab.com/api/v4/projects"
ACCESS_TOKEN = "glpat-9McAqdmiXzF2y2RPxgj_"

# Project details
project_name = "TestProject"
project_description = "Automated project creation"
visibility = "private"  # Options: "private", "internal", "public"
# Create project payload
data = {
    "name": project_name,
    "description": project_description,
    "visibility": visibility,
}
headers = {"PRIVATE-TOKEN": ACCESS_TOKEN}
# Send API request to create project
response = requests.post(API_URL, data=data, headers=headers)
if response.status_code == 201:
    project_info = response.json()
    print("Project created successfully:", project_info["web_url"])
else:
    print("Failed to create project. Status code:", response.status_code)