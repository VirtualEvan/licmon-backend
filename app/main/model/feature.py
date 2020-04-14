class Feature:
    """ Feature Model for storing feature related details """

    # TODO:  Too many arguments
    def __init__(self, 
        name,
        version = None,
        vendor = None,
        licenses_issued = None,
        licenses_in_use = None,
        message = None
    ):
        self.name = name
        self.version = version
        self.vendor = vendor
        self.licenses_issued = licenses_issued
        self.licenses_in_use = licenses_in_use
        self.users = []
        self.message = message

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        self._vendor = vendor

    @property
    def licenses_issued(self):
        return self._licenses_issued

    @licenses_issued.setter
    def licenses_issued(self, licenses_issued):
        self._licenses_issued = licenses_issued

    @property
    def licenses_in_use(self):
        return self._licenses_in_use

    @licenses_in_use.setter
    def licenses_in_use(self, licenses_in_use):
        self._licenses_in_use = licenses_in_use

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users):
        self._users = users

    # TODO: Put message as property? Mutually exclusive...
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    def add_user(self, user):
        return self._users.append(user)

    def __repr__(self):
        return f"<Product '{self.name}'>"