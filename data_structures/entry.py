from datetime import datetime

class Entry:

    def __init__(self, address, available, last_used):

        self.address = str(address)
        self.available = bool(available)
        self.last_used = datetime(last_used)

        """
        define new method to chanke gey argument of sorted and call it with self.new-method in comstructor body
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        pass
