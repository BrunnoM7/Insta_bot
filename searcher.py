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
    

def busca_usuario_browser(texto):
    texto_busca = f"https://www.instagram.com/{texto}/"
    m.move(885,112,True,1)
    mp.click(clicks=2 ,interval=1)
    mp.click(clicks=2)
    mp.typewrite(texto_busca, interval=0.2)
    mp.press('enter', interval=2.0)
    time.sleep(10)