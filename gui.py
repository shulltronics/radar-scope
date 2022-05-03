from re import I
from unigui import UniGui, PygameDisplay
from unigui import Widget, TextWidget, Solarized, VSCode
import adafruit_imageload
import displayio

# Global properties of our GUI
WIDTH = 800
HEIGHT = 800
SCALE_FACTOR = 2
CS = VSCode.dark

# Create the display
display = PygameDisplay(WIDTH*SCALE_FACTOR, HEIGHT*SCALE_FACTOR)

# Create the GUI
gui = UniGui(WIDTH, HEIGHT, scale=SCALE_FACTOR, colorscheme=CS)

class ImageWidget(Widget):
    """
    A widget that loads and displays a list of bmp images
    """
    def __init__(self, name, paths):
        self.tilegrids = []
        self.num_images = 0
        for path in paths:
            self.num_images += 1
            self.tilegrids.append(self.__load_image(path))
        print("number of tilegrids: ", self.tilegrids.__len__())
        super().__init__(name, 0, 0, 800, 800, colorscheme=CS)
        self.append(self.tilegrids[0])
        self.current_tg_index = 0

    def __load_image(self, path):
        image, pal = adafruit_imageload.load(
            path,
            bitmap=displayio.Bitmap,
            palette=displayio.Palette,
        )
        pal.make_transparent(0)
        pal[1] = 0xFFFFFF
        tg = displayio.TileGrid(
            image,
            pixel_shader=pal,
            width=1,
            height=1,
            tile_width=800,
            tile_height=800,
        )
        return tg

    def increment_image(self):
        self.current_tg_index = self.current_tg_index + 1
        if self.current_tg_index == self.num_images:
            self.current_tg_index = 0
        try:
            # Try to get the top tilegrid
            tg = self.pop()
            tg = self.tilegrids[self.current_tg_index]
        except:
            pass
        self.append(self.tilegrids[self.current_tg_index])

    @property
    def current_index(self):
        return self.current_tg_index


m = ImageWidget("map", ["assets/florida.bmp"])
print(m.num_images)
m.increment_image()
m.set_bg_transparent(True)
gui.add_widget(m)

paths = ["assets/image0.bmp", "assets/image1.bmp", "assets/image2.bmp"]
i = ImageWidget("radar", paths)
i.set_bg_transparent(True)
gui.add_widget(i)

# Create our widgets
tw = TextWidget("text", 0, 0, WIDTH, HEIGHT, colorscheme=CS, font_path=TextWidget.LARGE_FONT)
tw.set_bg_transparent(True)
tw.set_value("hello from radar app", h_justification="center", v_justification="top")
gui.add_widget(tw)

gui.update(display)