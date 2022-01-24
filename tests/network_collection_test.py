import unittest
from ro_interview_assignment.data_structures.network_collection import NetworkCollection


class TestRemoveInvalidCluster(unittest.TestCase):

    def setUp(self):
        self.network_collection = NetworkCollection("255.255.255.255", [])

    def test_invalid_records(self):

        data = {'192.168.0.0/24': [{'address': '192.168.0.1', 'available': True, 'last_used': '30/01/20 17:00:00'},
                                   {'address': '192.168..0.3', 'available': True, 'last_used': '30/01/20 17:00:00'}],
                '192.168.11.0/24': [{'address': '192.168.11.1', 'available': True, 'last_used': '30/01/20 17:00:00'},
                                    {'address': '192.168.2.1', 'available': False, 'last_used': '30/01/20 17:00:00'}]
                }

        expected = {'192.168.0.0/24': [{'address': '192.168.0.1', 'available': True, 'last_used': '30/01/20 17:00:00'}],
                    '192.168.11.0/24': [{'address': '192.168.11.1', 'available': True, 'last_used': '30/01/20 17:00:00'}],
                    }
        actual = {}

        self.network_collection = [NetworkCollection(key, value) for key, value in data.items()]
        for elem in self.network_collection:
            elem.remove_invalid_records()
        for elem in self.network_collection:
            actual[elem.ipv4_network] = elem.entries
        self.assertEqual(actual, expected)

    #def tearDown(self) -> None:

