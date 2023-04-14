
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

babic = webdriver.Chrome (options = option)

babic.get("https://puppies-closet.com/evidencija/login.php")


time.sleep(3)
poljeI = babic.find_element(By.NAME,"username")
poljeI.send_keys("luk")

poljeL = babic.find_element(By.NAME,"password")
poljeL.send_keys("kerim1")

dugmeP = babic.find_element(By.NAME,"login")
dugmeP.click()


padajuciMeni = babic.find_elements_by_name("Oprema")
trazenaRijec = "OPREMA"

for rijec in padajuciMeni:

    v = rijec.text.upper() 
    
    if trazenaRijec in v:
        print(rijec.text)
        rijec.click()
        break
    time.sleep(4)
"""
time.sleep(2)

padajuciMeni = babic.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(2) > a")
padajuciMeni.click()
time.sleep(5)
"""
unosPoInverturnomBr = babic.find_element(By.CLASS_NAME, "search")
unosPoInverturnomBr.send_keys(99)


time.sleep(3)
Pretraga = babic.find_element(By.CLASS_NAME,"button.blue")
Pretraga.click()
time.sleep(5)

dugmeBrisanjeOpreme = babic.find_element(By.CLASS_NAME,"button.red")
dugmeBrisanjeOpreme.click()
time.sleep(4)

prvoPolje = babic.find_element(By.ID,"del")
prvoPolje.click()

time.sleep(4)

drugoPolje = babic.find_element(By.CLASS_NAME,"logout")
drugoPolje.click()

time.sleep(3)




