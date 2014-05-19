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

"""

version.py: A bunch of API methods for interacting with v4 server version in the PuppetDB API.

The response will be in application/json, and will return a JSON map with a single key: version, whose value is a string representation of the version of the running PuppetDB server.

{"version": "X.Y.Z"}

"""

__author__ = "monkee"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_version(api_url=None, verify=False, cert=list()):
    """
    Returns server version

    :param api_url: Base PuppetDB API url

    Response

    {
        {"version": "X.Y.Z"}
    }
    """
    return utils._make_api_request(api_url, '/version', verify, cert)

