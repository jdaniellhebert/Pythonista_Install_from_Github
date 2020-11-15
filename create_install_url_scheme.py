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
from tools_github import get_secret

# https://raw.githubusercontent.com/jdaniellhebert/Pythonista_Install_from_Github/main/install_from_github.py

RAW_CODE = 'install_from_github.py'
SHORTCUTS_URL = ''

console.clear()

config_dict = json.load(open('install_config.json'))
c = SimpleNamespace(**config_dict)

params_url = f"https://raw.githubusercontent.com/jdaniellhebert/Pythonista_Install_from_Github/main/install_config.json"
code_url = f"'https://raw.githubusercontent.com/{c.git_usr}/{c.git_repo}/{c.git_branch}/{RAW_CODE}'"
glbls = {}
lcls = {'p_url':params_url}
exec_code = f"import requests as r; exec(r.get({code_url}).content)".replace(' ', '%20') # requests needs spaces represented by %20
url_scheme =  f"pythonista://?exec={exec_code}"

print(f"\nURL scheme: {url_scheme}")
url_file = 'install_installer.url'
open(url_file, "w").write(url_scheme)
print(f"\nURL Scheme saved as: {url_file}")

img = qrcode.make(url_scheme)
img.show()
qrcode_file = 'install_installer.jpg'
img.save(qrcode_file)
print(f"\nQR Code saved as: {qrcode_file}")

shortcuts.open_url(url_scheme)
