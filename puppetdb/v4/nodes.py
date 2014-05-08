#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""nodes.py: A bunch of API methods for interacting with v4 nodes in the PuppetDB API."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"


from puppetdb import utils

API_VERSION = 'v3'

def get_nodes(api_url=None, verify=False, cert=list()):
    """
    Returns info for all Nodes

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/nodes', verify, cert)

def get_node(api_url=None, node_name=None, verify=False, cert=list()):
    """
    Returns info for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node

    """
    return utils._make_api_request(api_url, '/nodes/{0}'.format(node_name), verify, cert)

def get_node_facts(api_url=None, node_name=None, verify=False, cert=list()):
    """
    Returns facts for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node

    """
    return utils._make_api_request(api_url, '/nodes/{0}/facts'.format(node_name), verify, cert)

def get_node_fact_by_name(api_url=None, node_name=None, fact_name=None, verify=False, cert=list()):
    """
    Returns specified fact for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node
    :param fact_name: Name of fact

    """
    return utils._make_api_request(api_url, '/nodes/{0}/facts/{1}'.format(node_name,
        fact_name), verify, cert)

def get_node_resources(api_url=None, node_name=None, verify=False, cert=list()):
    """
    Returns resources for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node

    """
    return utils._make_api_request(api_url, '/nodes/{0}/resources'.format(node_name), verify, cert)

def get_node_resource_by_type(api_url=None, node_name=None,
    type_name=None, verify=False, cert=list()):
    """
    Returns specified resource for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node
    :param type_name: Type of resource

    """
    return utils._make_api_request(api_url, '/nodes/{0}/resources/{1}'.format(node_name,
        type_name), verify, cert)

def get_facts(api_url=None, query={}, verify=False, cert=list()):
    """
    Returns info for all Nodes

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/nodes', verify, cert)
