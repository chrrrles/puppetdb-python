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

"""fact_names.py: A bunch of API methods for interacting with v3 server time in the PuppetDB API."""

__author__ = "monkee"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_server_time(api_url=None, verify=False, cert=list()):
    """
    Returns fact names

    :param api_url: Base PuppetDB API url

    Response

    {
        "server-time": "2013-09-20T20:54:27.472Z"
    }
    """
    return utils._make_api_request(api_url, '/server-time', verify, cert)

