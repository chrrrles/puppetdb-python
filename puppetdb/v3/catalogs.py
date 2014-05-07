#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""resources.py: A bunch of API methods for interacting with v3 catalogs in the PuppetDB API."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_catalogs(api_url=None, node_name=None, verify=False, cert=list()):
    """
    Returns catalogs by node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node

    """
    return utils._make_api_request(api_url, '/catalogs/{0}'.format(node_name), verify, cert)

