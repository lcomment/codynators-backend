# from pdf2image import convert_from_path
# import cv2
# import preprocessing
# import objectProcessing
# import objectRecognition
# import recognition_modules
# import numpy as np
# import functions as fs
# import os
# import pyxl_modules as pm
# from openpyxl import Workbook
#
# file_name = "canthave.png"
# #
# # pages = convert_from_path("./musicsheet/" + file_name)
#
# workbook = Workbook()
#
# # for i, page in enumerate(pages):
# #     if i == 0: # 첫 페이지
# sheet = pm.init_excel(workbook)  # 액셀 파일 초기화
#
#
# file = "./source/" + file_name
# # page.save(file, "JPEG")
#
# image = cv2.imread(file, 0)
# img_gray = image
# image = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
# ret, img_gray = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# img_width, img_height = img_gray.shape[::-1]
#
# masked_image = preprocessing.remove_noise(image)
#
#
# noStaves_img, staves = preprocessing.rmStaves(masked_image)
#
# normal_MS, staves = preprocessing.musicsheetNormalization(
#     noStaves_img, staves, 150)
# # 4. 객체 검출 과정
# normal_MS = fs.closing(normal_MS)
# findObject, objects = objectProcessing.object_detection(normal_MS, staves)
# #     #cv2.connectedComponentsWithStats(src, label, stats, centroids)
# #     # src 입력 이미지, labels: 레이블 맵 행렬, stats: connected components를 감싸는 직사각형 및 픽셀 정보를 담고 있음 centroids: 각 connected components의 무게 중심 위치
# #     # cv2.rectangle(img, pt1, pt2, color, thickness)
# #     # img : 이미지 파일, pt1: 시작점 좌표, pt2: 종료점 좌표 color: 색상 , thickness : 선 두께
# #
# #     # 5. 객체 분석 과정
# findObject, objects = objectRecognition.object_analysis(findObject, objects)
# #
# #     # 6. 인식 과정
# findObject, key, beats, pitches = objectRecognition.recognition(
#     findObject, staves, objects)
#
#
# cv2.imwrite("./source/" + "검출" + ".png", findObject)
# print("exit")
import cv2
import sys
import numpy as np
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


def get_center(start_y, end_y):
    return (end_y - start_y) / 2 + start_y


def head_matching(img, thr):
    # img = cv2.imread(image)
    # binary_img = fs.threshold(img)
    # height, width = binary_img.shape
    # print(height, width, "\n\n")
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread("./resource/head.png", cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[:2]
    result = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)

    (yCoords, xCoords) = np.where(result >= thr)
    print("[INFO] {} matched locations *before* NMS".format(len(yCoords)))
    rects = []
    tup = []
    for (x, y) in zip(xCoords, yCoords):
        rects.append((x, y, x + w * 2, y + h / 2))

    pick = non_max_suppression(np.array(rects))
    for (startX, startY, endX, endY) in pick:
        # draw the bounding box on the image
        # if startX == 647 and startY == 1250:
        cv2.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 3)

    for i in range(1, 9):
        staff[i] = []

    for loc in pick:
        if loc[1] <= 311:
            center = get_center(loc[1], loc[3])
            if 301 < center < 310:
                staff[1].append(tuple(loc) + tuple('8'))
            elif 289 < center < 298:
                staff[1].append(tuple(loc) + tuple('6'))
            elif 277 < center < 286:
                staff[1].append(tuple(loc) + tuple('2'))
            elif center < 274:
                staff[1].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 501:
            center = get_center(loc[1], loc[3])
            if 491 < center < 500:
                staff[2].append(tuple(loc) + tuple('8'))
            elif 479 < center < 488:
                staff[2].append(tuple(loc) + tuple('6'))
            elif 466 < center < 475:
                staff[2].append(tuple(loc) + tuple('2'))
            elif center < 463:
                staff[2].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 691:
            center = get_center(loc[1], loc[3])
            if 681 < center < 690:
                staff[3].append(tuple(loc) + tuple('8'))
            elif 656 < center < 665:
                staff[3].append(tuple(loc) + tuple('2'))
            elif center < 647:
                staff[3].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 880:
            center = get_center(loc[1], loc[3])
            if 870 < center < 879:
                staff[4].append(tuple(loc) + tuple('8'))
            elif 858 < center < 867:
                staff[4].append(tuple(loc) + tuple('6'))
            elif 846 < center < 855:
                staff[4].append(tuple(loc) + tuple('2'))
            elif center < 843:
                staff[4].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 1070:
            center = get_center(loc[1], loc[3])
            if 1060 < center < 1069:
                staff[5].append(tuple(loc) + tuple('8'))
            elif 1036 < center < 1045:
                staff[5].append(tuple(loc) + tuple('2'))
            elif center < 1026:
                staff[5].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 1260:
            center = get_center(loc[1], loc[3])
            if 1250 < center < 1259:
                staff[6].append(tuple(loc) + tuple('8'))
            elif 1238 < center < 1247:
                staff[6].append(tuple(loc) + tuple('6'))
            elif 1226 < center < 1235:
                staff[6].append(tuple(loc) + tuple('2'))
            elif center < 1222:
                staff[6].append(tuple(loc) + tuple('4'))
            else:
                staff[6].append(tuple(loc))
        elif loc[1] <= 1222:
            staff[7].append(tuple(loc))
        else:
            staff[8].append(tuple(loc))

    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    return staff, img


def hihat_matching(img, thr):
    # img = cv2.imread(image)
    # binary_img = fs.threshold(img)
    # height, width = binary_img.shape
    # print(height, width, "\n\n")
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread("./resource/hihat.png", cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[:2]
    result = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)

    (yCoords, xCoords) = np.where(result >= thr)
    print("[INFO] {} matched locations *before* NMS".format(len(yCoords)))
    rects = []
    tup = []
    for (x, y) in zip(xCoords, yCoords):
        rects.append((x, y, x + w, y + h))

    pick = non_max_suppression(np.array(rects))
    for (startX, startY, endX, endY) in pick:
        # draw the bounding box on the image
        # if startX == 647 and startY == 1250:
        cv2.rectangle(img, (startX, startY), (endX, endY), (0, 125, 0), 3)

    for loc in pick:
        flag = False
        center = get_center(loc[0], loc[2])

        if loc[1] <= 311:
            for idx, value in enumerate(staff[1]):
                if value[0] < center < value[2]:
                    staff[1][idx] = staff[1][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                staff[1].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 501:
            for idx, value in enumerate(staff[2]):
                if value[0] < center < value[2]:
                    staff[2][idx] = staff[2][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                staff[2].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 691:
            for idx, value in enumerate(staff[3]):
                if value[0] < center < value[2]:
                    staff[3][idx] = staff[3][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                staff[3].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 880:
            for idx, value in enumerate(staff[4]):
                if value[0] < center < value[2]:
                    staff[4][idx] = staff[4][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                staff[4].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 1070:
            for idx, value in enumerate(staff[5]):
                if value[0] < center < value[2]:
                    staff[5][idx] = staff[5][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                staff[5].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 1260:
            for idx, value in enumerate(staff[6]):
                if value[0] < center < value[2]:
                    staff[6][idx] = staff[6][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                staff[6].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 1222:
            staff[7].append(tuple(loc) + tuple('1'))
        else:
            staff[8].append(tuple(loc) + tuple('1'))

    for key in staff:
        staff[key].sort(key=lambda x: x[0])
    # print(staff)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    return staff, img


def crash_matching(img, thr):
    # img = cv2.imread(image)
    # binary_img = fs.threshold(img)
    # height, width = binary_img.shape
    # print(height, width, "\n\n")
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread("./resource/crash.png", cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[:2]
    result = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)

    (yCoords, xCoords) = np.where(result >= thr)
    print("[INFO] {} matched locations *before* NMS".format(len(yCoords)))
    rects = []
    tup = []
    for (x, y) in zip(xCoords, yCoords):
        rects.append((x, y, x + w, y + h))

    pick = non_max_suppression(np.array(rects))
    for (startX, startY, endX, endY) in pick:
        # draw the bounding box on the image
        # if startX == 647 and startY == 1250:
        cv2.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 3)

    for loc in pick:
        flag = False
        center = get_center(loc[0], loc[2])

        if loc[1] <= 311:
            for idx, value in enumerate(staff[1]):
                if value[0] < center < value[2]:
                    staff[1][idx] = staff[1][idx] + tuple('3')
                    flag = True
                    break
            if flag is False:
                staff[1].append(tuple(loc) + tuple('3'))
        elif loc[1] <= 501:
            for idx, value in enumerate(staff[2]):
                if value[0] < center < value[2]:
                    staff[2][idx] = staff[2][idx] + tuple('3')
                    flag = True
                    break
            if flag is False:
                staff[2].append(tuple(loc) + tuple('3'))
        elif loc[1] <= 691:
            for idx, value in enumerate(staff[3]):
                if value[0] < center < value[2]:
                    staff[3][idx] = staff[3][idx] + tuple('3')
                    flag = True
                    break
            if flag is False:
                staff[3].append(tuple(loc) + tuple('3'))
        elif loc[1] <= 880:
            for idx, value in enumerate(staff[4]):
                if value[0] < center < value[2]:
                    staff[4][idx] = staff[4][idx] + tuple('3')
                    flag = True
                    break
            if flag is False:
                staff[4].append(tuple(loc) + tuple('3'))
        elif loc[1] <= 1070:
            for idx, value in enumerate(staff[5]):
                if value[0] < center < value[2]:
                    staff[5][idx] = staff[5][idx] + tuple('3')
                    flag = True
                    break
            if flag is False:
                staff[5].append(tuple(loc) + tuple('3'))
        elif loc[1] <= 1260:
            for idx, value in enumerate(staff[6]):
                if value[0] < center < value[2]:
                    staff[6][idx] = staff[6][idx] + tuple('3')
                    flag = True
                    break
            if flag is False:
                staff[6].append(tuple(loc) + tuple('3'))
        elif loc[1] <= 1222:
            staff[7].append(tuple(loc) + tuple('3'))
        else:
            staff[8].append(tuple(loc) + tuple('3'))

    for key in staff:
        staff[key].sort(key=lambda x: x[0])
    return staff, img


img = "./source/canthaveyou.png"
image = cv2.imread(img)
# 헤드 탐색
staff, image = head_matching(image, 0.8)

# 하이햇 탐색
staff, image = hihat_matching(image, 0.8)

staff, image = crash_matching(image, 0.9)
cv2.imshow('img', image)
cv2.waitKey(0)
# [[1번], [2번] ... ]
