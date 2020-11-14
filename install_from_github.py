# Python imports
import os, requests, shutil, zipfile, json, sys
from types import SimpleNamespace
from pprint import pprint

# Pythonista imports
import shortcuts
import qrcode

# Package imports
from make_url_scheme import make_run_url_scheme

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

if __name__ == '__main__':
    if len(sys.argv) > 1:
        p_keys = ('module', 'install_dir', 'git_auth', 'git_usr', 'git_repo', 'git_branch', 'start_file', 'is_release')
        params_dict = dict(zip(p_keys, sys.argv))
        p = SimpleNamespace(**params_dict)
        print("\nInstalling:")
        pprint(params_dict)

        install_path = init_install_path(p.install_dir)
        url = make_git_url(p.git_usr, p.git_repo, p.git_branch)
        installed_files = install_from_github(install_path, p.git_auth, url)
        
        print(f"\nUnzipping: {url} ")
        pprint(installed_files)

        installed_dir = install_path + '/' + installed_files[0]

        url_scheme = make_run_url_scheme(install_path, installed_files[0].replace('/',''), p.start_file)
        print(f"\nURL scheme: {url_scheme}")
        url_file = p.start_file.split('.')[0] + '.url'
        open(installed_dir + url_file, "w").write(url_scheme)
        print(f"\nURL Scheme saved as: {url_file}")

        img = qrcode.make(url_scheme)
        img.show()
        qrcode_file = 'qrcode' + '-' + p.start_file.split('.')[0] + '.jpg'
        img.save(installed_dir + qrcode_file)
        print(f"\nQR Code saved as: {qrcode_file}")
    else:
        print(f"(ERROR) -- Missing parameters for module {sys.argv[0]}")

    # Pythonisat URL Scheme Template
    # pythonista://install_from_github.py?action=run&argv=<INSTALL_DIR>&argv=<GIT_AUTH>
    #                                               &argv=<GIT_USR>&argv=<GIT_REPO>&argv=<GIT_BRANCH>
    #                                               &argv=<START_FILE>
