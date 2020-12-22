"""
This script needs some things to work:
1 - It needs to have fluidsynth .dlls in the same directory
The dlls can be downloaded from https://www.fluidsynth.org/
Just copy ALL .dlls from fluidsynth/bin folder to script folder
2 - Install pyFluidSynth, it can be installed with command: pip install pyfluidsynth
3 - It needs a SoundFont. They can be downloaded from https://sites.google.com/site/soundfonts4u/
Don't forget to change the name in the script to match the SoundFont name
4 - The keys have to be configured to match personal preference
"""


""" ----- CONFIGURATIONS -----"""
font_name = 'chateau_grand.sf2'

"""
Define keyboard keys here
keyboard_key -> piano_key
piano_key is value between 1-88
"""
keys_config = {'a':40,
               's':42,
               'd':44,
               'f':45,
               'j':47,
               'k':49,
               'l':51}

"""How strongly keys are pressed [0-127] (Default = 60)"""
vel = 60

""" ----- END OF CONFIGURATIONS ----- """


import keyboard
import fluidsynth


"""Creates a Synth"""
fs = fluidsynth.Synth()
fs.start()

"""Loads the sound font from the directory(it needs to be downloaded)"""
sfid = fs.sfload(font_name)

"""Starts the Channel"""
fs.program_select(0, sfid, 0, 0)

"""Increases volume(127 is max)"""
fs.cc(0,7,127)

"""If you hold down a key, pressed events are constantly generated"""
"""The following dictionary is a work around this issue"""
currently_pressed = dict()
for keyboard_key in keys_config.keys():
    currently_pressed[keyboard_key] = False


def press_or_release(e):

    # KEY_DOWN Event(Key Pressed)
    if e.event_type == keyboard.KEY_DOWN:
        if e.name in keys_config.keys():
            if not currently_pressed[e.name]:
                fs.noteon(0, keys_config[e.name], vel)
                currently_pressed[e.name] = True

    # KEY_UP Event(Key Released)
    elif e.event_type == keyboard.KEY_UP:
        if e.name in keys_config.keys():
            fs.noteoff(0, keys_config[e.name])
            currently_pressed[e.name] = False


def main():

    # On Event calls function press_or_release
    keyboard.hook(press_or_release)

    # Sleeps until 'esc' key is pressed
    keyboard.wait('esc')


if __name__ == '__main__':
    main()

