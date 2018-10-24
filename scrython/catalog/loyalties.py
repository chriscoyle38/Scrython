from .catalogs_object import CatalogsObject

class Loyalties(CatalogsObject):
    """
    catalogs/loyalties

    Catalog object for all known starting loyalties.

    Example usage:
        >>> catalog = scrython.catalog.Loyalties()
        >>> catalog.data()
    """
    def __init__(self):
        self._url = 'catalog/loyalties?'
        super(Loyalties, self).__init__(self._url)
