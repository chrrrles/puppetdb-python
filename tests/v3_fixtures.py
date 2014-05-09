#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""v3_fixtures.py: These are fixture functions for returning PuppetDB data."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"
__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"


def v3():
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
         '/version': [
            {
                "version" : "2.0.0",
            }
        ],
         '/server-time': [
            {
                "server-time" : "2014-05-09T03:36:14.958Z"
            }
        ],
        '/catalogs/host1': [
            {
                "metadata": {
                    "api_version": 1
                },
                "data": {
                    "transaction-uuid": "a9f466d1-6057-4ae3-9ed8-ea8d8c558ff3",
                    "version": "1399421807",
                    "name": "host1",
                    "resources": [
                        {
                            "tags": [ "default", "node", "begin", "ntp", "bootstrap", "anchor", "class", "ntp::begin"],
                            "file": "/etc/puppet/modules/ntp/manifests/init.pp",
                            "type": "Anchor",
                            "title": "ntp::begin",
                            "line": 50,
                            "parameters": {
                                "before": "Class[Ntp::Install]"
                            },
                            "exported": False
                        }
                    ],
                    "edges": [
                        {
                            "source": {
                                "type": "Class",
                                "title": "main"
                            },
                            "target": {
                                "type": "Filebucket",
                                "title": "main"
                            },
                            "relationship": "contains"
                        }
                    ]
                }
            }
        ]
    }