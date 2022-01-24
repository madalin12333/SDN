import unittest

# import test modules
import cluster_test
import datacenter_test
import entry_test
import network_collection_test

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(cluster_test))
suite.addTests(loader.loadTestsFromModule(datacenter_test))
suite.addTests(loader.loadTestsFromModule(entry_test))
suite.addTests(loader.loadTestsFromModule(network_collection_test))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)