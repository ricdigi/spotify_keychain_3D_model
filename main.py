import cadquery as cq
import requests
import io
from PIL import Image
import utils

URL = "https://www.spotifycodes.com/downloadCode.php?uri=jpeg%2F000000%2Fwhite%2F640%2Fspotify%3Aalbum%3A4m2880jivSbbyEGAKfITCa"

if __name__ == '__main__':

    # –––––––––––––––––––––––––––––––––––––––
    # –––– GETTING INPUT URL AND PARSING ––––
    # –––––––––––––––––––––––––––––––––––––––
    share_link = input("Enter link of song, album, artist or playlist: ")

    data = utils.get_link_data(share_link)

    if len(data) != 2:
        print("Something went wrong while parsing the URL.")
        exit(-1)


    # ––––––––––––––––––––––––––––––––––––––
    # –––––– DOWNLOADING SPOTIFY CODE ––––––
    # ––––––––––––––––––––––––––––––––––––––
    code_URL = "https://www.spotifycodes.com/downloadCode.php?uri=jpeg%2F000000%2Fwhite%2F640%2Fspotify%3A" + data[0] + "%3A" + data[1]

    r = requests.get(code_URL)

    if not r.ok or not r.content:
        print("Something went wrong while fetching the Spotify code.")
        exit(-1)


    # ––––––––––––––––––––––––––––––––––––––
    # ––––––– LOADING THE CODE IMAGE –––––––
    # ––––––––––––––––––––––––––––––––––––––
    img = Image.open(io.BytesIO(r.content)).crop((160,0, 640-31, 160))
    width, height = img.size

    pix = img.load()


    # –––––––––––––––––––––––––––––––––––––
    # –––––––– GETTING BAR LENGTHS ––––––––
    # –––––––––––––––––––––––––––––––––––––
    bar_heights = []
    max_height_of_single_bar = 0

    for x in range(width):

        at_bar = False
        curr_height = 0

        for y in range(height):
            if pix[x,y][0] > 20 or pix[x,y][1] > 20 or pix[x,y][2] > 20:
                at_bar = True
                curr_height += 1

        if at_bar and curr_height > max_height_of_single_bar:
            max_height_of_single_bar = curr_height/20
        elif not at_bar and max_height_of_single_bar > 0:
            bar_heights.append(max_height_of_single_bar)
            max_height_of_single_bar = 0

    print(f"There are {len(bar_heights)} bars of heights {bar_heights}")


    # ––––––––––––––––––––––––––––––––––––
    # –––––– EDITING THE BASE MODEL ––––––
    # ––––––––––––––––––––––––––––––––––––
    model = cq.importers.importStep('base_model.step')

    curr_bar = 0

    for bar in bar_heights:
        model = (
            model.pushPoints([(15.5 + curr_bar * 1.88, 7.5)])
            .sketch()
            .slot(9 / 5 * bar, 1, 90)
            .finalize()
            .extrude(4)
        )
        curr_bar += 1

    cq.exporters.export(model, 'model.stl')

