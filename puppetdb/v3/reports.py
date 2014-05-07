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
reports.py: A bunch of API methods for interacting with v3 reports in the PuppetDB API.

Operators
The only available OPERATOR is =.

Fields
FIELD may be any of the following. All fields support only the equality operator.

certname
the name of the node that the report was received from.
hash
the id of the report; these ids can be acquired via event queries (see the /events query endpoint).

The response is a JSON array of report summaries for all reports that matched the input parameters.
The summaries are sorted by the completion time of the report, in descending order:
[
  {
    "end-time": "2012-10-29T18:38:01.000Z",
    "puppet-version": "3.0.1",
    "receive-time": "2012-10-29T18:38:04.238Z",
    "configuration-version": "1351535883",
    "start-time": "2012-10-29T18:38:00.000Z",
    "hash": "bd899b1ee825ec1d2c671fe5541b5c8f4a783472",
    "certname": "foo.local",
    "report-format": 4,
    "transaction-uuid": "030c1717-f175-4644-b048-ac9ea328f221"
    },
  {
    "end-time": "2012-10-26T22:39:32.000Z",
    "puppet-version": "3.0.1",
    "receive-time": "2012-10-26T22:39:35.305Z",
    "configuration-version": "1351291174",
    "start-time": "2012-10-26T22:39:31.000Z",
    "hash": "cd4e5fd8846bac26d15d151664a40e0f2fa600b0",
    "certname": "foo.local",
    "report-format": 4,
    "transaction-uuid": null
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

def get_reports(api_url=None, query='', verify=False, cert=list()):
    """
    Returns reports

    :param api_url: Base PuppetDB API url
    :param query: Required. A JSON array of query predicates, in prefix form. (The standard ["<OPERATOR>", "<FIELD>", "<VALUE>"] format.)

    Response
     [
      {
        "end-time": "2012-10-29T18:38:01.000Z",
        "puppet-version": "3.0.1",
        "receive-time": "2012-10-29T18:38:04.238Z",
        "configuration-version": "1351535883",
        "start-time": "2012-10-29T18:38:00.000Z",
        "hash": "bd899b1ee825ec1d2c671fe5541b5c8f4a783472",
        "certname": "foo.local",
        "report-format": 4,
        "transaction-uuid": "030c1717-f175-4644-b048-ac9ea328f221"
        },
      {
        "end-time": "2012-10-26T22:39:32.000Z",
        "puppet-version": "3.0.1",
        "receive-time": "2012-10-26T22:39:35.305Z",
        "configuration-version": "1351291174",
        "start-time": "2012-10-26T22:39:31.000Z",
        "hash": "cd4e5fd8846bac26d15d151664a40e0f2fa600b0",
        "certname": "foo.local",
        "report-format": 4,
        "transaction-uuid": null
        }
    ]
    """
    return utils._make_api_request(api_url, '/reports', verify, cert, params={'query': query})
