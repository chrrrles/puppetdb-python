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

"""PuppetDBClientTestCaseV3.py: A bunch of unittests for testing this module."""

__author__ = "monkee"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"


import unittest
from mock import patch
from puppetdb.core import PuppetDBClient
import helpers


class PuppetDBClientTestCaseV3(unittest.TestCase):
    def setUp(self):
        self._client = PuppetDBClient(api_version='v3')

    def tearDown(self):
        pass

    @patch('puppetdb.utils.api_request')
    def test_get_nodes(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_nodes()
        self.assertEqual(len(resp), 2)
        node_0 = resp[0]
        self.assertTrue(node_0.has_key('name'))
        self.assertEqual(node_0.get('name'), 'host1')
        node_1 = resp[1]
        self.assertTrue(node_1.has_key('name'))
        self.assertEqual(node_1.get('name'), 'host2')

    @patch('puppetdb.utils.api_request')
    def test_get_node(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node('host1')
        self.assertTrue(resp.has_key('name'))
        self.assertEqual(resp.get('name'), 'host1')

    @patch('puppetdb.utils.api_request')
    def test_get_node_facts(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node_facts('host1')
        self.assertNotEqual(len(resp), 0)
        fact_0 = resp[0]
        self.assertTrue(fact_0.has_key('certname'))
        self.assertEqual(fact_0.get('certname'), 'host1')
        self.assertTrue(fact_0.has_key('name'))
        self.assertEqual(fact_0.get('name'), 'architecture')
        self.assertTrue(fact_0.has_key('value'))
        self.assertEqual(fact_0.get('value'), 'amd64')

    @patch('puppetdb.utils.api_request')
    def test_get_node_fact_by_name(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node_fact_by_name('host1', 'architecture')
        self.assertNotEqual(len(resp), 0)
        fact_0 = resp[0]
        self.assertTrue(fact_0.has_key('certname'))
        self.assertEqual(fact_0.get('certname'), 'host1')
        self.assertTrue(fact_0.has_key('name'))
        self.assertEqual(fact_0.get('name'), 'architecture')
        self.assertTrue(fact_0.has_key('value'))
        self.assertEqual(fact_0.get('value'), 'amd64')

    @patch('puppetdb.utils.api_request')
    def test_get_node_resources(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node_resources('host1')
        self.assertNotEqual(len(resp), 0)
        res_0 = resp[0]
        self.assertTrue(res_0.has_key('certname'))
        self.assertEqual(res_0.get('certname'), 'host1')
        self.assertTrue(res_0.has_key('parameters'))
        self.assertTrue(res_0.has_key('sourceline'))
        self.assertEqual(res_0.get('sourceline'), 7)

    @patch('puppetdb.utils.api_request')
    def test_get_node_resource_by_type(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node_resource_by_type('host1', 'Class')
        self.assertNotEqual(len(resp), 0)

    @patch('puppetdb.utils.api_request')
    def test_get_facts(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_facts(["=", "name", "architecture"])
        self.assertNotEqual(len(resp), 0)
        fact_0 = resp[0]
        self.assertTrue(fact_0.has_key('certname'))
        self.assertEqual(fact_0.get('certname'), 'host1')
        self.assertTrue(fact_0.has_key('name'))
        self.assertEqual(fact_0.get('name'), 'puppetversion')
        self.assertTrue(fact_0.has_key('value'))
        self.assertEqual(fact_0.get('value'), '3.2.2')
        fact_1 = resp[1]
        self.assertTrue(fact_1.has_key('certname'))
        self.assertEqual(fact_1.get('certname'), 'host2')
        self.assertTrue(fact_1.has_key('name'))
        self.assertEqual(fact_1.get('name'), 'puppetversion')
        self.assertTrue(fact_1.has_key('value'))
        self.assertEqual(fact_1.get('value'), '2.7.10')

    @patch('puppetdb.utils.api_request')
    def test_get_facts_by_name(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_facts_by_name('ipaddress')
        self.assertNotEqual(len(resp), 0)
        fact_0 = resp[0]
        self.assertTrue(fact_0.has_key('certname'))
        self.assertEqual(fact_0.get('certname'), 'host1')
        self.assertTrue(fact_0.has_key('name'))
        self.assertEqual(fact_0.get('name'), 'ipaddress')
        self.assertTrue(fact_0.has_key('value'))
        self.assertEqual(fact_0.get('value'), '10.10.10.11')
        fact_1 = resp[1]
        self.assertTrue(fact_1.has_key('certname'))
        self.assertEqual(fact_1.get('certname'), 'host2')
        self.assertTrue(fact_1.has_key('name'))
        self.assertEqual(fact_1.get('name'), 'ipaddress')
        self.assertTrue(fact_1.has_key('value'))
        self.assertEqual(fact_1.get('value'), '10.10.10.12')

    @patch('puppetdb.utils.api_request')
    def test_get_facts_by_name_and_value(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_facts_by_name_and_value('kernelversion', '3.2.34')
        self.assertNotEqual(len(resp), 0)
        fact_0 = resp[0]
        self.assertTrue(fact_0.has_key('certname'))
        self.assertEqual(fact_0.get('certname'), 'host1')
        self.assertTrue(fact_0.has_key('name'))
        self.assertEqual(fact_0.get('name'), 'kernelversion')
        self.assertTrue(fact_0.has_key('value'))
        self.assertEqual(fact_0.get('value'), '3.2.34')

    @patch('puppetdb.utils.api_request')
    def test_get_catalog(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_catalog('host1')
        self.assertNotEqual(len(resp), 0)
        cat_0 = resp[0]
        self.assertTrue(cat_0.has_key('metadata'))

    @patch('puppetdb.utils.api_request')
    def test_get_version(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_version()
        self.assertNotEqual(len(resp), 0)
        ver_0 = resp[0]
        self.assertTrue(ver_0.has_key('version'))
        self.assertEqual(ver_0.get('version'), '2.0.0')

    @patch('puppetdb.utils.api_request')
    def test_get_server_time(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_server_time()
        self.assertNotEqual(len(resp), 0)
        st_0 = resp[0]
        self.assertTrue(st_0.has_key('server-time'))
        self.assertEqual(st_0.get('server-time'), '2014-05-09T03:36:14.958Z')

    @patch('puppetdb.utils.api_request')
    def test_get_fact_names(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_fact_names()
        self.assertNotEqual(len(resp), 0)
        self.assertTrue('_timestamp' in resp)
        self.assertTrue('architecture' in resp)
        self.assertTrue('fqdn' in resp)
        self.assertFalse('BogusName' in resp)

    @patch('puppetdb.utils.api_request')
    def test_get_metric_names(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_metric_names()
        self.assertNotEqual(len(resp), 0)
        mn_0 = resp[0]
        self.assertTrue(mn_0.has_key('JMImplementation:type=MBeanServerDelegate'))
        self.assertEqual(mn_0.get('JMImplementation:type=MBeanServerDelegate'), '/metrics/mbean/JMImplementation%3Atype%3DMBeanServerDelegate')

    @patch('puppetdb.utils.api_request')
    def test_get_metrics_by_name(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_metrics_by_name('JMImplementation%3Atype%3DMBeanServerDelegate')
        self.assertNotEqual(len(resp), 0)
        mn_0 = resp[0]
        self.assertTrue(mn_0.has_key('MBeanServerId'))
        self.assertEqual(mn_0.get('MBeanServerId'), 'puppetmaster_1399427297187')

    @patch('puppetdb.utils.api_request')
    def test_get_reports(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_reports('["=", "certname", "puppetmaster.local"]')
        self.assertEqual(len(resp), 2)
        rep_0 = resp[0]
        self.assertTrue(rep_0.has_key('configuration-version'))
        self.assertEqual(rep_0.get('configuration-version'), '1399421807')
        self.assertTrue(rep_0.has_key('hash'))
        self.assertEqual(rep_0.get('hash'), '79b322fe816132cdbf537048a081764955fe175e')
        rep_1 = resp[1]
        self.assertTrue(rep_1.has_key('configuration-version'))
        self.assertEqual(rep_1.get('configuration-version'), '1399421807')
        self.assertTrue(rep_1.has_key('hash'))
        self.assertEqual(rep_1.get('hash'), '50008ca41657d480425eb6961b91d84889e6ce84')