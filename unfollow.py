from selenium import webdriver
import pyautogui
import time

def eminim():
    pyautogui.click(926, 715) #emin misiniz'e yanit
    time.sleep(3)

def login():

    pyautogui.click(1513, 214)
    time.sleep(4)
    pyautogui.click(857, 382)
    pyautogui.typewrite('hotelizm') #enter your id
    time.sleep(2)
    pyautogui.click(905, 447)
    pyautogui.typewrite('zapzulukum38') #enter your password
    time.sleep(3)
    pyautogui.click(938, 522)
    time.sleep(5)

def open_wo_login():
    pyautogui.click(333, 1051)

def unf():

    web_page_url = 'https://www.instagram.com/hotelizm/'
    driver_path = "D:\Projects\Sosyal\Instagram\chromedriver"
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.maximize_window()
    #browser.get(web_page_url)
    time.sleep(5)

    #login()
    open_wo_login()

    for i in range(90):
        pyautogui.click(134, 78) #refresh
        time.sleep(8)
        pyautogui.click(1079, 463) #takip listesi
        time.sleep(5)

        pyautogui.click(1148, 452) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1148, 519) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1148, 591) #unf
        time.sleep(3)
        eminim()

        pyautogui.click(1148, 662) #unf
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



