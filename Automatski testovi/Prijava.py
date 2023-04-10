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

driver = webdriver.Chrome (options = opcijeZaPokretanje, executable_path = "C:\\Users\\KBard\\OneDrive\\Radna površina\\GitHub testovi\\ITakademija-QA-Projekt\\Automatski testovi\\chromedriver.exe" )

driver.get("https://puppies-closet.com/evidencija/login.php")
time.sleep(3)
poljeI = driver.find_element(By.NAME,"username")
poljeI.send_keys("kerimbardak")

poljeL = driver.find_element(By.NAME,"password")
poljeL.send_keys("kerimbardak123")

dugmeP = driver.find_element(By.NAME,"login")
dugmeP.click()

time.sleep(4)