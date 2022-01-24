from ipaddress import IPv4Network, IPv4Address
import re

class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):

        #self.ipv4_network = IPv4Network(ipv4_network) #each network
        self.ipv4_network = str(ipv4_network) 
        self.entries = list(raw_entry_list) 
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        pass

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        pattern = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        self.entries = [ elem for elem in self.entries if re.match(pattern, elem['address']) ]
        self.entries = [ elem for elem in self.entries if IPv4Address(elem['address']) in IPv4Network(self.ipv4_network) ]

        pass

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
