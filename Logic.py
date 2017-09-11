import cv2
import numpy as np
class Logic:
    def creategrid(img, thickness, count, color):
        h,w,c = img.shape
        h_2, w_2 = int(h/count), int(w/count)
        for i in range(count-1):
            cv2.line(img, (w_2 + i*(w_2), 0), (w_2 + i*(w_2), h), color, thickness)
        for i in range(count-1):
            cv2.line(img, (0, h_2 + i*(h_2)), (w, h_2 + i*(h_2)), color, thickness)
        return img

    def findgrid(img):
        h, w, c = img.shape
        img_output = np.zeros((h, w, 3), np.uint8)
        img_output[0:h,0:w] = (255,255,255)

        img_edge = cv2.Canny(img, 10, 50)

        x, y = 0, 0
        for i in range(h):
            x, y = 0, 0
            for j in range(w):
                if img_edge[i][j] == 255:
                    x = x + 1
                else:
                    y = y + 1
            if x == 0:
                for k in (i-1, i, i+1):
                    if i-1 > 0 and i+1 < w:
                        img_output[k, 0:w] = img[k, 0:w]

        for i in range(w):
            x, y = 0, 0
            for j in range(h):
                if img_edge[j][i] == 255:
                    x = x + 1
                else:
                    y = y + 1
            if x == 0:
                for k in (i-1, i, i+1):
                    if i-1 > 0 and i+1 < h:
                        img_output[0:h, k] = img[0:h, k]

        return img_output
'''
    img_input = cv2.imread('C:/Users/Natali/Documents/145274.jpg')

    thickness = 8
    count = 6
    color = (0, 125, 0)
    img_grid = creategrid(img_input, thickness, count, color)
    cv2.imshow('123', img_grid)

    img_only_grid = findgrid(img_grid)
    cv2.imshow('234', img_only_grid)

    cv2.waitKey(0)
'''