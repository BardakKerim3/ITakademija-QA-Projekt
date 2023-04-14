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


poljeI = driver.find_element(By.NAME,"username")
poljeI.send_keys("kerimbardak")

poljeL = driver.find_element(By.NAME,"password")
poljeL.send_keys("kerimbardak123")

dugmeP = driver.find_element(By.NAME,"login")
dugmeP.click()

time.sleep(4)


opcija = driver.find_element(By.CSS_SELECTOR, "#wrapper > header > nav > ul:nth-child(1) > li:nth-child(3) > a")

opcija.click()
time.sleep(5)

dugmeIzvjestaj = driver.find_element(By.NAME, "orgReport")

dugmeIzvjestaj.click()

time.sleep(5)