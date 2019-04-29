import mouse as m
import pyautogui as mp
import pyperclip as cp
import sys
import time

from create_list import create_clean_list, get_user_name
from searcher import busca_usuario

#cria lista bruta
def create_raw_list(content):
    file = open('raw_list', 'w')
    file.write(content)
    file.close()

#copia texto selecionado para código
def copy_clipboard():
    mp.hotkey('ctrl', 'c')
    time.sleep(.01)
    return cp.paste()

#clica nos seguidores
def click_followers():
    m.move(782,337, duration=1)
    mp.click()

# rola a barra para destravar a lista íe volta para o incio
def unlock_followers():
    m.move(904,309, duration=2)
    mp.mouseDown()
    m.move(904,352, duration=2)
    mp.mouseUp()
    mp.mouseDown()
    m.move(904,382, duration=2)
    mp.mouseUp()
    mp.mouseDown()
    m.move(904,402, duration=2)
    mp.mouseUp()
    mp.mouseDown()
    m.move(904,422, duration=2)
    mp.mouseUp()
    mp.mouseDown()
    m.move(904,309, duration=2)
    mp.mouseUp()

#começa a pegar todo o texto
def select_followers(five_seconds=1):
    m.move(516,312, duration=1)
    mp.mouseDown()
    for i in range(five_seconds):
        m.move(835,675, duration=2.5)
        m.move(574,680, duration=2.5)

if __name__ == "__main__":

    usuario = sys.argv[1]

    user_name = get_user_name(usuario)
    print(user_name)
    busca_usuario(user_name)

    click_followers()
    unlock_followers()
    select_followers(300)

    lista_bruta = copy_clipboard()
    create_raw_list(lista_bruta)

    create_clean_list(usuario)
