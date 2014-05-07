from mock import Mock
import fixtures
import json

def mock_api_request(host_url=None, path=None, *args, **kwargs):
    resp = Mock()
    # HACK: find the api version in url
    data = None
    if host_url.find('v2') > -1:
        data = fixtures.v2().get(path)
    elif host_url.find('v3') > -1:
        data = fixtures.v3().get(path)
    elif host_url.find('v4') > -1:
        data = fixtures.v4().get(path)

    resp.content = json.dumps(data)
    resp.headers = kwargs.get('headers')
    return resp
