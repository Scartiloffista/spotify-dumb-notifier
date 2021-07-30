from SwSpotify import SpotifyClosed, SpotifyNotRunning, SpotifyPaused, spotify
import pystray
import time
import sys
import os

def create_image():
    from PIL import Image, ImageDraw
    # for now, dumb icon
    width = 20
    height = 20
    color1 = (228, 150, 150)
    color2 = (0,0,0)
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)
    return image

def display_notification(icon):
    icon.visible = True
    string_to_display = ""
    while(icon.visible):
        time.sleep(1)
        try:
            new_string = spotify.song() + " - " + spotify.artist()
            if(new_string != string_to_display):
                string_to_display = new_string
                icon.title = spotify.song()
                icon.notify(spotify.artist())
        except SpotifyClosed or SpotifyNotRunning or SpotifyPaused:
            pass

def quit_everything(icon):
    icon.visible = False
    import signal
    os.kill(os.getpid(), signal.SIGTERM)    

def handle_systray():
    from pystray import Icon as icon, Menu as menu, MenuItem as item
    icon = pystray.Icon('Spotify Notification', create_image(), title='Spotify Notification', menu=menu(
    item(
        'Quit',
        lambda icon, item: quit_everything(icon))))


    icon.run(display_notification)

handle_systray()