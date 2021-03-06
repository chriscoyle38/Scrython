from .cards_object import CardsObject

class TCGPlayerId(CardsObject):
    """
    cards/id
    Get a card by the TCGPlayer id.

    Args:
        id (string):
            The TCGPlayer Id of the card.
        format (string, optional):
            Defaults to 'json'.
            Returns data in the specified method.
        face (string, optional):
            Defaults to empty string.
            If you're using the `image` format, this will specify if you want the front or back face.
        version (string, optional):
            Defaults to empty string.
            If you're using the `image` format, this will specify if you want the small, normal,
            large, etc version of the image.
        pretty (string, optional):
            Defaults to empty string.
            Returns a prettier version of the json object.
            Note that this may break functionality with Scrython.

    Returns:
        N/A

    Raises:
        Exception: If the 'id' parameter is not provided.
        Exception: If the object returned is an error.

    Examples:
        >>> card = scrython.cards.TCGPlayerId(id="6147")
        >>> card.name()
    """
    def __init__(self, **kwargs):
        if kwargs.get('id') is None:
            raise Exception('No id provided to search by')

        self.url = 'cards/tcgplayer/{}?'.format(str(kwargs.get('id')))
        super(TCGPlayerId, self).__init__(self.url)
