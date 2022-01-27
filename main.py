import pyautogui as pg
import pyautogui
import time
import random

TAI_X = 453
TAI_Y = 587
XIU_X = 802
XIU_Y = 588
MOT_NGHIN_X = 354
MOT_NGHIN_Y = 718
SUBMIT_X = 615
SUBMIT_Y = 785
CANCEL_X = 769
CANCEL_Y = 785

MONEY = 5  # 5000 nghin moi lan cuoc
TIME = 60  # 60s cuoc 1 lan


def TAI(money):
    pyautogui.click(TAI_X, TAI_Y)
    time.sleep(1)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X, MOT_NGHIN_Y)
    time.sleep(1)
    pyautogui.click(SUBMIT_X, SUBMIT_Y)


def XIU(money):
    pyautogui.click(XIU_X, XIU_Y)
    time.sleep(1)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X, MOT_NGHIN_Y)
    time.sleep(1)
    pyautogui.click(SUBMIT_X, SUBMIT_Y)


def START():
    while True:
        time.sleep(TIME)
        TAI_XIU_RANDOM = random.randint(1, 100)
        ps = pg.position()
        print(ps)
        print(TAI_XIU_RANDOM)
        if(TAI_XIU_RANDOM % 2 == 0):
            TAI(MONEY)
            print('tai an cut 5k')
        else:
            print('xiu an cut 5k')
            XIU(MONEY)


def FIND_TAI_XIU_SUBMIT_POSITION():
    while True:
        time.sleep(5)
        ps = pg.position()
        print(ps)


FIND_TAI_XIU_SUBMIT_POSITION()
# START()
