class Cluster:
    def __init__(self, name, network_dict, security_level):

        self.name = str(name)
        self.network_dict = int(network_dict)
        self.security_level = list(security_level)

        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        pass
