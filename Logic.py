import cv2
print ("hi")

class Solution:
    '''
Я подумал что будет логично если ты займешься логикой работы а я накатаю интерфейс пока
как я подумал мне нужен методы возвращающий избражение cv2.imread()
creategrid принимает изображение толщину решетки и интервал между ними в целых числах и
возвращющий картинку с решеткой и нужен метод findgrid который будет принимать изображение и
возврщать рисунок решетки без задних текстур а я пока займусь интерфейсом. Как закнчу буду
помогать тебе.
    '''

    a = cv2.imread('/home/anton/Downloads/345.jpg')
    b = a
    h, w, c = a.shape
    # a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    # a = cv2.imread('/home/anton/pycharm-2017.2.3/bin/pycharm.png')
    a = cv2.Canny(a, 100, 150)
    # a = cv2.Sobel(a, cv2.CV_64F, 0, 1)
    '''
    for i in range(h):
        if a[i][0] == 255:

            for j in range(w):
                if a[i][j] == 0:
                    print (i, j)
                    break
                break
    '''
    x, y = 0, 0
    for i in range(h):
        x, y = 0, 0
        for j in range(w):
            if a[i][j] == 255:
                x = x + 1
            else:
                y = y + 1
        if x == 0:
            print(x, y, i)

    print('/n')
    for i in range(w):
        x, y = 0, 0
        for j in range(h):
            if a[j][i] == 255:
                x = x + 1
            else:
                y = y + 1
        if x == 0:
            print(x, y, i)
    # cv2.CascadeClassifier()E
    cv2.imshow("123", b)
    cv2.waitKey(0)
