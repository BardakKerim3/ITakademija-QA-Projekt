
from selenium import webdriver 
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ChromeOptions

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notification")

driver = webdriver.Chrome (options = option)

driver.get("https://puppies-closet.com/evidencija/login.php")


time.sleep(5)

poljeI = driver.find_element(By.NAME,"username")
poljeI.send_keys("luk")

poljeL = driver.find_element(By.NAME,"password")
poljeL.send_keys("kerim1")

dugmeP = driver.find_element(By.NAME,"login")
dugmeP.click()

time.sleep(4)

dugmeSlijedeca = driver.find_element(By.CLASS_NAME, "btnPage")
dugmeSlijedeca.click()


time.sleep(3)   
    

brisanjePodataka = driver.find_element(By. CSS_SELECTOR,"#results > div > table > tbody > tr:nth-child(11) > td:nth-child(8) > button.button.red" )

brisanjePodataka.click()

odabir = driver.find_element(By.ID,"del")

odabir.click()

time.sleep(3)

odjava = driver.find_element(By.CLASS_NAME,"logout")
odjava.click()
time.sleep(4)