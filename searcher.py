import mouse as m
import pyautogui as mp
import time

def busca_usuario(texto):
    m.move(709,168,True,1)
    mp.click(interval=1)
    mp.typewrite(texto, interval=0.2)
    mp.press('enter', interval=2.0)
    mp.press('enter', presses=2)
    mp.press('enter', interval=1.0)
    time.sleep(1)
    