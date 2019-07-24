

from selenium import webdriver
import pyautogui
import time
import random

run = True

video_link = input('[BOT][LINK] Hello there, please enter the video you want to bot: ')
browser = webdriver.Chrome('C:\webdrivers\ChromeDriver')
while run:

    rand = random.randint(10, 20)

    browser.get(video_link)
    time.sleep(rand)
    pyautogui.press('ctrl')
    pyautogui.press('r')
repeat()