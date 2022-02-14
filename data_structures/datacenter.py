import re

class Datacenter:
    
    def __init__(self, name, cluster_dict):

         """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
            
        self.name = str(name)
        self.cluster_dict = list(cluster_dict)

    def remove_invalid_clusters(self):

        
        """
        Removes invalid objects from the clusters list.
        """
        
        pattern = r"\b" + re.escape(self.name[:3].upper()) + r"-[0-9]{1,3}\b"
        self.cluster_dict = [ elem for elem in self.cluster_dict if re.match(pattern, elem) ]
       
