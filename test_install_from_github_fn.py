# Python imports
import json
from types import SimpleNamespace

# Pythonista imports
import console
from pprint import pprint
import shortcuts

# Module imports
from tools_github import get_secret
from install_from_github import init_install_path, make_git_url, install_from_github

# globals
GIT_AUTH = get_secret()['CREDS1']['AUTH_TOKEN']

config_dict = json.load(open('install_config.json'))
c = SimpleNamespace(**config_dict)

def test_install_from_github():
    console.clear()
    print("*** Testing Module Functions from: install_from_github.py ***\n")
    install_path = init_install_path(c.install_dir_name)
    url = make_git_url(c.git_usr, c.git_repo, c.git_branch)
    installed_files = install_from_github(install_path, GIT_AUTH, url)
    print(f"Installed the following files from: {url} ")
    pprint(installed_files)

if __name__ == '__main__':
    test_install_from_github()