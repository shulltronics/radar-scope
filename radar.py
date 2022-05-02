from gui import display, gui, tw
import requests
import gzip
from PIL import Image

print("Starting Radar App...")

path = "assets\KJAX_L3_BDHC_20220502_183513.tif"

# Open image in palette mode
image = Image.open(path).convert(mode="P", palette=Image.Palette.ADAPTIVE, colors=8)
print(image.getpalette()[0:3*8])
print("image size: ", image.width, image.height)
image = image.resize((800, 800))
image.save("assets/image.bmp", "BMP")

url0 = "https://mrms.ncep.noaa.gov/data/RIDGEII/L3/KJAX/BDHC/KJAX_L3_BDHC_20220502_183803.tif.gz"
url1 = "https://mrms.ncep.noaa.gov/data/RIDGEII/L3/KJAX/BDHC/KJAX_L3_BDHC_20220502_184030.tif.gz"
url2 = "https://mrms.ncep.noaa.gov/data/RIDGEII/L3/KJAX/BDHC/KJAX_L3_BDHC_20220502_184323.tif.gz"
url3 = "https://mrms.ncep.noaa.gov/data/RIDGEII/L3/KJAX/BDHC/KJAX_L3_BDHC_20220502_184544.tif.gz"
r = requests.get(url0)
print("Status code: ", r.status_code)

while True:
    display.refresh()
    click = display.get_mouse_clicks()
    if click is not None:
        print(gui.__len__())
        print("click: " + str(click))
        tw.set_value("poop")
        