import json
import urllib.request
import urllib.error

base = 'http://127.0.0.1:8000'


def request(path, method='GET', data=None):
    body = None if data is None else json.dumps(data).encode()
    req = urllib.request.Request(base + path, data=body, method=method)
    if data is not None:
        req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(method, path, resp.status)
            print(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(method, path, 'HTTP', e.code)
        print(e.read().decode())


request('/')
request('/api/tasks/')
request('/api/tasks/', method='POST', data={'title': 'Test task from script'})
request('/api/tasks/')
