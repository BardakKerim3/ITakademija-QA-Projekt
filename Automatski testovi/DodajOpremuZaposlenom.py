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

time.sleep(3)

poljeI = driver.find_element(By.NAME,"username")
poljeI.send_keys("kerimbardak")

poljeL = driver.find_element(By.NAME,"password")
poljeL.send_keys("kerimbardak123")

dugmeP = driver.find_element(By.NAME,"login")
dugmeP.click()

time.sleep(4)

padajuciMeni = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(2) > a")

padajuciMeni.click()


time.sleep(4)
meni = driver.find_element(By.ID, 'type_id')
meni.click()
select = Select(meni)
select.select_by_index(2)

time.sleep(4)

meni = Select(driver.find_element_by_id('producer_id'))
meni.select_by_index(2)
time.sleep(2)

brojInventurni = driver.find_element(By.NAME, "inventoryNumber")
brojInventurni.send_keys("1373635343")


brojSerijski = driver.find_element(By.NAME, "serialNumber")
brojSerijski.send_keys("18171615141")

time.sleep(3)

dugmeSpremi = driver.find_element(By.NAME, "save")
dugmeSpremi.click()

time.sleep(4)

