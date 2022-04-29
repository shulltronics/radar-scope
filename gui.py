from unigui import UniGui, PygameDisplay
from unigui import TextWidget

# Global properties of our GUI
WIDTH = 800
HEIGHT = 600
SCALE_FACTOR = 2

# Create the display
display = PygameDisplay(WIDTH*SCALE_FACTOR, HEIGHT*SCALE_FACTOR)

# Create the GUI
gui = UniGui(WIDTH, HEIGHT, scale=SCALE_FACTOR)

# Create our widgets
tw = TextWidget("text", 0, 0, WIDTH, HEIGHT)
tw.set_value("hello from radar app", h_justification="center", v_justification="top")
gui.add_widget(tw)

gui.update(display)