#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""resources.py: A bunch of API methods for interacting with v3 resources in the PuppetDB API."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_resources(api_url=None, query='', verify=False, cert=list()):
    """
    Returns resources

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/resources', verify, cert, params={'query': query})

def get_resources_by_name(api_url=None, resource_name=None, verify=False, cert=list()):
    """
    Returns facts by name

    :param api_url: Base PuppetDB API url
    :param resource_name: Name of resource

    """
    return utils._make_api_request(api_url, '/resources/{0}'.format(resource_name), verify, cert)

def get_resources_by_name_and_value(api_url=None, resource_name=None, resource_value=None, verify=False, cert=list()):
    """
    Returns resources by name and value

    :param api_url: Base PuppetDB API url
    :param resource_name: Name of fact
    :param resource_value: Value of fact

    """
    return utils._make_api_request(api_url, '/resources/{0}/{1}'.format(resource_name, resource_value), verify, cert)
