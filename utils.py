def get_link_data(link):
    """
    Returns a tuple (type, URI) parsed from the input link.
    The type may be "track", "album", "artist" or "user".
    """
    end_of_uri = link.rfind('?')
    return tuple(link[:end_of_uri].split('/')[3:])