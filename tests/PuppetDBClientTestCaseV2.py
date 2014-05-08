#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PuppetDBClientTestCaseV2.py: A bunch of unittests for testing this module."""

__author__ = "monkee"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"


import unittest
from mock import MagicMock, patch
import requests
from puppetdb.core import PuppetDBClient
import json
import helpers


class PuppetDBClientTestCaseV2(unittest.TestCase):
    def setUp(self):
        self._client = PuppetDBClient(api_version='v2')

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

