
print("byebye")
# ARGS definition can be appended before this file in create_install_url_scheme.py

# Python imports
import os, requests, shutil, zipfile, json, sys
from types import SimpleNamespace
from pprint import pprint

# Pythonista imports
import shortcuts
import qrcode
import requests

CONFIG_DICT =   {
                "install_dir_name" : "from-Github",
                "git_usr" : "dh-metre",
                "git_repo" : "Metre-UI-App-Pythonista",
                "git_branch" : "v0.1",
                "start_file" : "App.py",
                "is_release" : "True"
                }

c = SimpleNamespace(**CONFIG_DICT)

def init_install_path(install_dir_name):
    install_path = os.path.abspath(os.path.expanduser('~/Documents/' + install_dir_name))
    os.makedirs(install_path, exist_ok=True)
    return install_path

def make_git_url(usr, repo, branch):
    URL_TEMPLATE = 'https://github.com/{}/{}/archive/{}.zip'
    url = URL_TEMPLATE.format(usr, repo, branch)
    return url

def git_headers(git_pat):
    token = "token " + git_pat
    headers = {"Authorization": token}
    return headers

def install_from_github(install_path, auth_token, url):
    token_pyld = "token " + auth_token
    headers = {"Authorization": token_pyld}
    dwnld_zipfile = '/'+ url.split('/')[-1]
    local_zipfile = install_path + dwnld_zipfile
    try:
        r = requests.get(url, stream=True, headers=headers)
        r.raise_for_status()
        with open(local_zipfile, 'wb') as f:
            block_sz = 1024
            for chunk in r.iter_content(block_sz):
                f.write(chunk)
        z = zipfile.ZipFile(local_zipfile)
        z.extractall(install_path)
        unzipped_dirname = z.namelist()[0]
        os.remove(local_zipfile)
        return z.namelist()
    except Exception as e:
        print(f"Install Error: {e}")
        return None

def install_branch(params):
    install_path = init_install_path(params.install_dir)
    url = make_git_url(params.git_usr, params.git_repo, params.git_branch)
    installed_files = install_from_github(install_path, params.git_auth, url)
    print(f"\nUnzipping: {url} ")
    pprint(installed_files)
    return install_path, url, installed_files

def create_url_scheme_and_qr_code(installed_dir, url_scheme, start_file):
    url_file = start_file.split('.')[0] + '.url'
    open(installed_dir + url_file, "w").write(url_scheme)
    print(f"\nURL Scheme saved as: {url_file}")

    img = qrcode.make(url_scheme)
    img.show()
    qrcode_file = 'qrcode' + '-' + start_file.split('.')[0] + '.jpg'
    img.save(installed_dir + qrcode_file)
    print(f"\nQR Code saved as: {qrcode_file}")

def main():
    print('hello')
    if len(sys.argv) > 1:
        p_keys = ('module', 'install_dir', 'git_auth', 'git_usr', 'git_repo', 'git_branch', 'start_file', 'is_release')
        params_dict = dict(zip(p_keys, sys.argv))
        print("\nInstalling:")
        pprint(params_dict)

        params = SimpleNamespace(**params_dict)
        install_path, url, installed_files = install_branch(params)

        start_path = install_path + '/' + installed_files[0].replace('/','') + '/' + params.start_file
        url_scheme = shortcuts.pythonista_url(path=start_path, action='run', args="", argv=[])
        print(f"\nURL scheme: {url_scheme}")

        installed_dir = install_path + '/' + installed_files[0]
        create_url_scheme_and_qr_code(installed_dir, url_scheme, params.start_file)
    else:
        print("\nInstalling:")
        pprint(CONFIG_DICT)
        install_path, url, installed_files = install_branch(params)

        start_path = install_path + '/' + installed_files[0].replace('/','') + '/' + params.start_file
        url_scheme = shortcuts.pythonista_url(path=start_path, action='run', args="", argv=[])
        print(f"\nURL scheme: {url_scheme}")

        installed_dir = install_path + '/' + installed_files[0]
        create_url_scheme_and_qr_code(installed_dir, installed_dir, url_scheme, start_file)

if __name__ == '__main__':
    main()
