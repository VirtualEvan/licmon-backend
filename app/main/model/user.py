class Product:
    """ Feature Model for storing feature related details """

    def __init__(self, username, hostname, display, version, server, port, handle, checkout):
            self.username = username
            self.hostname = hostname
            self.display = display
            self.version = version
            self.server = server
            self.port = port
            self.handle = handle
            self.checkout = checkout

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        self._hostname = hostname

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, display):
        self._display = display

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, server):
        self._server = server

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def handle(self):
        return self._handle

    @handle.setter
    def handle(self, handle):
        self._handle = handle

    @property
    def checkout(self):
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        self._checkout = checkout

    def __repr__(self):
        return f"<Product '{self.name}'>"