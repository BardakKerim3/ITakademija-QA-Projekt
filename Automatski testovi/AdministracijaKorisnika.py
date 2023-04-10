from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opcijeZaPokretanje = Options()

opcijeZaPokretanje.add_argument("--disable-infobars") 
opcijeZaPokretanje.add_argument("start-maximized") 
opcijeZaPokretanje.add_argument("--disable-extensions") 
opcijeZaPokretanje.add_argument("--disable-notification")

oko = webdriver.Chrome (options = opcijeZaPokretanje, executable_path="drajveri/chromedriver.exe")

oko.get("https://puppies-closet.com/evidencija/login.php")

time.sleep(4)

imeKorisnika = oko.find_element_by_xpath ("/html/body/div/form/div/div[2]/input[1]")
sifraKorisnika = oko.find_element_by_xpath("/html/body/div/form/div/div[2]/input[2]")

imeKorisnika.send_keys("kerimbardak")
sifraKorisnika.send_keys("kerimbardak123")

dugmePrijava = oko.find_element_by_xpath("/html/body/div/form/div/div[2]/input[3]")
dugmePrijava.click()

time.sleep(5)

administracijaKorisnika = oko.find_element(By.XPATH,"/html/body/div/header/nav/ul[1]/li[6]/a")
administracijaKorisnika.click()

time.sleep(4)

dugmePromjenaLozinke = oko.find_element(By.XPATH,"/html/body/div/div[2]/div/table/tbody/tr[50]/td[6]/button[2]")
dugmePromjenaLozinke.click()

time.sleep(6)

poljeZaIzmjenuLozinke = oko.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/form/input[1]")
poljeZaIzmjenuLozinke.send_keys("promjenije")

time.sleep(4)

dugmeSacuvaj = oko.find_element(By.XPATH,"/html/body/div/div[4]/div/div/div[2]/div/form/input[2]")
dugmeSacuvaj.click()

time.sleep(3)

dugmeZaOdjavu = oko.find_element(By.XPATH,"/html/body/div/header/nav/ul[2]/li/a")
dugmeZaOdjavu.click()

time.sleep(6)