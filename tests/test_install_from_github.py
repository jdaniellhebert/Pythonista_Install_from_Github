# To run this test easily move from tests folder to parent folder.

# Python imports
import os, json, console
from types import SimpleNamespace

# Pythonista imports
from pprint import pprint
import shortcuts

# Module imports
from install_from_github import init_install_path
from make_url_scheme import make_run_url_scheme
from tools_github import get_secret

# globals for test functions
GIT_AUTH = get_secret()['CREDS1']['AUTH_TOKEN']
CONFIG_DICT =   {
                "install_dir_name" : "from-Github",
                "git_usr" : "dh-metre",
                "git_repo" : "Metre-UI-App-Pythonista",
                "git_branch" : "v0.1",
                "start_file" : "App.py",
                "is_release" : "True"
                }

# config_dict = json.load(open('install_config.json'))
c = SimpleNamespace(**CONFIG_DICT)

def test_install_from_url_scheme():
    console.clear()
    print("*** Testing URL Scheme __main__ for: install_from_github.py ***\n")

    path = os.path.dirname(os.path.abspath(__file__)) + '/install_from_github.py'

    argv = [c.install_dir_name, GIT_AUTH, c.git_usr, c.git_repo, c.git_branch, c.start_file, c.is_release]

    url_scheme = shortcuts.pythonista_url(path=path, action='run', args="", argv=argv)

    print(f"URL Scheme: {url_scheme}")

    # shortcuts.open_url(url_scheme)

    # Expected URL Scheme output to match install_from_github.py __main__ argv parameters:
    # pythonista://install_from_github.py?action=run&argv=<INSTALL_DIR>&argv=<GIT_AUTH>
    #                                               &argv=<GIT_USR>&argv=<GIT_REPO>&argv=<GIT_BRANCH>
    #                                               &argv=<START_FILE>

if __name__== '__main__':
    test_install_from_url_scheme()
