from PIL import Image
import pyautogui as pg
import pyautogui
import time
import os

TAI_X = 577
TAI_Y = 670
XIU_X = 1076
XIU_Y = 669
MOT_NGHIN_X = 476
MOT_NGHIN_Y = 855
SUBMIT_X = 817
SUBMIT_Y = 931
KQUA_X = 1062
KQUA_Y = 764


def TAI(money):
    pyautogui.click(TAI_X, TAI_Y)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X, MOT_NGHIN_Y)
    pyautogui.click(SUBMIT_X, SUBMIT_Y)
    pyautogui.click(SUBMIT_X, SUBMIT_Y)


def XIU(money):
    pyautogui.click(XIU_X, XIU_Y)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X, MOT_NGHIN_Y)
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

    Time = 0
    Round = 0
    dem = 0
    dem_1_1 = 0
    dem_1_2 = 0
    dem_2_2 = 0
    dem_3_3 = 0
    dem_4_4 = 0

    check = -1
    check1 = -1
    check2 = -1
    check3 = -1
    check4 = -1

    pick0_4 = -1
    pick0_6 = -1
    pick0_12 = -1
    pick0_24 = -1
    pick1_4 = -1
    pick1_6 = -1
    pick1_12 = -1
    pick1_24 = -1
    pick = 0

    while True:
        TIEN_CUOC = 0
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'E:\Tool\Tai-Xiu\Tai-Xiu.png')

        def rgb_of_pixel(img_path, x, y):
            im = Image.open(img_path).convert('RGB')
            r, g, b = im.getpixel((x, y))
            a = (r, g, b)
            return a

        img = "Tai-Xiu.png"
        # 4 cầu gần nhất
        check3 = check2
        check2 = check1
        check1 = check
        if rgb_of_pixel(img, KQUA_X, KQUA_Y)[0] == 214 and rgb_of_pixel(img, KQUA_X, KQUA_Y)[1] == 254 and rgb_of_pixel(img, KQUA_X, KQUA_Y)[2] == 255:
            dem = dem+1
            if check == 1:
                dem = 1
                dem_1_1 = dem_1_1+1
            else:
                dem_1_1 = 0

            if dem == 1 and dem_1_1 == 1:
                dem_2_2 = dem_2_2
            elif dem == 2 and check == 0:
                dem_2_2 = dem_2_2 + 1
            else:
                dem_2_2 = 0

            check = 0
        else:
            dem = dem+1
            if check == 0:
                dem = 1
                dem_1_1 = dem_1_1+1
            else:
                dem_1_1 = 0

            if dem == 1 and dem_1_1 == 1:
                dem_2_2 = dem_2_2
            elif dem == 2 and check == 1:
                dem_2_2 = dem_2_2 + 1
            else:
                dem_2_2 = 0
            check = 1

        # Đếm cầu 1-2
        if dem_1_1 == 1 and dem_2_2 == 1:
            dem_1_2 = dem_1_2+1
        if dem_1_1 >= 3 or dem_2_2 >= 2 or dem >= 3:
            dem_1_2 = 0

        # Đếm cầu 3-3
        if dem == 3:
            dem_3_3 = dem_3_3+1
        if dem_2_2 >= 2 or dem_1_1 >= 2 or dem >= 4:
            dem_3_3 = 0
        if dem_2_2 == 1 and dem_1_1 == 1:
            dem_3_3 = 0

        if check == 0:
            if pick0_4 == 0 or pick0_6 == 0 or pick0_12 == 0 or pick0_24 == 0:
                pick0_4 = -1
                pick0_6 = -1
                pick0_12 = -1
                pick0_24 = -1
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ HÚP TRỌN ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            if pick1_6 == 0 or pick1_6 == 0 or pick1_12 == 0 or pick1_24 == 0:
                pick1_4 = -1
                pick1_6 = -1
                pick1_12 = -1
                pick1_24 = -1
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ HÚP TRỌN ~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        Round = Round + 1
        print(Round)
        file = open("./Data.txt", "w", encoding="utf-8")
        file.write("--------------Round")
        file.write("\n")
        # file.write("Đếm 1-1:", dem_1_1)
        # file.write("\n")
        # file.write("Đếm 2-2:", dem_2_2)
        # file.write("\n")
        file.write("Đếm Bệt:")
        # file.write(dem)
        file.write("\n")

        print('Đếm 1-1:', dem_1_1)
        print('Đếm 1-2:', dem_1_2)
        print('Đếm 2-2:', dem_2_2)
        print('Đếm 3-3:', dem_3_3)
        # print('Đếm 4-4:', dem_4_4)
        print('Đếm Bệt:', dem)
        if check == 0:
            print('Kết quả:', 'Tài')
            file.write("Kết quả:")
            file.write("TÀI")
        else:
            print('Kết quả:', 'Xỉu')
            file.write("Kết quả:")
            file.write("XỈU")
        print("-------------------------------------------------------------------------------")
        if dem_1_1 == 10:
            dem = 6
        if dem_1_2 == 5:
            dem_1_2 = 4
        if(dem == 11):
            dem = 7
        if dem_2_2 == 6:
            dem_2_2 = 4
        if dem_3_3 == 4:
            dem_3_3 = 3
        if(dem >= 7):
            if dem == 7:
                TIEN_CUOC = 4
            elif dem == 8:
                TIEN_CUOC = 6
            elif dem == 9:
                TIEN_CUOC = 12
            elif dem == 10:
                TIEN_CUOC = 24
            if check == 1:
                TAI(TIEN_CUOC)
                print('Đã chọn TÀI', TIEN_CUOC, 'k')
                if dem == 7:
                    pick0_4 = pick0_4+1
                if dem == 8:
                    pick0_6 = pick0_6+1
                if dem == 9:
                    pick0_12 = pick0_12+1
                if dem == 10:
                    pick0_24 = pick0_24+1
            else:
                XIU(TIEN_CUOC)
                print('Đã chọn XỈU', TIEN_CUOC, 'k')
                if dem == 7:
                    pick1_4 = pick1_4+1
                if dem == 8:
                    pick1_6 = pick1_6+1
                if dem == 9:
                    pick1_12 = pick1_12+1
                if dem == 10:
                    pick1_24 = pick1_24+1
        else:
            if dem_1_1 == 6:
                if check == 0:
                    pick0_4 = pick0_4+1
                    TAI(4)
                    print('Đã chọn TÀI', 4, 'k')
                else:
                    pick1_4 = pick1_4+1
                    XIU(4)
                    print('Đã chọn XỈU', 4, 'k')
            elif dem_1_1 == 7:
                if check == 0:
                    pick0_6 = pick0_6+1
                    TAI(6)
                    print('Đã chọn TÀI', 6, 'k')
                else:
                    pick1_6 = pick1_6+1
                    XIU(6)
                    print('Đã chọn XỈU', 6, 'k')
            elif dem_1_1 == 8:
                if check == 0:
                    pick0_12 = pick0_12+1
                    TAI(12)
                    print('Đã chọn TÀI', 12, 'k')
                else:
                    pick1_12 = pick1_12+1
                    XIU(12)
                    print('Đã chọn XỈU', 12, 'k')
            elif dem_1_1 == 9:
                if check == 0:
                    pick0_24 = pick0_24+1
                    TAI(24)
                    print('Đã chọn TÀI', 24, 'k')
                else:
                    pick1_24 = pick1_24+1
                    XIU(24)
                    print('Đã chọn XỈU', 24, 'k')
            else:
                if dem_2_2 == 4:
                    if check == 0 and dem_1_1 == 0:
                        pick0_4 = pick0_4+1
                        TAI(4)
                        print('Đã chọn TÀI', 4, 'k')
                    elif check == 1 and dem_1_1 == 0:
                        pick1_4 = pick1_4+1
                        XIU(4)
                        print('Đã chọn XỈU', 4, 'k')
                    elif check == 0 and dem_1_1 == 1:
                        pick1_6 = pick1_6+1
                        XIU(6)
                        print('Đã chọn XỈU', 6, 'k')
                    elif check == 1 and dem_1_1 == 1:
                        pick0_6 = pick0_6+1
                        TAI(6)
                        print('Đã chọn TÀI', 6, 'k')
                elif dem_2_2 == 5:
                    if check == 0 and dem_1_1 == 0:
                        pick0_12 = pick0_12+1
                        TAI(12)
                        print('Đã chọn TÀI', 12, 'k')
                    elif check == 1 and dem_1_1 == 0:
                        pick0_12 = pick0_12+1
                        XIU(12)
                        print('Đã chọn XỈU', 12, 'k')
                    elif check == 0 and dem_1_1 == 1:
                        pick1_24 = pick1_24+1
                        XIU(24)
                        print('Đã chọn XỈU', 24, 'k')
                    elif check == 1 and dem_1_1 == 1:
                        pick0_24 = pick0_24+1
                        TAI(24)
                        print('Đã chọn TÀI', 24, 'k')
                else:
                    if dem_1_2 == 4:
                        if dem_2_2 == 1 and dem == 2:
                            if check == 0:
                                pick1_4 = pick1_4+1
                                XIU(4)
                                print('Đã chọn XỈU', 4, 'k')
                            else:
                                pick0_4 = pick0_4+1
                                TAI(4)
                                print('Đã chọn TÀI', 4, 'k')
                        elif dem_1_1 == 1 and dem_2_2 == 1:
                            if check == 0:
                                pick0_6 = pick0_6+1
                                TAI(6)
                                print('Đã chọn TÀI', 6, 'k')
                            else:
                                pick1_6 = pick1_6+1
                                XIU(6)
                                print('Đã chọn XỈU', 6, 'k')
                        elif dem_1_1 == 2:
                            if check == 0:
                                pick1_12 = pick1_12+1
                                XIU(12)
                                print('Đã chọn XỈU', 12, 'k')
                            else:
                                pick0_12 = pick0_12+1
                                TAI(12)
                                print('Đã chọn TÀI', 12, 'k')
                    else:
                        if dem_3_3 == 3:
                            if dem_1_1 == 0:
                                if check == 0:
                                    pick0_4 = pick0_4+1
                                    TAI(4)
                                    print('Đã chọn TÀI', 4, 'k')
                                else:
                                    pick1_4 = pick1_4+1
                                    XIU(4)
                                    print('Đã chọn XỈU', 4, 'k')
                            elif dem_1_1 == 1:
                                if check == 0:
                                    pick1_6 = pick1_6+1
                                    XIU(6)
                                    print('Đã chọn XỈU', 6, 'k')
                                else:
                                    pick0_6 = pick0_6+1
                                    TAI(6)
                                    print('Đã chọn TÀI', 6, 'k')
                            elif dem == 2:
                                if check == 0:
                                    pick1_12 = pick1_12+1
                                    XIU(12)
                                    print('Đã chọn XỈU', 12, 'k')
                                else:
                                    pick0_12 = pick0_12+1
                                    TAI(12)
                                    print('Đã chọn TÀI', 12, 'k')

        time.sleep(68.6)
        file_path = './Tai-Xiu.png'
        os.remove(file_path)


# FIND_RGB_COLOR()
# FIND_TAI_XIU_SUBMIT_POSITION()
START()
