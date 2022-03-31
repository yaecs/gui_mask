import cv2
from cv2 import inRange

def process_img(img, name, color):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(hsv_img, color[0], color[1])
    cv2.imshow('mask ' + name, img_mask)
#функция обработки при изменени ползунков
def update(value=0):
    color_low = (
        cv2.getTrackbarPos('h_min', 'ui'),
        cv2.getTrackbarPos('s_min', 'ui'),
        cv2.getTrackbarPos('v_min', 'ui')
    )
    color_high = (
        cv2.getTrackbarPos('h_min', 'ui'),
        cv2.getTrackbarPos('s_min', 'ui'),
        cv2.getTrackbarPos('v_min', 'ui')
    )
    color = (color_low, color_high)
    process_img(img, 'img', color)
    process_img(rainbow, 'img', color)

#код, непосредственно выполняющийся при запуске
img = cv2.imread('imgs/aquarium.jpg')
rainbow = cv2.imread('imgs/rainbow.jpg')

cv2.namedWindow('ui')
cv2.createTrackbar('h_min', 'ui', 0, 180, update)
cv2.createTrackbar('s_min', 'ui', 0, 255, update)
cv2.createTrackbar('v_min', 'ui', 0, 180, update)
cv2.createTrackbar('h_max', 'ui', 180, 180, update)
cv2.createTrackbar('s_max', 'ui', 255, 255, update)
cv2.createTrackbar('v_max', 'ui', 255, 255, update)
cv2.imshow('ui', img)
update()

cv2.waitKey(0)
