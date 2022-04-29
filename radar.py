from gui import display, gui, tw

print("Starting Radar App...")

while True:
    display.refresh()
    click = display.get_mouse_clicks()
    if click is not None:
        print(gui.__len__())
        print("click: " + str(click))
        tw.set_value("poop")
        