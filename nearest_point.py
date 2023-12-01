import math
from math import *
# I am just writing a function by using this function we can get the nearest point of red dot

# for blue dot list from the file as a dimension list


def blue(file1):
    try:
        with open(file1) as bluedot:
            line = bluedot.readline().strip()
            blue_list = []
            while line != '':
                blue_list.append(line.split(','))
                line = bluedot.readline().strip()
        return blue_list
    except IOError:
        print(f'{file1} does not exist')
        exit()

# for red dot


def red(file2):
    try:
        with open(file2) as red_dot:
            red_point = red_dot.readline().strip().split(',')
            return red_point
    except IOError:
        print(f'{file2} does not exist')
        exit()

# to calculate the nearest coordinate


def closest(red_point, blue_list):
    nearest = sqrt(pow((int(red_point[0])-int(blue_list[0][0])), 2)+pow((int(red_point[1])-int(blue_list[0][1])), 2))
    coordinates = blue_list[0]
    for i in range(1, len(blue_list)):
        distance = sqrt(pow((int(red_point[0])-int(blue_list[i][0])), 2)+pow((int(red_point[1])-int(blue_list[i][1])), 2))
        if distance < nearest:
            nearest = distance
            coordinates = blue_list[i]
    print(coordinates)

