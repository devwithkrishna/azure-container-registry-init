import json
import os
import requests


def create_template_repo(organization: str,template_repo:str, repo_name: str):
	"""create github org based on template repo"""
	print(f"New repo will be created on Organization {organization} named {repo_name} referring {template_repo} as template")
	headers = {
		"Accept": "application/vnd.github+json",
		"Authorization": f"Bearer {os.getenv('GH_APP_TOKEN')}",
		"X-GitHub-Api-Version": "2022-11-28"
	}
	endpoint = f"https://api.github.com/repos/{organization}/{template_repo}/generate"

	print(f"Endpoint is {endpoint}")

	data ={
		   "owner": organization,
		   "name": repo_name,
		   "description":"This is your first test repository",
		   "include_all_branches": False,
		   "private":True
		}

	# Get the template repo details
	response = requests.post(url=endpoint, headers=headers, json=data)
	print(response.json())
	pass


def main():
	"""Run the code"""
	# parser = argparse.ArgumentParser("Parse args for repo creation")
	# parser.add_argument("--organization", required=True, default="devwithkrishna", help="github org name")
	# parser.add_argument("--template_repo",nargs='?', default="azure-container-registry-creation-repo", help="github template repo name")
	# parser.add_argument("--repo_name", required=True, help="github new repo name")
	#
	# args = parser.parse_args()

	os.environ["organization"] = "devwithkrishna"
	os.environ["template_repo"] = "azure-container-registry-creation-repo"
	os.environ["repo_name"] = "container1zxserd"

	organization = os.getenv("organization")
	template_repo = os.getenv("template_repo")
	repo_name = os.getenv("repo_name")

	create_template_repo(organization=organization, repo_name=repo_name, template_repo=template_repo)


if __name__ == "__main__":
	main()
