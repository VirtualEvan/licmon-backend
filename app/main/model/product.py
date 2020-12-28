class Product:
    """ Prduct Model for storing product related details """

    def __init__(self, name):
        self.name = name
        self.features = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, features):
        self._features = features

    def add_feature(self, feature):
        return self._features.append(feature)

    def __repr__(self):
        return f"<Product '{self.name}'>"
