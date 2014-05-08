#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""fact_names.py: A bunch of API methods for interacting with v4 server time in the PuppetDB API."""

__author__ = "monkee"
__license__ = "GPL"
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

