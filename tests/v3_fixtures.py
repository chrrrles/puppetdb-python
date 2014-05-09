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
        '/fact-names': [
            "_timestamp", "architecture", "bios_release_date", "bios_vendor", "bios_version", "blockdevice_sda_model", "blockdevice_sda_size", "blockdevice_sda_vendor", "blockdevice_sr0_model", "blockdevice_sr0_size", "blockdevice_sr0_vendor", "blockdevices", "boardmanufacturer", "boardproductname", "boardserialnumber", "clientcert", "clientnoop", "clientversion", "domain", "facterversion", "filesystems", "fqdn", "hardwareisa", "hardwaremodel", "hostname", "id", "interfaces", "ipaddress", "ipaddress_eth0", "ipaddress_eth1", "ipaddress_lo", "is_pe", "is_virtual", "kernel", "kernelmajversion", "kernelrelease", "kernelversion", "lsbdistcodename", "lsbdistdescription", "lsbdistid", "lsbdistrelease", "lsbmajdistrelease", "macaddress", "macaddress_eth0", "macaddress_eth1", "manufacturer", "memoryfree", "memoryfree_mb", "memorysize", "memorysize_mb", "mtu_eth0", "mtu_eth1", "mtu_lo", "netmask", "netmask_eth0", "netmask_eth1", "netmask_lo", "network_eth0", "network_eth1", "network_lo", "operatingsystem", "operatingsystemmajrelease", "operatingsystemrelease", "osfamily", "path", "physicalprocessorcount", "processor0", "processorcount", "productname", "ps", "puppet_vardir", "puppetversion", "root_home", "rubysitedir", "rubyversion", "selinux", "serialnumber", "sshdsakey", "sshecdsakey", "sshfp_dsa", "sshfp_ecdsa", "sshfp_rsa", "sshrsakey", "swapfree", "swapfree_mb", "swapsize", "swapsize_mb", "timezone", "type", "uniqueid", "uptime", "uptime_days", "uptime_hours", "uptime_seconds", "uuid", "virtual"
        ],
        '/metrics/mbeans': [
            {
              "JMImplementation:type=MBeanServerDelegate" : "/metrics/mbean/JMImplementation%3Atype%3DMBeanServerDelegate",
              "com.jolbox.bonecp:type=BoneCP" : "/metrics/mbean/com.jolbox.bonecp%3Atype%3DBoneCP",
              "com.jolbox.bonecp:type=BoneCPConfig" : "/metrics/mbean/com.jolbox.bonecp%3Atype%3DBoneCPConfig",
              "com.puppetlabs.puppetdb.command:type=global,name=discarded" : "/metrics/mbean/com.puppetlabs.puppetdb.command%3Atype%3Dglobal%2Cname%3Ddiscarded",
              "com.puppetlabs.puppetdb.command:type=global,name=fatal" : "/metrics/mbean/com.puppetlabs.puppetdb.command%3Atype%3Dglobal%2Cname%3Dfatal",
              "com.puppetlabs.puppetdb.command:type=global,name=processed" : "/metrics/mbean/com.puppetlabs.puppetdb.command%3Atype%3Dglobal%2Cname%3Dprocessed",
              "com.puppetlabs.puppetdb.command:type=global,name=processing-time" : "/metrics/mbean/com.puppetlabs.puppetdb.command%3Atype%3Dglobal%2Cname%3Dprocessing-time",
              "com.puppetlabs.puppetdb.command:type=global,name=retried" : "/metrics/mbean/com.puppetlabs.puppetdb.command%3Atype%3Dglobal%2Cname%3Dretried",
              "com.puppetlabs.puppetdb.command:type=global,name=retry-counts" : "/metrics/mbean/com.puppetlabs.puppetdb.command%3Atype%3Dglobal%2Cname%3Dretry-counts",
              "com.puppetlabs.puppetdb.command:type=global,name=seen" : "/metrics/mbean/com.puppetlabs.puppetdb.command%3Atype%3Dglobal%2Cname%3Dseen",
              "com.puppetlabs.puppetdb.http.server:type=/v2,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv2%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v2,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv2%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v2/facts,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv2%2Ffacts%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v2/facts,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv2%2Ffacts%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v2/facts/puppetmaster.local,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv2%2Ffacts%2Fpuppetmaster.local%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v2/facts/puppetmaster.local,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv2%2Ffacts%2Fpuppetmaster.local%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v2/version,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv2%2Fversion%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v2/version,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv2%2Fversion%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/catalogs,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fcatalogs%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/catalogs,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fcatalogs%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/catalogs/puppetmaster.local,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fcatalogs%2Fpuppetmaster.local%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/catalogs/puppetmaster.local,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fcatalogs%2Fpuppetmaster.local%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/fact-names,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffact-names%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/fact-names,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffact-names%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts/custom_stage,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Fcustom_stage%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts/custom_stage,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Fcustom_stage%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts/puppetmaster.local,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Fpuppetmaster.local%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts/puppetmaster.local,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Fpuppetmaster.local%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts/state,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Fstate%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts/state,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Fstate%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts/uuid,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Fuuid%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/facts/uuid,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Ffacts%2Fuuid%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics/mbean,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Fmbean%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics/mbean,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Fmbean%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics/mbean,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Fmbean%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics/mbean/java.lang_type_Memory,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Fmbean%2Fjava.lang_type_Memory%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics/mbean/java.lang_type_Memory,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Fmbean%2Fjava.lang_type_Memory%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics/mbeans,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Fmbeans%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/metrics/mbeans,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fmetrics%2Fmbeans%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/facts,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Ffacts%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/facts,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Ffacts%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/facts/operatingsystem,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Ffacts%2Foperatingsystem%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/facts/operatingsystem,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Ffacts%2Foperatingsystem%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/User,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2FUser%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/User,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2FUser%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/bootsrap,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Fbootsrap%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/bootsrap,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Fbootsrap%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/bootstrap,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Fbootstrap%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/bootstrap,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Fbootstrap%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/certname,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Fcertname%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/certname,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Fcertname%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/ntp,name=404" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Fntp%2Cname%3D404",
              "com.puppetlabs.puppetdb.http.server:type=/v3/nodes/puppetmaster.local/resouces/ntp,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fnodes%2Fpuppetmaster.local%2Fresouces%2Fntp%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/server-time,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fserver-time%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/server-time,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fserver-time%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v3/version,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fversion%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v3/version,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv3%2Fversion%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v4,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv4%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v4,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv4%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.http.server:type=/v4/version,name=200" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv4%2Fversion%2Cname%3D200",
              "com.puppetlabs.puppetdb.http.server:type=/v4/version,name=service-time" : "/metrics/mbean/com.puppetlabs.puppetdb.http.server%3Atype%3D%2Fv4%2Fversion%2Cname%3Dservice-time",
              "com.puppetlabs.puppetdb.query.population:type=default,name=avg-resources-per-node" : "/metrics/mbean/com.puppetlabs.puppetdb.query.population%3Atype%3Ddefault%2Cname%3Davg-resources-per-node",
              "com.puppetlabs.puppetdb.query.population:type=default,name=num-nodes" : "/metrics/mbean/com.puppetlabs.puppetdb.query.population%3Atype%3Ddefault%2Cname%3Dnum-nodes",
              "com.puppetlabs.puppetdb.query.population:type=default,name=num-resources" : "/metrics/mbean/com.puppetlabs.puppetdb.query.population%3Atype%3Ddefault%2Cname%3Dnum-resources",
              "com.puppetlabs.puppetdb.query.population:type=default,name=pct-resource-dupes" : "/metrics/mbean/com.puppetlabs.puppetdb.query.population%3Atype%3Ddefault%2Cname%3Dpct-resource-dupes",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=add-edges" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dadd-edges",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=add-resources" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dadd-resources",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=catalog-hash" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dcatalog-hash",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=catalog-hash-match-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dcatalog-hash-match-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=catalog-hash-miss-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dcatalog-hash-miss-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=catalog-volitilty" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dcatalog-volitilty",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=duplicate-catalogs" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dduplicate-catalogs",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=duplicate-pct" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dduplicate-pct",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=gc-catalogs-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dgc-catalogs-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=gc-environments-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dgc-environments-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=gc-params-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dgc-params-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=gc-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dgc-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=new-catalog-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dnew-catalog-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=new-catalogs" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dnew-catalogs",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=replace-catalog-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dreplace-catalog-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=replace-facts-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dreplace-facts-time",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=resource-hashes" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dresource-hashes",
              "com.puppetlabs.puppetdb.scf.storage:type=default,name=store-report-time" : "/metrics/mbean/com.puppetlabs.puppetdb.scf.storage%3Atype%3Ddefault%2Cname%3Dstore-report-time",
              "com.sun.management:type=HotSpotDiagnostic" : "/metrics/mbean/com.sun.management%3Atype%3DHotSpotDiagnostic",
              "java.lang:type=ClassLoading" : "/metrics/mbean/java.lang%3Atype%3DClassLoading",
              "java.lang:type=Compilation" : "/metrics/mbean/java.lang%3Atype%3DCompilation",
              "java.lang:type=GarbageCollector,name=Copy" : "/metrics/mbean/java.lang%3Atype%3DGarbageCollector%2Cname%3DCopy",
              "java.lang:type=GarbageCollector,name=MarkSweepCompact" : "/metrics/mbean/java.lang%3Atype%3DGarbageCollector%2Cname%3DMarkSweepCompact",
              "java.lang:type=Memory" : "/metrics/mbean/java.lang%3Atype%3DMemory",
              "java.lang:type=MemoryManager,name=CodeCacheManager" : "/metrics/mbean/java.lang%3Atype%3DMemoryManager%2Cname%3DCodeCacheManager",
              "java.lang:type=MemoryPool,name=Code Cache" : "/metrics/mbean/java.lang%3Atype%3DMemoryPool%2Cname%3DCode+Cache",
              "java.lang:type=MemoryPool,name=Eden Space" : "/metrics/mbean/java.lang%3Atype%3DMemoryPool%2Cname%3DEden+Space",
              "java.lang:type=MemoryPool,name=Perm Gen" : "/metrics/mbean/java.lang%3Atype%3DMemoryPool%2Cname%3DPerm+Gen",
              "java.lang:type=MemoryPool,name=Survivor Space" : "/metrics/mbean/java.lang%3Atype%3DMemoryPool%2Cname%3DSurvivor+Space",
              "java.lang:type=MemoryPool,name=Tenured Gen" : "/metrics/mbean/java.lang%3Atype%3DMemoryPool%2Cname%3DTenured+Gen",
              "java.lang:type=OperatingSystem" : "/metrics/mbean/java.lang%3Atype%3DOperatingSystem",
              "java.lang:type=Runtime" : "/metrics/mbean/java.lang%3Atype%3DRuntime",
              "java.lang:type=Threading" : "/metrics/mbean/java.lang%3Atype%3DThreading",
              "java.nio:type=BufferPool,name=direct" : "/metrics/mbean/java.nio%3Atype%3DBufferPool%2Cname%3Ddirect",
              "java.nio:type=BufferPool,name=mapped" : "/metrics/mbean/java.nio%3Atype%3DBufferPool%2Cname%3Dmapped",
              "java.util.logging:type=Logging" : "/metrics/mbean/java.util.logging%3Atype%3DLogging",
              "org.apache.activemq:BrokerName=localhost,Type=Broker" : "/metrics/mbean/org.apache.activemq%3ABrokerName%3Dlocalhost%2CType%3DBroker",
              "org.apache.activemq:BrokerName=localhost,Type=Queue,Destination=com.puppetlabs.puppetdb.commands" : "/metrics/mbean/org.apache.activemq%3ABrokerName%3Dlocalhost%2CType%3DQueue%2CDestination%3Dcom.puppetlabs.puppetdb.commands",
              "org.apache.activemq:BrokerName=localhost,Type=Subscription,persistentMode=Non-Durable,destinationType=Queue,destinationName=com.puppetlabs.puppetdb.commands,clientId=ID_puppetmaster-48675-1399427318538-4_1,consumerId=ID_puppetmaster-48675-1399427318538-5_1_1_1" : "/metrics/mbean/org.apache.activemq%3ABrokerName%3Dlocalhost%2CType%3DSubscription%2CpersistentMode%3DNon-Durable%2CdestinationType%3DQueue%2CdestinationName%3Dcom.puppetlabs.puppetdb.commands%2CclientId%3DID_puppetmaster-48675-1399427318538-4_1%2CconsumerId%3DID_puppetmaster-48675-1399427318538-5_1_1_1",
              "org.apache.activemq:BrokerName=localhost,Type=Subscription,persistentMode=Non-Durable,destinationType=Topic,destinationName=ActiveMQ.Advisory.TempQueue_ActiveMQ.Advisory.TempTopic,clientId=ID_puppetmaster-48675-1399427318538-4_1,consumerId=ID_puppetmaster-48675-1399427318538-5_1_-1_1" : "/metrics/mbean/org.apache.activemq%3ABrokerName%3Dlocalhost%2CType%3DSubscription%2CpersistentMode%3DNon-Durable%2CdestinationType%3DTopic%2CdestinationName%3DActiveMQ.Advisory.TempQueue_ActiveMQ.Advisory.TempTopic%2CclientId%3DID_puppetmaster-48675-1399427318538-4_1%2CconsumerId%3DID_puppetmaster-48675-1399427318538-5_1_-1_1",
              "org.apache.activemq:BrokerName=localhost,Type=Topic,Destination=ActiveMQ.Advisory.Connection" : "/metrics/mbean/org.apache.activemq%3ABrokerName%3Dlocalhost%2CType%3DTopic%2CDestination%3DActiveMQ.Advisory.Connection",
              "org.apache.activemq:BrokerName=localhost,Type=Topic,Destination=ActiveMQ.Advisory.Consumer.Queue.com.puppetlabs.puppetdb.commands" : "/metrics/mbean/org.apache.activemq%3ABrokerName%3Dlocalhost%2CType%3DTopic%2CDestination%3DActiveMQ.Advisory.Consumer.Queue.com.puppetlabs.puppetdb.commands",
              "org.apache.activemq:BrokerName=localhost,Type=Topic,Destination=ActiveMQ.Advisory.Queue" : "/metrics/mbean/org.apache.activemq%3ABrokerName%3Dlocalhost%2CType%3DTopic%2CDestination%3DActiveMQ.Advisory.Queue",
              "org.apache.activemq:BrokerName=localhost,Type=jobScheduler,jobSchedulerName=JMS" : "/metrics/mbean/org.apache.activemq%3ABrokerName%3Dlocalhost%2CType%3DjobScheduler%2CjobSchedulerName%3DJMS"
            }
        ],
        '/metrics/mbean/JMImplementation%3Atype%3DMBeanServerDelegate': [
            {
              "MBeanServerId" : "puppetmaster_1399427297187",
              "SpecificationName" : "Java Management Extensions",
              "SpecificationVersion" : "1.4",
              "SpecificationVendor" : "Oracle Corporation",
              "ImplementationName" : "JMX",
              "ImplementationVersion" : "1.7.0_55-b14",
              "ImplementationVendor" : "Oracle Corporation"
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