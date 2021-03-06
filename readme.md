# puppetdb-python
Python interface to [PuppetDB](http://docs.puppetlabs.com/puppetdb/1.1/index.html)

[![Build Status](https://travis-ci.org/monk-ee/puppetdb-python.png?branch=master)](https://travis-ci.org/monk-ee/puppetdb-python)

Added Support for API versions

* v2 (Deprecated)
* v3 (This is the Default as of 6/5/2014)
* v4 (Experimental)

# Usage

* `pip install puppetdb` or `python setup.py install` (from this source)

```
>>> from puppetdb import PuppetDBClient
>>> c = PuppetDBClient()
>>> c.get_nodes()
>>> [{'deactivated': None, 'facts_timestamp': '2013-02-09T21:05:15.082Z', 'name': 'sandbox.local', {...}]

>>> c.get_node('sandbox.local')
>>> {'deactivated': None, 'facts_timestamp': '2013-02-09T21:05:15.082Z', 'name': 'sandbox.local', {...}

>>> c.get_node_facts('sandbox.local')
>>> [{'certname': 'sandbox.local', 'name': 'architecture', 'value': 'amd64'}, {...}]

>>> c.get_node_resources('sandbox.local')
>>> [{'sourcefile': '/etc/puppet/modules/arcus/manifests/package.pp', {...}]

>>> c.get_facts('["and", ["=", "name", "kernelversion"], ["=", "value", "3.2.34"]]')
>>> [{'certname': 'sandbox.local', 'name': 'kernelversion', 'value': '3.2.34'}, {...}]

>>> c.get_facts_by_name('virtual')
>>> [{'certname': 'sandbox.local', 'name': 'virtual', 'value': 'xenu'}, {...}]

>>> c.get_facts_by_name_and_value('selinux', 'true')
>>> [{'certname': 'sandbox.local', 'name': 'selinux', 'value': 'true'}, {...}]


```

For connections to a remote PuppetDB host, you have to authenticate using SSL and client certificates

```
>>> from puppetdb import PuppetDBClient
>>> c = PuppetDBClient(host="puppetdb.example.com",port=8081,use_ssl=True,verify='/var/lib/puppet/ssl/certs/ca.pem',cert=('/var/lib/puppet/ssl/certs/puppet.example.com.pem','/var/lib/puppet/ssl/private_keys/puppet.example.com.pem'))
...
```


# ToDo

* Proper paging support
* Query support

# Contributing
* `pip install -r requirements.txt`
* `./test.sh -v` (optional)
* Fork, Edit, Issue Pull Request
