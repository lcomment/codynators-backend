import cv2
import numpy as np
import pyxl_modules as pm
from openpyxl import Workbook
from butter_function import head_matching as hm
from butter_function import hihat_matching as him
from imutils.object_detection import non_max_suppression
from collections import defaultdict


staff = defaultdict(list)
staff_files = [
    "./resource/b0.png",
    "./resource/b2.png",
    "./resource/b4.png",
    "./resource/b8.png",
    "./resource/basedrum.png",
    "./resource/crashbase4.png",
    "./resource/crashbase8.png",
    "./resource/highhatbnase8-1.png",
    "./resource/highhatbnase8-2.png",
    "./resource/highhatsnare8.png",
    "./resource/highhat.png",
    "./resource/snaredrum.png",
    "./resource/tomfloor.png",
    "./resource/tomhigh8.png",
    "./resource/tomhigh16.png",
    "./resource/tommiddle.png"]

def save_xlsx_value(x, y, z):
    values = []
    for i in range(1, 9):
        if i == int(x) or i == int(y) or i == int(z):
            values.append(1)
        else:
            values.append(0)
    return values

def butter_algorithm(filename):
    img = "./source/" + filename + ".png"
    image = cv2.imread(img)
    staff, image = hm(image, 0.8)

    staff, image = him(image, 0.72, staff)
    print(staff)
    workbook = Workbook() # 액셀파일로 사용하기 위한 변수

    sheet = workbook.active
    sheet['A1'] = "Hihat"
    sheet['B1'] = "Snare"
    sheet['C1'] = "Crash"
    sheet['D1'] = "HighTom"
    sheet['E1'] = "MidTom"
    sheet['F1'] = "LowTom"
    sheet['G1'] = "Ride"
    sheet['H1'] = "Base"

    for stf in staff:
        for tup in staff[stf]:
            loc = tup[4:]
            if len(loc) == 3:
                x, y, z = loc[0], loc[1], loc[2]
            elif len(loc) == 2:
                x, y, z = loc[0], loc[1], 20
            else:
                x, y, z = loc[0], 20, 20
            values = save_xlsx_value(x, y, z)
            sheet.append(values)

    workbook.save(filename + '.csv')