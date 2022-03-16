from PIL import Image
import pyautogui as pg
import pyautogui
import time
import os

TAI_X = 585
TAI_Y = 679
XIU_X = 1078
XIU_Y = 686
MOT_NGHIN_X = 477
MOT_NGHIN_Y = 850
SUBMIT_X = 802
SUBMIT_Y = 931
KQUA_X = 1064
KQUA_Y = 771
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
        time.sleep(5)
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
        if rgb_of_pixel(img, KQUA_X, KQUA_Y)[0] == 212 and rgb_of_pixel(img, KQUA_X, KQUA_Y)[1] == 255 and rgb_of_pixel(img, KQUA_X, KQUA_Y)[2] == 255:
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

        if(dem == 7):
            dem = 1
        if(dem >= 4):
            TIEN_CUOC = pow(2, dem-3) * MONEY
            if check == 1:
                pick = 0
                TAI(TIEN_CUOC)
                print('Đã chọn TÀI', TIEN_CUOC, 'k')
            else:
                pick = 1
                XIU(TIEN_CUOC)
                print('Đã chọn XỈU', TIEN_CUOC, 'k')
        else:
            pick = -1

        if pick == -1:
            time.sleep(68.2)
        else:
            time.sleep(67.2)
        file_path = './Tai-Xiu.png'
        os.remove(file_path)


# FIND_RGB_COLOR()
# FIND_TAI_XIU_SUBMIT_POSITION()
START()
