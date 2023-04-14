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
usernamePolje = driver.find_element(By.NAME, "username")
passwordPolje = driver.find_element(By.NAME, "password")


usernamePolje.send_keys("kerimbardak")
passwordPolje.send_keys("kerimbardak123")


dugmePrijava = driver.find_element(By.NAME,"login")
dugmePrijava.click()        
time.sleep(3)

"""
menuIzvjestaji = driver.find_elements_by_tag_name("li")
trazenaRijec = "OPREMA"

i = 0
found = False

while not found and i < len(menuIzvjestaji):
    rijec = menuIzvjestaji[i]
    v = rijec.text.upper()
    
    if trazenaRijec in v:
        print(rijec.text)
        rijec.click()
        found = True
    else:
        i += 1
        time.sleep(4)



"""
menuIzvjestaji = driver.find_elements_by_tag_name("li")
trazenaRijec = "OPREMA"

for rijec in menuIzvjestaji:

    v = rijec.text.upper() 
    
    if trazenaRijec in v:
        print(rijec.text)
        rijec.click()
        break
    time.sleep(4)


odaberTipaOpreme = Select(driver.find_element_by_id("type_id"))

options = odaberTipaOpreme.options


for option in options:
    if option.text == "Monitor":
        option.click()
        break

time.sleep(6)

proizvodjacOpreme = Select(driver.find_element_by_id("producer_id"))


trazeniProizvodjac = "Dell"


for proizvodjac in proizvodjacOpreme.options:
    if trazeniProizvodjac.lower() in proizvodjac.text.lower():
        proizvodjac.click()
        break

time.sleep(6)

inverturniBroj = driver.find_element(By.NAME,"inventoryNumber")
serijskiBroj = driver.find_element(By.NAME,"serialNumber")

inverturniBroj.send_keys("11111111116666666111111111")
serijskiBroj.send_keys("09090909090990")
time.sleep(4)


dugmeSacuvaj = driver.find_element(By.NAME,"save")
dugmeSacuvaj.click()
time.sleep(3)