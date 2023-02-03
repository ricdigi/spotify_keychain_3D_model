def get_link_data(link):
    """
    Returns a tuple (type, URI) parsed from the input link.
    The type may be "track", "album", "artist" or "user".
    """
    end_of_uri = link.rfind('?')
    return tuple(link[:end_of_uri].split('/')[3:])


def generate_bars(bar_heights, model):
    """
    Given a set of bar heights, the function create the 3D code
    on the top face of the base model .
    """
    curr_bar = 0

    for bar in bar_heights:
        model = (
           model.pushPoints([(15 + curr_bar * 1.8, 7.5)])
           .sketch()
           .slot(9/5 * bar, 1, 90)
           .finalize()
           .extrude(4)
        )
        curr_bar += 1

    return model

