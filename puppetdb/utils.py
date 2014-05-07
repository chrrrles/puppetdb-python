#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""utils.py: Handy utility class for this module."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"
import requests
import os
import urllib
try:
    import simplejson as json
except ImportError:
    import json

def api_request(api_base_url='http://localhost:8080/', path='', method='get',
    data=None, params={}, verify=True, cert=list()):
    """
    Wrapper function for requests

    :param api_base_url: Base URL for requests
    :param path: Path to request
    :param method: HTTP method
    :param data: Data for post (ignored for GETs)
    :param params: Dict of key, value query params
    :param verify: True/False/CA_File_Name to perform SSL Verification of CA Chain
    :param cert: list of cert and key to use for client authentication

    """
    method = method.lower()
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }
    methods = {
        'get': requests.get,
        'post': requests.post,
    }
    if path[0] != '/':
        path = '/{0}'.format(path)
    if params:
        path += '?{0}'.format(urllib.urlencode(params))
    url = '{0}{1}'.format(api_base_url, path)
    resp = methods[method](url, data=json.dumps(data), headers=headers,
                           verify=verify, cert=cert)
    return resp

def _make_api_request(api_url=None, path=None, verify=False, cert=list(),
                      params={}):
    resp = api_request(api_url, path, params=params, verify=verify, cert=cert)
    data = json.loads(resp.content)
    return data

