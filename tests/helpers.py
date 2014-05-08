#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""helpers.py: These are helper mock functions for testing this module."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from mock import Mock
import v2_fixtures,v3_fixtures,v4_fixtures
import json

def mock_api_request(host_url=None, path=None, *args, **kwargs):
    resp = Mock()
    # HACK: find the api version in url
    data = None
    if host_url.find('v2') > -1:
        data = v2_fixtures.v2().get(path)
    elif host_url.find('v3') > -1:
        data = v3_fixtures.v3().get(path)
    elif host_url.find('v4') > -1:
        data = v4_fixtures.v4().get(path)

    resp.content = json.dumps(data)
    resp.headers = kwargs.get('headers')
    return resp
