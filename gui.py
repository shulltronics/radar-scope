from unigui import UniGui, PygameDisplay
from unigui import Widget, TextWidget, Solarized
import adafruit_imageload
import displayio

# Global properties of our GUI
WIDTH = 800
HEIGHT = 800
SCALE_FACTOR = 1
CS = Solarized.dark

# Create the display
display = PygameDisplay(WIDTH*SCALE_FACTOR, HEIGHT*SCALE_FACTOR)

# Create the GUI
gui = UniGui(WIDTH, HEIGHT, scale=SCALE_FACTOR, colorscheme=CS)

class ImageWidget(Widget):
    """
    A widget that loads and displays a bmp image
    """
    def __init__(self):
        image, pal = adafruit_imageload.load(
            "assets/image.bmp",
            bitmap=displayio.Bitmap,
            palette=displayio.Palette,
        )
        super().__init__("image", 0, 0, image.width, image.height, colorscheme=CS)
        print("palette length: ", pal.__len__())
        self.tg = displayio.TileGrid(
            image,
            pixel_shader=pal,
            width=1,
            height=1,
            tile_width=800,
            tile_height=800,
        )
        self.append(self.tg)

i = ImageWidget()
gui.add_widget(i)

# Create our widgets
tw = TextWidget("text", 0, 0, WIDTH, HEIGHT, colorscheme=CS, font_path=TextWidget.LARGE_FONT)
tw.set_bg_transparent(True)
tw.set_value("hello from radar app", h_justification="center", v_justification="top")
gui.add_widget(tw)

gui.update(display)