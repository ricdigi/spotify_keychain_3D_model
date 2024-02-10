def get_link_data(link):
    """
    Returns a tuple (type, URI) parsed from the input link.
    The type may be "track", "album", "artist", or "playlist".
    """
    # First, remove any query parameters
    link = link.split('?')[0]

    # Next, split the URL into parts
    parts = link.split('/')

    # Check for the presence of "track", "album", "artist", or "playlist"
    for i, part in enumerate(parts):
        if part in ["track", "album", "artist", "playlist"]:
            # Check if the next part of the URL is available
            if i + 1 < len(parts):
                return (part, parts[i + 1])

    # If no match is found, return None
    return None

# Test the function with your example URL
link = "https://open.spotify.com/intl-it/track/4R1bPIiMEr5xfejy05H7cW?si=eb7468028a9d410c"
data = get_link_data(link)
print(data)
