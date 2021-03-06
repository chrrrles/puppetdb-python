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

"""
event_counts.py: A bunch of API methods for interacting with v4 event counts in the PuppetDB API.

Operators
See the Operators page for the full list of available operators. Note that inequality operators (<, >, <=, >=) are only supported against the timestamp FIELD.

Fields
FIELD may be any of the following. Unless otherwise noted, all fields support both equality and regular expression match operators, but do not support inequality operators.

certname: the name of the node that the event occurred on.
report: the id of the report that the event occurred in; these ids can be acquired via event queries or via the /reports query endpoint.
status: the status of the event; legal values are success, failure, noop, and skipped.
timestamp: the timestamp (from the puppet agent) at which the event occurred. This field supports the inequality operators. All values should be specified as ISO-8601 compatible date/time strings.
run-start-time: the timestamp (from the puppet agent) at which the puppet run began. This field supports the inequality operators. All values should be specified as ISO-8601 compatible date/time strings.
run-end-time: the timestamp (from the puppet agent) at which the puppet run finished. This field supports the inequality operators. All values should be specified as ISO-8601 compatible date/time strings.
report-receive-time: the timestamp (from the PuppetDB server) at which the puppet report was received. This field supports the inequality operators. All values should be specified as ISO-8601 compatible date/time strings.
resource-type: the type of resource that the event occurred on; e.g., File, Package, etc.
resource-title: the title of the resource that the event occurred on
property: the property/parameter of the resource that the event occurred on; e.g., for a Package resource, this field might have a value of ensure. NOTE: this field may contain NULL values; see notes below.
new-value: the new value that Puppet was attempting to set for the specified resource property. NOTE: this field may contain NULL values; see notes below.
old-value: the previous value of the resource property, which Puppet was attempting to change. NOTE: this field may contain NULL values; see notes below.
message: a description (supplied by the resource provider) of what happened during the event. NOTE: this field may contain NULL values; see notes below.
file: the manifest file in which the resource definition is located. NOTE: this field may contain NULL values; see notes below.
line: the line (of the containing manifest file) at which the resource definition can be found. NOTE: this field may contain NULL values; see notes below.
containing-class: the Puppet class where this resource is declared. NOTE: this field may contain NULL values; see notes below.
latest-report?: whether the event occurred in the most recent Puppet run (per-node). NOTE: the value of this field is always boolean (true or false without quotes), and it is not supported by the regex match operator.

Notes on fields that allow NULL values
In the case of a skipped resource event, some of the fields of an event may not have values. We handle this case in a slightly special way when these fields are used in equality (=) or inequality (!=) queries; specifically, an equality query will always return false for an event with no value for the field, and an inequality query will always return true.

The response is a JSON array of maps. Each map contains the counts of events that matched the input parameters. The events are counted based on their statuses: failures, successes, noops, skips.

The maps also contain additional data about which object the events occurred on. The subject-type is the value that was used to summarize by (and therefore should match the input value to summarize-by). The subject map contains specific data about the object the event occurred on, and will vary based on the value specified for summarize-by.

When summarizing by certname, the subject will contain a title key:
[
  {
    "subject-type": "certname",
    "subject": { "title": "foo.local" },
    "failures": 0,
    "successes": 2,
    "noops": 0,
    "skips": 1
  },
  {
    "subject-type": "certname",
    "subject": { "title": "bar.local" },
    "failures": 1,
    "successes": 0,
    "noops": 0,
    "skips": 1
  }
]

When summarizing by resource, the subject will contain a type and title key:
[
  {
    "subject-type": "resource",
    "subject": { "type": "Notify", "title": "Foo happened" },
    "failures": 0,
    "successes": 1,
    "noops": 0,
    "skips": 0
  },
  {
    "subject-type": "resource",
    "subject": { "type": "Notify", "title": "Bar happened" },
    "failures": 0,
    "successes": 0,
    "noops": 0,
    "skips": 1
  }
]

When summarizing by containing-class, the subject will contain a title key:
[
  {
    "subject-type": "containing-class",
    "subject": { "title": "Foo::Class" },
    "failures": 1,
    "successes": 2,
    "noops": 0,
    "skips": 1
  },
  {
    "subject-type": "containing-class",
    "subject": { "title": null },
    "failures": 0,
    "successes": 0,
    "noops": 2,
    "skips": 0
  }
]

"""

__author__ = "monkee"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

from puppetdb import utils

API_VERSION = 'v3'

def get_event_counts(api_url=None, query='', summarize_by='', count_by='', counts_filter='', distinct_resources='', verify=False, cert=list()):
    """
    Returns facts

    :param api_url: Base PuppetDB API url
    :param query: Required. A JSON array of query predicates in prefix form (["<OPERATOR>", "<FIELD>", "<VALUE>"]). This query is forwarded to the events endpoint - see there for additional documentation.
    :param summarize_by: Required. A string specifying which type of object you’d like to see counts for. Supported values are resource, containing-class, and certname.
    :param count_by: Optional. A string specifying what type of object is counted when building up the counts of successes, failures, noops, and skips. Supported values are resource (default) and certname.
    :param counts_filter: Optional. A JSON array of query predicates in the usual prefix form. This query is applied to the final event counts output. Supported operators are =, >, <, >=, and <=. Supported fields are failures, successes, noops, and skips.
    :param distinct_resources: Optional. (EXPERIMENTAL: it is possible that the behavior of this parameter may change in future releases.) This parameter is passed along to the event query - see there for additional documentation.

    Response
    When summarizing by certname, the subject will contain a title key:
    [
      {
        "subject-type": "certname",
        "subject": { "title": "foo.local" },
        "failures": 0,
        "successes": 2,
        "noops": 0,
        "skips": 1
      },
      {
        "subject-type": "certname",
        "subject": { "title": "bar.local" },
        "failures": 1,
        "successes": 0,
        "noops": 0,
        "skips": 1
      }
    ]
    When summarizing by resource, the subject will contain a type and title key:
    [
      {
        "subject-type": "resource",
        "subject": { "type": "Notify", "title": "Foo happened" },
        "failures": 0,
        "successes": 1,
        "noops": 0,
        "skips": 0
      },
      {
        "subject-type": "resource",
        "subject": { "type": "Notify", "title": "Bar happened" },
        "failures": 0,
        "successes": 0,
        "noops": 0,
        "skips": 1
      }
    ]
    When summarizing by containing-class, the subject will contain a title key:
    [
      {
        "subject-type": "containing-class",
        "subject": { "title": "Foo::Class" },
        "failures": 1,
        "successes": 2,
        "noops": 0,
        "skips": 1
      },
      {
        "subject-type": "containing-class",
        "subject": { "title": null },
        "failures": 0,
        "successes": 0,
        "noops": 2,
        "skips": 0
      }
    ]
    """
    return utils._make_api_request(api_url, '/event-counts', verify, cert, params={'query': query,'summarize-by':summarize_by,'count-by':count_by,'counts-filter':counts_filter,'distinct_resources':distinct_resources})
