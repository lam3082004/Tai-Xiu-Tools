from PIL import Image
import pyautogui as pg
import pyautogui
import time
import random

TAI_X = 583
TAI_Y = 664
XIU_X = 1094
XIU_Y = 660
MOT_NGHIN_X = 476
MOT_NGHIN_Y = 836
SUBMIT_X = 828
SUBMIT_Y = 927
CANCEL_X = 1049
CANCEL_Y = 929
KQUA_X = 1093
KQUA_Y = 774

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


# SreenShot
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'E:\Tool\Tai-Xiu\Tai-Xiu.png')


def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a


dem = 5
check = True
img = "Tai-Xiu.png"
# print(rgb_of_pixel(img, KQUA_X, KQUA_Y))

if((81, 77, 134) == rgb_of_pixel(img, KQUA_X, KQUA_Y)):
    dem = dem+1
    if check == False:
        dem = 0
    check = True
else:
    dem = dem+1
    if check == True:
        dem = 0
    check = False

if(dem >= 5):
    START()
else:
    time.sleep(TIME)
# FIND_TAI_XIU_SUBMIT_POSITION()
