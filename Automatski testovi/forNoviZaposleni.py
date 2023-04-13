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

driver = webdriver.Chrome (options = option, executable_path = "C:\\Users\\KBard\\OneDrive\\Radna površina\\GitHub testovi\\ITakademija-QA-Projekt\\Automatski testovi\\chromedriver.exe" )

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
poljeEmail.send_keys("salkosalkicxxx@gmail.com") 

PoljePhone = driver.find_element(By.NAME,"phone")
PoljePhone.send_keys("+387 61 542 500") 

time.sleep(4)
padajucimeni = Select(driver.find_element_by_id("office_id"))
trazenaKancelarija = "amer"

for kancelarija in padajucimeni.options:
    if trazenaKancelarija.lower() in kancelarija.text.lower():
        kancelarija.click()
        break

time.sleep(5)

padajucimeni2 = Select(driver.find_element_by_name("organization_id"))
trazenaRijec = "plava"

for rijec in padajucimeni2.options:
    if trazenaRijec.lower() in rijec.text.lower():
        rijec.click()
        break
time.sleep(4)



dugmeSave = driver.find_element(By.NAME, "save")
dugmeSave.click()


time.sleep(2)







