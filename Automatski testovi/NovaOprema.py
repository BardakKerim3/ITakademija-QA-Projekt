
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
poljeI.send_keys("kerimbardak")

poljeL = babic.find_element(By.NAME,"password")
poljeL.send_keys("kerimbardak123")

dugmeP = babic.find_element(By.NAME,"login")
dugmeP.click()

time.sleep(4)

padajuciMeni = babic.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(2) > a")

padajuciMeni.click()



time.sleep(4)
dropdown = babic.find_element(By.ID, 'type_id')
dropdown.click()
select = Select(dropdown)
select.select_by_index(8)

time.sleep(4)

dropdown = Select(babic.find_element_by_id('producer_id'))
dropdown.select_by_index(4)
time.sleep(2)

brojInventurni = babic.find_element(By.NAME, "inventoryNumber")
brojInventurni.send_keys("667776666767")


brojSerijski = babic.find_element(By.NAME, "serialNumber")
brojSerijski.send_keys("9989989999")

time.sleep(3)

dugmeSpremi = babic.find_element(By.NAME, "save")
dugmeSpremi.click()

time.sleep(4)

