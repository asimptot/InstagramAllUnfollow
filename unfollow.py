from selenium import webdriver
import pyautogui
import time

def eminim():
    pyautogui.click(926, 715) #emin misiniz'e yanit
    time.sleep(2)

def login():

    pyautogui.click(1513, 214)
    time.sleep(4)
    pyautogui.click(857, 382)
    pyautogui.typewrite('en_ucuz_ucus') #enter your id
    time.sleep(2)
    pyautogui.click(905, 447)
    pyautogui.typewrite('10031144') #enter your password
    time.sleep(3)
    pyautogui.click(938, 522)
    time.sleep(5)

def unf():

    web_page_url = 'https://www.instagram.com/en_ucuz_ucus/'
    driver_path = "D:\development_group\Tests\Sosyal\Instagram\chromedriver"
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.maximize_window()
    browser.get(web_page_url)
    time.sleep(5)

    login()

    for i in range(90):
        pyautogui.click(134, 78) #refresh
        time.sleep(8)
        pyautogui.click(1115, 462) #takip listesi
        time.sleep(3)
        eminim()

        pyautogui.click(1129, 449) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1139, 519) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1128, 591) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1135, 662) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1147, 721) #unf
        time.sleep(5)
        eminim()

        pyautogui.click(1147, 793) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1147, 869) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1214, 318) #close
        time.sleep(3)
unf()



