# Python imports
import requests, json
from pprint import pprint

# Module imports
from install_from_github import init_install_path
from tools_github import get_secret

def make_bitly_url(bitly_generic_token, long_url):
    headers = { 'Authorization': str(bitly_generic_token), 'Content-Type': 'application/json' }
    data = { 'long_url': str(long_url), 'domain': 'bit.ly' }
    try:
        r = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=json.dumps(data))
        r.raise_for_status()
    except Exception as e:
        print(e)
    return r.json()

def test_make_bitly_url():
    TEST_URL = 'http://www.nytimes.com'
    BITLY_GENERIC_TOKEN = get_secret()['CREDS2']['AUTH_TOKEN']
    print(f"\nURL to shorten: {TEST_URL}")
    print("\nBit.ly Shortened Report:")
    r = make_bitly_url(BITLY_GENERIC_TOKEN, TEST_URL)
    pprint(r)

if __name__ == '__main__':
    test_make_bitly_url()
