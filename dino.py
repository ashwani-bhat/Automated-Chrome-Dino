import pyautogui as pg
from PIL import ImageGrab
import time


def hit(key):
    pg.keyDown(key)
    return

# change the pixel locations according to the position on the screens
def createStrip(image):
    # for cactus
    for i in range(355, 405):
        for j in range(380, 435):
            if image[i, j] > 100:   # white pixels
                hit('up')
                return
    # for birds 
    for i in range(320, 370):
        for j in range(300, 355):
            if image[i, j] > 100:   # white pixels
                hit('down')
                return
    return

def createScreenShot():
    image = ImageGrab.grab().convert('L')
    return image


if __name__ == '__main__':
    time.sleep(3)
    while True:
        image = createScreenShot()
        data = image.load()
        createStrip(data)
