
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

opcijeZaPokretanje = Options()

opcijeZaPokretanje.add_argument("--disable-infobars") 
opcijeZaPokretanje.add_argument("start-maximized") 
opcijeZaPokretanje.add_argument("--disable-extensions") 
opcijeZaPokretanje.add_argument("--disable-notification")

babic = webdriver.Chrome (options = opcijeZaPokretanje, executable_path = "C:\\Users\\KBard\\OneDrive\\Radna površina\\GitHub testovi\\ITakademija-QA-Projekt\\Automatski testovi\\chromedriver.exe" )

babic.get("https://puppies-closet.com/evidencija/login.php")

time.sleep(3)
poljeI = babic.find_element(By.NAME,"username")
poljeI.send_keys("luk")

poljeL = babic.find_element(By.NAME,"password")
poljeL.send_keys("kerim1")

dugmeP = babic.find_element(By.NAME,"login")
dugmeP.click()


time.sleep(2)

padajuciMeni = babic.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(2) > a")
padajuciMeni.click()
time.sleep(5)

unosPoInverturnomBr = babic.find_element(By.CLASS_NAME, "search")
unosPoInverturnomBr.send_keys(99)

time.sleep(3)
dugmePretraga = babic.find_element(By.NAME,"equipmentSearch")
dugmePretraga.click()
time.sleep(5)

dugmeBrisanjeOpreme = babic.find_element(By.CSS_SELECTOR,"#results > div > table > tbody > tr:nth-child(2) > td:nth-child(10) > button.button.red")
dugmeBrisanjeOpreme.click()
time.sleep(4)

prvoPolje = babic.find_element(By.ID,"del")
prvoPolje.click()

time.sleep(4)

drugoPolje = babic.find_element(By.CLASS_NAME,"logout")
drugoPolje.click()

time.sleep(3)




