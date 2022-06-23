import cv2
import numpy as np
import pyxl_modules as pm
from openpyxl import Workbook
from imutils.object_detection import non_max_suppression
from collections import defaultdict


staff = defaultdict(list)


def get_center(start_y, end_y):
    return (end_y - start_y) / 2 + start_y


def head_priority(_staff):
    new_staff = []
    visited = defaultdict(bool)
    for key in _staff:
        visited[key] = False

    for values in _staff:
        for copy in _staff:
            if values == copy or visited[values] is True:
                continue
            if values[0] - copy[0] == 0 or abs(values[0] - copy[0]) == 1 or abs(values[0] - copy[0]) == 2:
                # Visited Node
                visited[values] = True
                visited[copy] = True
                if values[1] > copy[1]:
                    priority = values + tuple('2')
                else:
                    priority = copy + tuple('2')
                if priority not in new_staff:
                    new_staff.append(priority)
                    break
        if not visited[values]:
            visited[values] = True
            new_staff.append(values)
    _staff = new_staff
    return _staff


def head_matching(img, thr):

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
        if loc[1] <= 321:
            center = get_center(loc[1], loc[3])
            if 311 < center < 320:
                staff[1].append(tuple(loc) + tuple('8'))
            elif 287 < center < 296:
                staff[1].append(tuple(loc) + tuple('2'))
            elif center < 287:
                staff[1].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 506:
            center = get_center(loc[1], loc[3])
            if 496 < center < 505:
                staff[2].append(tuple(loc) + tuple('8'))
            elif 472 < center < 481:
                staff[2].append(tuple(loc) + tuple('2'))
            elif center < 472:
                staff[2].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 690:
            center = get_center(loc[1], loc[3])
            if 680 < center < 689:
                staff[3].append(tuple(loc) + tuple('8'))
            elif 657 < center < 666:
                staff[3].append(tuple(loc) + tuple('2'))
            elif center < 657:
                staff[3].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 875:
            center = get_center(loc[1], loc[3])
            if 865 < center < 874:
                staff[4].append(tuple(loc) + tuple('8'))
            elif 841 < center < 850:
                staff[4].append(tuple(loc) + tuple('2'))
            elif center < 841:
                staff[4].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 1060:
            center = get_center(loc[1], loc[3])
            if 1050 < center < 1059:
                staff[5].append(tuple(loc) + tuple('8'))
            elif 1026 < center < 1035:
                staff[5].append(tuple(loc) + tuple('2'))
            elif center < 1026:
                staff[5].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 1244:
            center = get_center(loc[1], loc[3])
            if 1234 < center < 1243:
                staff[6].append(tuple(loc) + tuple('8'))
            elif 1210 < center < 1219:
                staff[6].append(tuple(loc) + tuple('2'))
            elif center < 1210:
                staff[6].append(tuple(loc) + tuple('4'))
        elif loc[1] <= 1429:
            center = get_center(loc[1], loc[3])
            if 1419 < center < 1428:
                staff[7].append(tuple(loc) + tuple('8'))
            elif 1395 < center < 1404:
                staff[7].append(tuple(loc) + tuple('2'))
            elif center < 1395:
                staff[7].append(tuple(loc) + tuple('4'))
        else:
            center = get_center(loc[1], loc[3])
            if 1603 < center < 1612:
                staff[8].append(tuple(loc) + tuple('8'))
            elif 1580 < center < 1589:
                staff[8].append(tuple(loc) + tuple('2'))
            elif center < 1580:
                staff[8].append(tuple(loc) + tuple('4'))

    for key in staff:
        staff[key].sort(key=lambda x: x[0])

    staff[5] = head_priority(staff[5])
    staff[6] = head_priority(staff[6])
    return staff, img


def hihat_matching(img, thr, _staff):
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

        if loc[1] <= 321:
            for idx, value in enumerate(_staff[1]):
                if value[0] < center < value[2]:
                    _staff[1][idx] = _staff[1][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                _staff[1].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 506:
            for idx, value in enumerate(_staff[2]):
                if value[0] < center < value[2]:
                    _staff[2][idx] = _staff[2][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                _staff[2].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 690:
            for idx, value in enumerate(_staff[3]):
                if value[0] < center < value[2]:
                    _staff[3][idx] = _staff[3][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                _staff[3].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 875:
            for idx, value in enumerate(_staff[4]):
                if value[0] < center < value[2]:
                    _staff[4][idx] = _staff[4][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                _staff[4].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 1060:
            for idx, value in enumerate(_staff[5]):
                if value[0] < center < value[2]:
                    _staff[5][idx] = _staff[5][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                _staff[5].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 1244:
            for idx, value in enumerate(_staff[6]):
                if value[0] < center < value[2]:
                    _staff[6][idx] = _staff[6][idx] + tuple('1')
                    flag = True
                    break
            if flag is False:
                _staff[6].append(tuple(loc) + tuple('1'))
        elif loc[1] <= 1429:
            _staff[7].append(tuple(loc) + tuple('1'))
        else:
            _staff[8].append(tuple(loc) + tuple('1'))

    for key in staff:
        _staff[key].sort(key=lambda x: x[0])
    # print(staff)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    return _staff, img