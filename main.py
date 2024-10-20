# !/usr/bin/env python

import pynput.keyboard

def proccess_key_press(key):
  print(key)

keyboard_listener = pynput.keyboard.Listener(on_press=proccess_key_press)

with keyboard_listener:
  keyboard_listener.join()