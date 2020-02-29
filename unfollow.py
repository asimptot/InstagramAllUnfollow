import pyautogui as pg
import time

def sure():
    pg.press('tab')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(1)

def close_window():
    pg.press('esc')
    time.sleep(3)

def open_wo_login():
    pg.press('win')
    pg.typewrite('chrome.exe')
    time.sleep(2)
    pg.press('enter')
    time.sleep(2)
    pg.typewrite('https://www.instagram.com/gizos_tekin/')
    pg.press('enter')
    time.sleep(2)
    #pg.click(334, 1058)
    #time.sleep(2)

def refresh():
    pg.click(127, 74)  # refresh
    time.sleep(8)

def unfollow_list():
    for m in range(6):
        pg.press('tab')
        time.sleep(0.5)
    pg.press('enter')
    time.sleep(5)

def unfollow_all():

    unfollower = 20

    for j in range(0, unfollower*4, 4):
        if j == 44:
            for m in range(99):
                pg.press('tab')
                time.sleep(0.25)
            pg.press('enter')
            time.sleep(1)
            sure()
        else:
            for k in range(7 + j):
                pg.press('tab')
                time.sleep(0.25)
            pg.press('enter')
            time.sleep(1)
            sure()

def main():
    open_wo_login()
    #refresh()
    unfollow_list()  # takipçi listesi
    unfollow_all()

    close_window()

main()