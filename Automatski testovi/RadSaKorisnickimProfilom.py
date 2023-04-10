
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

babic = webdriver.Chrome (options = opcijeZaPokretanje, executable_path = "C:\\Users\\KBard\\OneDrive\\Radna površina\\GitHub testovi\\ITakademija-QA-Projekt\\GitHub-Automatski-testovi\\chromedriver.exe")

babic.get("https://puppies-closet.com/evidencija/login.php")
time.sleep(3)
poljeI = babic.find_element(By.NAME,"username")
poljeI.send_keys("kerimbardak")

poljeL = babic.find_element(By.NAME,"password")
poljeL.send_keys("kerimbardak123")

dugmeP = babic.find_element(By.NAME,"login")
dugmeP.click()


time.sleep(2)

padajuciMeni = babic.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(6)")

""""
dropdown = babic.find_element(By.CLASS_NAME, "main-navigation")
dropdown.click()
select = Select(dropdown)
select.select_by_index(6)
"""
dugmeA = babic.find_element(By.XPATH, "/html/body/div/header/nav/ul[1]/li[6]/a")
dugmeA.click()

time.sleep(5)

korisnikIme = cevap.find_element(By.NAME,"firstname")
korisnikIme.send_keys("poli")

korisnikPrezime = cevap.find_element(By.NAME,"lastname")
korisnikPrezime.send_keys("moli")

time.sleep(4)

korisnickoIme = cevap.find_element_by_xpath ("/html/body/div/div[1]/form/input[3]")
korisnickoIme.send_keys("cevapevoli")


korisnickalozinka = cevap.find_element_by_xpath ("/html/body/div/div[1]/form/input[4]")
korisnickalozinka.send_keys("izvoli")

time.sleep(5)

grupaKorisnik = cevap.find_element(By.XPATH,"/html/body/div/div[1]/form/select/option[3]")
grupaKorisnik.click()

time.sleep(4)

spremiKorisnika = cevap.find_element(By.XPATH,"/html/body/div/div[1]/form/input[5]")
spremiKorisnika.click()


odjaviSe = cevap.find_element(By.XPATH,"/html/body/div/header/nav/ul[2]/li/a")
odjaviSe.click()

time.sleep(5)




