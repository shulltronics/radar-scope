from unigui import UniGui, PygameDisplay
from unigui import TextWidget, Solarized

# Global properties of our GUI
WIDTH = 1024
HEIGHT = 1024
SCALE_FACTOR = 1
CS = Solarized.dark

# Create the display
display = PygameDisplay(WIDTH*SCALE_FACTOR, HEIGHT*SCALE_FACTOR)

# Create the GUI
gui = UniGui(WIDTH, HEIGHT, scale=SCALE_FACTOR, colorscheme=CS)

# Create our widgets
tw = TextWidget("text", 0, 0, WIDTH, HEIGHT, colorscheme=CS)
tw.set_value("hello from radar app", h_justification="center", v_justification="top")
gui.add_widget(tw)

gui.update(display)