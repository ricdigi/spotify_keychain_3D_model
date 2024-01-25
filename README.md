# Spotify Keychain 3D Model

This repository contains the code and 3D model files needed to create a custom Spotify keychain. This keychain is designed to incorporate a Spotify code of your favorite song, album, artist, or playlist, which can be scanned to play music directly from Spotify.

![](https://github.com/ricdigi/spotify_keychain_3D_model/blob/master/Images/render_b.png?raw=true)

## How to Use the Code

The script in this repository uses `cadquery` to modify a base 3D model of the keychain by adding a Spotify code to it. Follow these steps to use the code:

1. **Setup Python Environment**:
   - Ensure you have Python installed on your system.
   - Install required packages: `cadquery`, `requests`, `PIL` (Python Imaging Library), and `io`.
   - You can install these packages using `pip install cadquery requests pillow`.

2. **Running the Script**:
   - Open the script in your Python environment.
   - Run the script. It will prompt you to enter the link of the song, album, artist, or playlist from Spotify.

3. **Input URL Parsing**:
   - The script parses the provided Spotify link and prepares a URL to fetch the corresponding Spotify code.

4. **Downloading the Spotify Code**:
   - The script downloads the Spotify code as an image based on the parsed data.

5. **Loading the Code Image**:
   - The code image is loaded and processed to determine the bar lengths which are essential to generate the Spotify code's pattern.

6. **Editing the Base Model**:
   - The script then takes a base model of the keychain (in STEP format) and modifies it by adding the Spotify code pattern.
   - The model is updated with extrusions representing the unique barcode of your Spotify link.

7. **Exporting the Final Model**:
   - Finally, the script exports the modified model as an STL file, which can be used for 3D printing.

8. **3D Printing**:
   - Use the exported STL file to 3D print your custom Spotify keychain.

## Customization

You can customize the keychain by using different Spotify links. Each link will generate a unique code that represents the specific song, album, artist, or playlist.

