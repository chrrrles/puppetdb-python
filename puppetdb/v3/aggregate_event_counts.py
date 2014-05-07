#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""facts.py: A bunch of API methods for interacting with v3 aggregate event counts in the PuppetDB API."""



__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_aggregate_event_counts(api_url=None, query='', summarize_by='', count_by='', counts_filter='', distinct_resources='', verify=False, cert=list()):
    """
    Returns facts

    :param api_url: Base PuppetDB API url
    :param query: Required. A JSON array of query predicates in prefix form (["<OPERATOR>", "<FIELD>", "<VALUE>"]). This query is forwarded to the events endpoint - see there for additional documentation.
    :param summarize_by: Required. A string specifying which type of object you’d like to see counts for. Supported values are resource, containing-class, and certname.
    :param count_by: Optional. A string specifying what type of object is counted when building up the counts of successes, failures, noops, and skips. Supported values are resource (default) and certname.
    :param counts_filter: Optional. A JSON array of query predicates in the usual prefix form. This query is applied to the final event counts output. Supported operators are =, >, <, >=, and <=. Supported fields are failures, successes, noops, and skips.
    :param distinct_resources: Optional. (EXPERIMENTAL: it is possible that the behavior of this parameter may change in future releases.) This parameter is passed along to the event query - see there for additional documentation.

    Response Format

    {
        "successes": 2,
        "failures": 0,
        "noops": 0,
        "skips": 1,
        "total": 3
    }
    """
    return utils._make_api_request(api_url, '/aggregate-event-counts', verify, cert, params={'query': query,'summarize-by':summarize_by,'count-by':count_by,'counts-filter':counts_filter,'distinct_resources':distinct_resources})
