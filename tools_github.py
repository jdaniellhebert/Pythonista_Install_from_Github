import json
from github import GitHub
from pprint import pprint

SECRETS_PATH = '../secrets.json'

def get_secret():
	return json.load(open(SECRETS_PATH))

def get_repos(gh_obj):
	repos = gh_obj.user.repos.get()
	repo_dicts=[]
	for repo in repos:
		usr = repo['owner']['login']
		repo_nm = repo['name']
		repo_dicts.append({'usr':usr, 'repo':repo_nm})
	return repo_dicts

def get_releases(gh_obj, repo_dict):
	releases = gh_obj.repos(repo_dict['usr'])(repo_dict['repo']).releases.get()
	release_dicts = []
	for release in releases:
		title = release['name']
		tag = release['tag_name']
		release_dicts.append({'usr':repo_dict['usr'], 'repo':repo_dict['repo'], 'branch':tag})
	return release_dicts

def get_branches(gh_obj, repo_dict):
	branches = gh_obj.repos(repo_dict['usr'])(repo_dict['repo']).branches.get()
	branch_dicts = []
	for branch in branches:
		tag = branch['name']
		branch_dicts.append({'usr':repo_dict['usr'], 'repo':repo_dict['repo'], 'branch': tag})
	return branch_dicts

def test_tools_github():
	GIT_AUTH = get_secret['CREDS1']['AUTH_TOKEN']
	gh = GitHub(access_token=GIT_AUTH)
	repos = get_repos(gh)
	for repo_dict in repos:
		releases = get_releases(gh, repo_dict)
		branches = get_branches(gh, repo_dict)
	pprint(releases)
	print()
	pprint(branches)

if __name__ == '__main__':
	test_tools_github()


