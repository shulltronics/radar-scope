from gui import display, gui, tw, i
import time
import requests
# import gzip
from PIL import Image
import cairosvg
from io import BytesIO

print("Starting Radar App...")

# path = "assets\KJAX_L3_BDHC_20220502_184030.tif"

# # Open image in palette mode
# image = Image.open(path).convert(mode="P", palette=Image.Palette.ADAPTIVE, colors=8)
# print(image.getpalette()[0:3*8])
# print("image size: ", image.width, image.height)
# image = image.resize((800, 800))
# image.save("assets/image.bmp", "BMP")

# url0 = "https://mrms.ncep.noaa.gov/data/RIDGEII/L3/KJAX/BDHC/KJAX_L3_BDHC_20220502_183803.tif.gz"
# url1 = "https://mrms.ncep.noaa.gov/data/RIDGEII/L3/KJAX/BDHC/KJAX_L3_BDHC_20220502_184030.tif.gz"
# url2 = "https://mrms.ncep.noaa.gov/data/RIDGEII/L3/KJAX/BDHC/KJAX_L3_BDHC_20220502_184323.tif.gz"
# url3 = "https://mrms.ncep.noaa.gov/data/RIDGEII/L3/KJAX/BDHC/KJAX_L3_BDHC_20220502_184544.tif.gz"
# r = requests.get(url0)
# print("Status code: ", r.status_code)

# print("Parsing SVG to BMP...")
# svg_stream = BytesIO()
# cairosvg.svg2png(url="assets/florida.svg", write_to=svg_stream)
# map = Image.open(svg_stream).convert(mode="P", palette=Image.Palette.ADAPTIVE, colors=8)
# print("map image is size:(", map.width, ",", map.height, ")")
# # TODO: make a function from this:
# x0 = 0
# y0 = 0
# x1 = 800
# y1 = 800
# map = map.crop((x0, y0, x1, y1))
# print(map.getpalette()[0:3*8])
# print("map size: ", map.width, map.height)
# map.save("assets/florida.bmp", "BMP")

start = time.time()
dt = 0.3
while True:
    t = time.time()
    if t - start > dt:
        # This code runs ever dt seconds
        display.refresh()
        click = display.get_mouse_clicks()
        if click is not None:
            print(gui.__len__())
        print("click: " + str(click))
        print("elapsed")
        i.increment_image()
        tw.set_value(str(i.current_tg_index), h_justification="center", v_justification="top")
        start = t
    time.sleep(0.2)