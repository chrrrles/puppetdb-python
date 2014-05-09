#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""metrics.py: A bunch of API methods for interacting with v3 metrics in the PuppetDB API."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_metric_names(api_url=None, verify=False, cert=list()):
    """
    Returns all available metric names

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/metrics/mbeans', verify, cert)

def get_metric_by_name(api_url=None, metric_name=None, verify=False, cert=list()):
    """
    Returns info for a Node

    :param api_url: Base PuppetDB API url
    :param metric_name: Name of metric

    """
    return utils._make_api_request(api_url, '/metrics/mbean/{0}'.format(metric_name), verify, cert)
