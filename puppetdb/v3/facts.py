#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""facts.py: A bunch of API methods for interacting with v3 facts in the PuppetDB API."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_facts(api_url=None, query='', verify=False, cert=list()):
    """
    Returns facts

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/facts', verify, cert, params={'query': query})

def get_facts_by_name(api_url=None, fact_name=None, verify=False, cert=list()):
    """
    Returns facts by name

    :param api_url: Base PuppetDB API url
    :param fact_name: Name of fact

    """
    return utils._make_api_request(api_url, '/facts/{0}'.format(fact_name), verify, cert)

def get_facts_by_name_and_value(api_url=None, fact_name=None, fact_value=None, verify=False, cert=list()):
    """
    Returns facts by name and value

    :param api_url: Base PuppetDB API url
    :param fact_name: Name of fact
    :param fact_value: Value of fact

    """
    return utils._make_api_request(api_url, '/facts/{0}/{1}'.format(fact_name, fact_value), verify, cert)
