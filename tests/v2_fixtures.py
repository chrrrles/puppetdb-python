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

"""v2_fixtures.py: These are fixture functions for returning PuppetDB data."""

__author__ = "monkee"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"


def v2():
    return {
        '/nodes': [
            {
                'name': 'host1',
                'deactivated': None,
                'catalog_timestamp': '2013-02-09T21:05:15.663Z',
                'facts_timestamp': '2013-02-09T21:05:15.663Z',
                'report_timestamp': None
            },
            {
                'name': 'host2',
                'deactivated': None,
                'catalog_timestamp': '2013-02-09T21:05:15.663Z',
                'facts_timestamp': '2013-02-09T21:05:15.663Z',
                'report_timestamp': None

            }
        ],
        '/nodes/host1': {
            'name': 'host1',
            'deactivated': None,
            'catalog_timestamp': '2013-02-09T21:05:15.663Z',
            'facts_timestamp': '2013-02-09T21:05:15.663Z',
            'report_timestamp': None
        },
        '/nodes/host1/facts': [
            {
                'certname': 'host1',
                'name': 'architecture',
                'value': 'amd64',
            },
            {
                'certname': 'host1',
                'name': 'domain',
                'value': 'local',
            },
            {
                'certname': 'host1',
                'name': 'ipaddress',
                'value': '1.2.3.4',
            }
        ],
        '/nodes/host1/facts/architecture': [
            {
                'certname': 'host1',
                'name': 'architecture',
                'value': 'amd64',
            }
        ],
        '/nodes/host1/resources': [
            {
                'certname': 'host1',
                'parameters': {
                    'ensure': 'installed',
                },
                'type': 'Class',
                'sourceline': 7,
                'sourcefile': '/etc/foo/bar.pp',
                'exported': False,
                'resource': '1234567890',
            },
        ],
        '/nodes/host1/resources/Class': [
            {
                'certname': 'host1',
                'parameters': {
                    'ensure': 'installed',
                },
                'type': 'Class',
                'sourceline': 7,
                'sourcefile': '/etc/foo/bar.pp',
                'exported': False,
                'resource': '1234567890',
            },
        ],
        '/facts': [
            {
                'certname': 'host1',
                'name': 'puppetversion',
                'value': '3.2.2',
            },
            {
                'certname': 'host2',
                'name': 'puppetversion',
                'value': '2.7.10',
            }
        ],
        '/facts/ipaddress': [
            {
                'certname': 'host1',
                'name': 'ipaddress',
                'value': '10.10.10.11',
            },
            {
                'certname': 'host2',
                'name': 'ipaddress',
                'value': '10.10.10.12',
            }
        ],
        '/facts/kernelversion/3.2.34': [
            {
                'certname': 'host1',
                'name': 'kernelversion',
                'value': '3.2.34',
            }
        ],
    }
