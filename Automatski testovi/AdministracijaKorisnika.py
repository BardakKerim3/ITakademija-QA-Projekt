from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


opcijeZaPokretanje = Options()

opcijeZaPokretanje.add_argument("--disable-infobars") 
opcijeZaPokretanje.add_argument("start-maximized") 
opcijeZaPokretanje.add_argument("--disable-extensions") 
opcijeZaPokretanje.add_argument("--disable-notification")

oko = webdriver.Chrome (options = opcijeZaPokretanje, executable_path = "chromedriver.exe" )

oko.get("https://puppies-closet.com/evidencija/login.php")

time.sleep(4)

imeKorisnika = oko.find_element(By.NAME,"username")
sifraKorisnika = oko.find_element(By.NAME,"password")

imeKorisnika.send_keys("kerimbardak")
sifraKorisnika.send_keys("kerimbardak123")

dugmePrijava = oko.find_element(By.NAME,"login")
dugmePrijava.click()

time.sleep(5)
menuIzvjestaji = oko.find_element_by_tag_name("li")
trazenaRijec = "Administracija korisnika"

i = 0
found = False

while not found and i < len(menuIzvjestaji):
    rijec = menuIzvjestaji[i]
    v = rijec.text.lower()

    if trazenaRijec in v:
        print(rijec.text)
        rijec.click
        found = True
    else:
        i+= 1
        time.sleep(5)
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

administracijaKorisnika = oko.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(6) > a")

administracijaKorisnika.click()

time.sleep(4)
"""
dugmePromjenaLozinke = oko.find_element(By.CSS_SELECTOR,"#wrapper > div.section-two > div > table > tbody > tr:nth-child(2) > td:nth-child(6) > button.button.blue")
dugmePromjenaLozinke.click()

time.sleep(6)

poljeZaIzmjenuLozinke = oko.find_element(By.NAME,"password")
poljeZaIzmjenuLozinke.send_keys("kerimbardak123")

time.sleep(4)

dugmeSacuvaj = oko.find_element(By.NAME,"updateUserPassword")
dugmeSacuvaj.click()

time.sleep(3)

dugmeZaOdjavu = oko.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul.logout > li > a")
dugmeZaOdjavu.click()

time.sleep(6)