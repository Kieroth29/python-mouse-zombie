import pyautogui as pag
from random import randint
import time

while True:
    x = randint(600,700)
    y = randint(200,600)
    pag.moveTo(x, y, 0.5)
    time.sleep(2)