from selenium import webdriver 
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notification")

driver = webdriver.Chrome (options = option, executable_path = "C:\\Users\\KBard\\OneDrive\\Radna površina\\GitHub testovi\\ITakademija-QA-Projekt\\GitHub-Automatski-testovi\\chromedriver.exe")

driver.get("https://puppies-closet.com/evidencija/login.php")
time.sleep(3)
poljeI = driver.find_element(By.NAME,"username")
poljeI.send_keys("kerimbardak")

poljeL = driver.find_element(By.NAME,"password")
poljeL.send_keys("kerimbardak123")

dugmeP = driver.find_element(By.NAME,"login")
dugmeP.click()


time.sleep(2)

poljeName = driver.find_element(By.NAME,"firstname")
poljeName.send_keys("Salko")

PoljeLastname = driver.find_element(By.NAME,"lastname")
PoljeLastname.send_keys("Salkić")
time.sleep(5)
poljeEmail = driver.find_element(By.NAME,"email")
poljeEmail.send_keys("salkosalkicxxx@gmail.com") # email

PoljePhone = driver.find_element(By.NAME,"phone")
PoljePhone.send_keys("+387 61 542 500") # broj telefona

time.sleep(4)
dropdown = driver.find_element(By.ID, "office_id")
dropdown.click()
select = Select(dropdown)
select.select_by_index(5)


dropdown2 = driver.find_element(By.ID,"organization_id")
dropdown2.click() # kancelarija
select = Select(dropdown2)
select.select_by_index(6)
time.sleep(3)

dugmeSave = driver.find_element(By.NAME, "save")
dugmeSave.click()


time.sleep(2)









