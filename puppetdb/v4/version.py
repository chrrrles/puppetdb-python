#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

version.py: A bunch of API methods for interacting with v4 server version in the PuppetDB API.

The response will be in application/json, and will return a JSON map with a single key: version, whose value is a string representation of the version of the running PuppetDB server.

{"version": "X.Y.Z"}

"""

__author__ = "monkee"
__license__ = "GPL"
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

