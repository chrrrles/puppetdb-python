#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013 Arcus, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""helpers.py: These are helper mock functions for testing this module."""

__author__ = "monkee"
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
