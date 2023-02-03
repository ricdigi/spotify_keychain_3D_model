import numpy as np
import cadquery as cq
import utils
import requests
from PIL import Image

URL = "https://www.spotifycodes.com/downloadCode.php?uri=jpeg%2F000000%2Fwhite%2F640%2Fspotify%3Aalbum%3A4m2880jivSbbyEGAKfITCa"

if __name__ == '__main__':

    share_link = input("Enter link of song, album, artist or user: ")

    data = utils.get_link_data(share_link)

    if len(data) != 2:
        print("Something went wrong. Probably your fault.")
        exit(-1)

    code_URL = "https://www.spotifycodes.com/downloadCode.php?uri=jpeg%2F000000%2Fwhite%2F640%2Fspotify%3A" + data[0] + "%3A" + data[1]

    r = requests.get(code_URL)

    if not r.ok or not r.content:
        print("Something went wrong. Probably your fault.")
        exit(-1)

    #img = Image.open(io.BytesIO(r.content))

    with open(data[1]+".png", "wb") as fp:
        fp.write(r.content)

    img = Image.open(data[1]+".png").crop((160,0, 640-31, 160))
    width, height = img.size

    pix = img.load()

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
            max_height_of_single_bar = np.round_(curr_height/20)
        elif not at_bar and max_height_of_single_bar > 0:
            bar_heights.append(max_height_of_single_bar)
            max_height_of_single_bar = 0

    print(f"There are {len(bar_heights)} bars of heights {bar_heights}")

    base_model = cq.importers.importStep('base_model.step')
    face = utils.generate_bars(bar_heights, base_model)
    cq.exporters.export(face, 'model.stl')

