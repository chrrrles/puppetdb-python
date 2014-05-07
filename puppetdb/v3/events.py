#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""facts.py: A bunch of API methods for interacting with v3 events in the PuppetDB API."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_events(api_url=None, query='', verify=False, cert=list()):
    """
    Returns facts

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/events', verify, cert, params={'query': query})
