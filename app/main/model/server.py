class Server:
    """Server Model storing infromation of the configured license servers"""

    def __init__(self, name, port, hostnames):
        self.name = name
        self.port = port
        self.hostnames = hostnames

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def hostnames(self):
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        self._hostnames = hostnames
