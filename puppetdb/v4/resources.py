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

"""resources.py: A bunch of API methods for interacting with v4 resources in the PuppetDB API."""

__author__ = "monkee"
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
