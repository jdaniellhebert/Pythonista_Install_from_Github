# Python imports
import os, json, console
from types import SimpleNamespace

# Pythonista imports
from pprint import pprint
import shortcuts
import qrcode
import console

# Module imports
from install_from_github import init_install_path
from make_url_scheme import make_run_url_scheme
from tools_github import get_secret

# globals for test functions

RAW_CODE = 'install_from_github.py'
INSTALL_DIR_NAME = 'from-Github'
GIT_AUTH = '' # empty because this is a public repository
GIT_USR = 'jdaniellhebert'
GIT_REPO = 'Pythonista-Github-Installer'
GIT_BRANCH = 'master'
START_FILE = 'installer_app.py'
IS_RELEASE = 'False'
SHORTCUTS_URL = ''

def make_argv_pyld(argv):
    argv_pyld = ''
    for arg in argv:
        argv_pyld = argv_pyld + '&argv=' + arg
    print(f"argv_pyld: {argv_pyld}")
    return argv_pyld

console.clear()

code_url = 'https://raw.githubusercontent.com/' + GIT_USR + '/' + GIT_REPO + '/' + GIT_BRANCH + '/' + RAW_CODE
exec_code = 'import%20requests%20as%20r;%20exec(r.get(' + code_url + ').content)'
argv = [INSTALL_DIR_NAME, GIT_AUTH, GIT_USR, GIT_REPO, GIT_BRANCH, START_FILE, IS_RELEASE]
argv_pyld = make_argv_pyld(argv)
url_scheme = 'pythonista://?exec='+ exec_code + argv_pyld

print(f"\nURL scheme: {url_scheme}")
url_file = 'install_installer.url'
open(url_file, "w").write(url_scheme)
print(f"\nURL Scheme saved as: {url_file}")

img = qrcode.make(url_scheme)
img.show()
qrcode_file = 'install_installer.jpg'
img.save(qrcode_file)
print(f"\nQR Code saved as: {qrcode_file}")