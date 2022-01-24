import unittest
from data_structures.datacenter import Datacenter


class TestRemoveInvalidCluster(unittest.TestCase):

    def setUp(self):
        self.datacenter_instance = Datacenter("", {})

    def test_invalid_format(self):

        data = {"Moscow": {"MOS-1": {}, "MOS-12": {}, "MO-3421": {}, "MOB--23": {}},
                "Barcelona": {"BAR-1221": {}, "BA-21": {}, "BAR-12": {}}
                }

        expected = {'Moscow': ['MOS-1', 'MOS-12'],
                    'Barcelona': ['BAR-12']}
        actual = {}

        self.datacenter_instance = [Datacenter(key, value) for key, value in data.items()]
        for elem in self.datacenter_instance:
            elem.remove_invalid_clusters()
        for elem in self.datacenter_instance:
            actual[elem.name] = elem.cluster_dict
        self.assertEqual(actual, expected)

    #def tearDown(self) -> None:
