__license__ = """
Copyright 2013 Parse.ly, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import logging
import mock
import unittest

from kazoo.client import KazooClient
from nose.plugins.attrib import attr

logger = logging.getLogger(__name__)

@attr('fixme')
class TestCluster(unittest.TestCase):
    """Test the methods of :class:`samsa.cluster.Cluster`."""

    def test_non_connected_zk(self, *args):
        """Test we throw an exception when ZK isn't connected yet"""
        client = KazooClient()
        self.assertRaises(Exception, lambda: Cluster(client))

if __name__ == '__main__':
    unittest.main()