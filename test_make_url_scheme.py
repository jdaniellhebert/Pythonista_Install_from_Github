# Python imports
import json
from types import SimpleNamespace

# Pytonista imports
import clipboard

# Module imports
from install_from_github import init_install_path
from make_url_scheme import make_exec_url_scheme
from make_url_scheme import make_run_url_scheme

config_dict = json.load(open('install_config.json'))
c = SimpleNamespace(**config_dict)

def test_make_exec_url_scheme():
    install_path = init_install_path(c.install_dir_name)
    url_scheme = make_exec_url_scheme(install_path, c.git_repo, c.git_repo)
    print("\nURL scheme:")
    print(url_scheme)
    return

def test_make_run_url_scheme():
    install_path = init_install_path(c.install_dir_name)
    url_scheme = make_run_url_scheme(install_path, c.git_repo, c.git_repo)
    print("\nURL scheme:")
    print(url_scheme)
    return

if __name__ == '__main__':
    test_make_run_url_scheme()
    test_make_exec_url_scheme()