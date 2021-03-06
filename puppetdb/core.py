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

"""PuppetDBClientTestCaseV3.py: The core of this module"""

__author__ = "monkee"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

import utils
import v2
import v3
import v4

class ClientException(BaseException):
    pass

class AuthException(BaseException):
    pass

class PuppetDBClient(object):
    def __init__(self, host='localhost', port=8080, api_version='v3',
        use_ssl=False, verify=True, cert=list()):
        self._host = host
        self._port = port
        self._api_version = api_version
        ssl = {
            True: 'https',
            False: 'http',
        }
        apis = {
            'v2': v2,
            'v3': v3,
            'v4': v4,
        }
        self._api = apis[api_version]
        self._verify = verify
        self._cert = cert
        self._api_url = '{0}://{1}:{2}/{3}'.format(ssl[use_ssl], self._host,
            self._port, api_version)

    def get_nodes(self):
        return self._api.nodes.get_nodes(self._api_url, self._verify, self._cert)

    def get_node(self, node_name=None):
        return self._api.nodes.get_node(self._api_url, node_name, self._verify, self._cert)

    def get_node_facts(self, node_name=None):
        return self._api.nodes.get_node_facts(self._api_url, node_name, self._verify, self._cert)

    def get_node_fact_by_name(self, node_name=None, fact_name=None):
        return self._api.nodes.get_node_fact_by_name(self._api_url, node_name, fact_name, self._verify, self._cert)

    def get_node_resources(self, node_name=None):
        return self._api.nodes.get_node_resources(self._api_url, node_name, self._verify, self._cert)

    def get_node_resource_by_type(self, node_name=None, type_name=None):
        return self._api.nodes.get_node_resource_by_type(self._api_url, node_name,
            type_name, self._verify, self._cert)

    def get_facts(self, query=''):
        return self._api.facts.get_facts(self._api_url, query, self._verify, self._cert)
    
    def get_facts_by_name(self, fact_name):
        return self._api.facts.get_facts_by_name(self._api_url, fact_name, self._verify, self._cert)
    
    def get_facts_by_name_and_value(self, fact_name, fact_value):
        return self._api.facts.get_facts_by_name_and_value(self._api_url, fact_name, fact_value, self._verify, self._cert)

    def get_catalog(self, node_name):
        return self._api.catalogs.get_catalog(self._api_url, node_name, self._verify, self._cert)

    def get_resources(self, query=''):
        return self._api.resources.get_resources(self._api_url, query, self._verify, self._cert)

    def get_resources_by_name(self, resource_name):
        return self._api.resources.get_resources_by_name(self._api_url, resource_name, self._verify, self._cert)

    def get_resources_by_name_and_value(self, resource_name, resource_value):
        return self._api.resources.get_resources_by_name_and_value(self._api_url, resource_name, resource_value, self._verify, self._cert)

    def get_fact_names(self):
        return self._api.fact_names.get_fact_names(self._api_url, self._verify, self._cert)

    def get_reports(self, query=''):
        return self._api.reports.get_reports(self._api_url, query, self._verify, self._cert)

    def get_events(self, query=''):
        return self._api.events.get_events(self._api_url, query, self._verify, self._cert)

    def get_event_counts(self, query='', summarize_by='', count_by='', counts_filter='', distinct_resources=''):
        return self._api.event_counts.get_event_counts(self._api_url, query, summarize_by, count_by, counts_filter, distinct_resources, self._verify, self._cert)

    def get_aggregate_event_counts(self, query='', summarize_by='', count_by='', counts_filter='', distinct_resources=''):
        return self._api.aggregate_event_counts.get_aggregate_event_counts(self._api_url, query, summarize_by, count_by, counts_filter, distinct_resources,self._verify, self._cert)

    def get_server_time(self):
        return self._api.server_time.get_server_time(self._api_url, self._verify, self._cert)

    def get_metric_names(self):
        return self._api.metrics.get_metric_names(self._api_url, self._verify, self._cert)

    def get_metrics_by_name(self, metric_name):
        return self._api.metrics.get_metrics_by_name(self._api_url, metric_name, self._verify, self._cert)

    def get_version(self):
        return self._api.version.get_version(self._api_url, self._verify, self._cert)

    def get_environments(self, query=''):
        return self._api.environments.get_environments(self._api_url, query, self._verify, self._cert)

    def get_environments_by_name(self, environment_name):
        return self._api.enviroments.get_environemnts_by_name(self._api_url, environment_name, self._verify, self._cert)

    def get_environments_by_route(self, environment_name, route, query):
        return self._api.environments.get_resources_by_route(self._api_url, environment_name, route, query, self._verify, self._cert)