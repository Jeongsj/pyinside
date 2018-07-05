import requests
import time
from hashlib import sha256
from base64 import b64encode
from urllib.parse import urlencode
from api import API


def get_app_id():
	t = time.localtime()
	app_key = 'dcArdchk_%04d%02d%02d%02d' \
                % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour)
	app_key = sha256(app_key.encode('ascii')).hexdigest()

	app_id = s.post(API['app_id'], data="value_token=" + app_key +
                 "&signature=ReOo4u96nnv8Njd7707KpYiIVYQ3FlcKHDJE046Pg6s=&pkg=com.dcinside.app&vCode=10808&vName=1.8.8").json()
	app_id = app_id[0]['app_id']

	print('app_id: ', app_id)
	return app_id


def redirect(url):
	hash = b64encode(bytes(url.encode("utf8")))
	url = 'http://m.dcinside.com/api/redirect.php?hash={}'.format(hash.decode('utf8'))
	return url


def get(api, body):
    body['app_id'] = app_id
    params = "{}?{}".format(api, urlencode(body))
    return s.get(redirect(params))


def post(api, body):
    body['app_id'] = app_id
    return s.post(api, body)


s = requests.session()
s.headers = {
    'User-Agent': "dcinside.app",
    'Referer': 'http://m.dcinside.com',
    'Content-Type': 'application/x-www-form-urlencoded'
}
app_id = get_app_id()

