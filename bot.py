import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):
    subprocess.call(r'C:\\Users\capta\AppData\Roaming\Zoom\bin\Zoom.exe')

    time.sleep(5)
    
    
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    time.sleep(3)

    #starts crying over my bug here XD can't seem to type on pyautogui
    #meeting_id_btn =  pyautogui.locateCenterOnScreen('meetingIdField.png')
    #pyautogui.moveTo(meeting_id_btn)
    #pyautogui.click()
    pyautogui.typewrite(meetingid)

    media_btn = pyautogui.locateAllOnScreen('media_btn.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(3)

    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')


sign_in('88163695989','R7Ru1U')  

