from unigui import UniGui, PygameDisplay
from unigui import TextWidget, Solarized

# Global properties of our GUI
WIDTH = 800
HEIGHT = 600
SCALE_FACTOR = 2
CS = Solarized.light

# Create the display
display = PygameDisplay(WIDTH*SCALE_FACTOR, HEIGHT*SCALE_FACTOR)

# Create the GUI
gui = UniGui(WIDTH, HEIGHT, scale=SCALE_FACTOR, colorscheme=Solarized.light)

# Create our widgets
tw = TextWidget("text", 0, 0, WIDTH, HEIGHT, colorscheme=Solarized.light)
tw.set_value("hello from radar app", h_justification="center", v_justification="top")
gui.add_widget(tw)

gui.update(display)