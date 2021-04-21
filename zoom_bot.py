#I'll keep my libaries here 
import datetime
import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# didn't work with pyautogui so tried a new way
#second try -_- 
#here we go

class zoom_bot:
	def join(self,meeting_link):
		self.bot = webdriver.Chrome("chromedriver.exe")
		self.bot.get(meeting_link)
		time.sleep(3)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("enter", do_press=True, do_release=True)
		time.sleep(10)

		self.bot.quit()

link = open("meeting_link.txt","r").read()

bot = zoom_bot()
bot.join(link)

