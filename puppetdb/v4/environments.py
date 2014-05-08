#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
environments.py: A bunch of API methods for interacting with v4 facts in the PuppetDB API.

Successful responses will be in application/json. Errors will be returned as non-JSON strings.

The response is a JSON array of hashes of the form:

{"name": <string>}
"""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v4'

def get_environments(api_url=None, query='', verify=False, cert=list()):
    """
    Returns environments

    :param api_url: Base PuppetDB API url
    :param query: Optional. A JSON array containing the query in prefix notation. If not provided, all results will be returned.

    Available Fields
    "name": matches environments of the given name

    Response
    {"name": <string>}
    """
    return utils._make_api_request(api_url, '/environments', verify, cert, params={'query': query})

def get_environments_by_name(api_url=None, environment_name=None, verify=False, cert=list()):
    """
    Returns environments by name

    :param api_url: Base PuppetDB API url
    :param environment_name: Name of environment

    Response
    {"name": <string>}]
    """
    return utils._make_api_request(api_url, '/environments/{0}'.format(environment_name), verify, cert)

def get_environments_by_route(api_url=None, environment_name=None, route='', query='', verify=False, cert=list()):
    """
    These routes are identical to issuing a request to /v4/[events|facts|reports|resources], with a query parameter of
    ["=","environment","<ENVIRONMENT>"].
    All query parameters and route suffixes from the original routes are supported. The result format is also the same.
    Additional query parameters are ANDed with the environment clause. See /v4/events, /v4/facts, /v4/reports or /v4/resources for more info.

    :param api_url: Base PuppetDB API url
    :param environment_name: Name of environment
    :param route: [events|facts|reports|resources]

    Response
    As per other routes
    """
    return utils._make_api_request(api_url, '/environments/{0}/{1}'.format(environment_name, route), verify, cert, params={'query': query})
