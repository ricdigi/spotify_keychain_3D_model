import utils


URL = "https://www.spotifycodes.com/downloadCode.php?uri=jpeg%2F000000%2Fwhite%2F640%2Fspotify%3Aalbum%3A4m2880jivSbbyEGAKfITCa"

if __name__ == '__main__':

    share_link = input("Enter link of song, album, artist or user: ")

    data = utils.get_link_data(share_link)

    share_link.rstrip()

    print(data)

"""
    if share_link.lstrip("https: // open.spotify.com /").startswith("track"

    https: // open.spotify.com / track / 0
    oks4FnzhNp5QPTZtoet7c?si = dc6855b6efa54ca0

    https: // open.spotify.com / album / 4
    m2880jivSbbyEGAKfITCa?si = 1_6
    htsJURnyVXujlsCiGYw
    """