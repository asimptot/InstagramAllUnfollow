import pyautogui as pg
import time

def sure():
    pg.press('tab')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(2)

def open_wo_login():
    pg.click(333, 752)
    time.sleep(2)

def refresh():
    pg.click(86, 49)  # refresh
    time.sleep(8)


def follow_list():
    for m in range(7):
        pg.press('tab')
        time.sleep(0.5)
    pg.press('enter')
    time.sleep(5)


def unfollow_all():
    for j in range(0, 1000, 4):
        if j == 44:
            for m in range(99):
                pg.press('tab')
                time.sleep(0.25)
            pg.press('enter')
            time.sleep(5)
            sure()
        else:
            for k in range(7 + j):
                pg.press('tab')
                time.sleep(0.25)
            pg.press('enter')
            time.sleep(5)
            sure()

def main():
    open_wo_login()
    refresh()
    follow_list()  # takipçi listesi
    unfollow_all()

    pg.click(860, 238)  # close
    time.sleep(3)


main()
