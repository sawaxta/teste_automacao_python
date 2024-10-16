import time
import pyautogui as pg

time.sleep(5)
x, y = pg.position()
print(f"Posição do mouse: x={x}, y={y}")

