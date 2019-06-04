import mouse as m
import pyautogui as mp

import searcher as s

import sys


mp.PAUSE = 0.5
seguidor_inicial_y = 310 
espacamento = 48
seguidor_atual_y = seguidor_inicial_y

def curte_foto():
    mp.click()
    m.move(536,470,True,1)
    mp.click(clicks=2,interval=0.2)
    m.move(1292,591,True,1)
    mp.click()

def rola_baixo():
    m.move(1362,172,True,1)
    mp.mouseDown()
    m.move(1365,203,True,0.5)
    mp.mouseUp()

def rola_cima():
    m.move(1365,203,True,0.5)
    mp.mouseDown()
    m.move(1362,172,True,1)
    mp.mouseUp()

def curte_fotos():
    rola_baixo()
    m.move(435,746,True,2)
    curte_foto()
    m.move(725,746,True,1.5)
    curte_foto()
    m.move(1018,746,True,1.5)
    curte_foto()
    rola_cima()

def voltar():
    m.move(92,106,True,1)
    mp.click()




"""
def ativa_seguidor(posicao):
    m.move(601,posicao,True,1)
    mp.click()
    curte_fotos()
    voltar()
"""

if __name__ == "__main__":

    db_file = open(sys.argv[1], 'r')
    lines = db_file.readlines()

    counter = 0
    for line in lines:
        user = line.rstrip()
        if(counter % 10 == 0):
            s.busca_usuario_browser(user)
        else:
            s.busca_usuario(user)
        curte_fotos()
        counter+= 1
