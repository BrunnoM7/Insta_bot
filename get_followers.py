import mouse as m
import pyautogui as mp
import pyperclip as cp
import sys
import time

from create_list import create_clean_list, get_user_name, create_raw_list, define_path
from searcher import busca_usuario

#copia texto selecionado para código
def copy_clipboard():
    mp.hotkey('ctrl', 'c')
    time.sleep(.5)
    return cp.paste()

#clica nos seguidores
def click_followers():
    m.move(733,331, duration=1)
    time.sleep(4)    
    mp.click()
    time.sleep(60)

# rola a barra para destravar a lista íe volta para o incio
def unlock_followers():
    m.move(904,199, duration=2)
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
    m.move(904,199, duration=2)
    mp.mouseUp()

#começa a pegar todo o texto
def select_followers(five_seconds=1):
    m.move(516,201, duration=1)
    mp.mouseDown()
    for i in range(five_seconds):
        m.move(895,766, duration=2.5)
        m.move(528,766, duration=2.5)
    m.move(812,697, duration=2)

if __name__ == "__main__":

    rel_path = "bases/seguidores/"
    path = define_path(rel_path)

    usuario = sys.argv[1]
    tempo = int(sys.argv[2]) if len(sys.argv) > 1 else 500
    tempo_impressao = format((5*tempo)/60, '.2f')

    print(f"Iniciando coleta em {usuario} com duração aproximada de {tempo_impressao} minutos.")

    user_name = get_user_name(usuario)
    print(user_name)
    busca_usuario(user_name)

    click_followers()
    unlock_followers()
    time.sleep(2)
    select_followers(tempo)

    lista_bruta = copy_clipboard()
    time.sleep(2)
    lista_bruta = copy_clipboard()
    
    create_raw_list(path, lista_bruta)

    create_clean_list(path, usuario)

    print("Coleta finalizada")
