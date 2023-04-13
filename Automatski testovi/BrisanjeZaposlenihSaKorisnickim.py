from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notification")
sreca = webdriver.Chrome (options = option, executable_path = "C:\\Users\\KBard\\OneDrive\\Radna površina\\GitHub testovi\\ITakademija-QA-Projekt\\Automatski testovi\\chromedriver.exe" )

sreca.get("https://puppies-closet.com/evidencija/login.php")

time.sleep(5)

poljeI = sreca.find_element(By.NAME,"username")
poljeI.send_keys("luk")

poljeL = sreca.find_element(By.NAME,"password")
poljeL.send_keys("kerim1")

dugmeP = sreca.find_element(By.NAME,"login")
dugmeP.click()

time.sleep(4)

dugmeSlijedeca = sreca.find_element(By.CLASS_NAME, "btnPage")
dugmeSlijedeca.click()


time.sleep(3)   
    

brisanjePodataka = sreca.find_element(By. CSS_SELECTOR,"#results > div > table > tbody > tr:nth-child(11) > td:nth-child(8) > button.button.red" )

brisanjePodataka.click()

odabir = sreca.find_element(By.ID,"del")

odabir.click()

time.sleep(3)

odjava = sreca.find_element(By.CLASS_NAME,"logout")
odjava.click()
time.sleep(4)