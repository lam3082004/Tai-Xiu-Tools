from PIL import Image
import pyautogui as pg
import pyautogui
import time
import os

TAI_X = 582
TAI_Y = 682
XIU_X = 1077
XIU_Y = 680
MOT_NGHIN_X = 468
MOT_NGHIN_Y = 866
SUBMIT_X = 830
SUBMIT_Y = 954
KQUA_X = 1065
KQUA_Y = 773
MONEY = 1


def TAI(money):
    pyautogui.click(TAI_X, TAI_Y)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X, MOT_NGHIN_Y)
    time.sleep(1)
    pyautogui.click(SUBMIT_X, SUBMIT_Y)
    pyautogui.click(SUBMIT_X, SUBMIT_Y)


def XIU(money):
    pyautogui.click(XIU_X, XIU_Y)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X, MOT_NGHIN_Y)
    time.sleep(1)
    pyautogui.click(SUBMIT_X, SUBMIT_Y)
    pyautogui.click(SUBMIT_X, SUBMIT_Y)


def FIND_TAI_XIU_SUBMIT_POSITION():
    while True:
        time.sleep(5)
        ps = pg.position()
        print(ps)


def FIND_RGB_COLOR():
    while True:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'E:\Tool\Tai-Xiu\Tai-Xiu.png')

        def rgb_of_pixel(img_path, x, y):
            im = Image.open(img_path).convert('RGB')
            r, g, b = im.getpixel((x, y))
            a = (r, g, b)
            return a

        img = "Tai-Xiu.png"

        print(rgb_of_pixel(img, KQUA_X, KQUA_Y))
        time.sleep(60)
        file_path = './Tai-Xiu.png'
        os.remove(file_path)


def START():
    dem = 0
    check = -1
    pick = -1
    while True:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'E:\Tool\Tai-Xiu\Tai-Xiu.png')

        def rgb_of_pixel(img_path, x, y):
            im = Image.open(img_path).convert('RGB')
            r, g, b = im.getpixel((x, y))
            a = (r, g, b)
            return a

        img = "Tai-Xiu.png"
        if rgb_of_pixel(img, KQUA_X, KQUA_Y)[0] == 225 and rgb_of_pixel(img, KQUA_X, KQUA_Y)[1] == 255 and rgb_of_pixel(img, KQUA_X, KQUA_Y)[2] == 255:
            dem = dem+1
            if check == 1:
                dem = 1
            check = 0
        else:
            dem = dem+1
            if check == 0:
                dem = 1
            check = 1

        if dem >= 4:
            if check == 0 and pick == 0 or check == 1 and pick == 1:
                dem = 1
                print('Húp Trọn!!!')

        if check == 0 and dem >= 1:
            print(dem, 'TÀI')
        else:
            print(dem, 'XỈU')

        if(dem == 9):
            dem = 1
        if(dem >= 4):
            if check == 1:
                pick = 0
                TAI(pow(2, dem-4) * MONEY)
                print('Đã chọn TÀI', pow(2, dem-4) * MONEY, 'k')
            else:
                pick = 1
                XIU(pow(2, dem-4) * MONEY)
                print('Đã chọn XỈU', pow(2, dem-4) * MONEY, 'k')
        else:
            pick = -1

        if pick == -1:
            time.sleep(68.8)
        else:
            time.sleep(67.8)
        file_path = './Tai-Xiu.png'
        os.remove(file_path)


# FIND_RGB_COLOR()
# FIND_TAI_XIU_SUBMIT_POSITION()
START()
