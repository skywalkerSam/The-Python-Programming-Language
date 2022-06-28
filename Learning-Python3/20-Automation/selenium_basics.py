
from time import sleep
from selenium import webdriver


browser = webdriver.Chrome(r"C:\Users\samsk\Downloads\chromedriver_win32\chromedriver.exe")
browser.get('https://skywalkersam.github.io')
browser.maximize_window()
sleep(180)

browser.close()     # Close the browser window
browser.quit()      # Quit the browser

