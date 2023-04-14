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


time.sleep(4)

imeKorisnika = driver.find_element(By.NAME,"username")
sifraKorisnika = driver.find_element(By.NAME,"password")

imeKorisnika.send_keys("kerimbardak")
sifraKorisnika.send_keys("kerimbardak123")

dugmePrijava = driver.find_element(By.NAME,"login")
dugmePrijava.click()

time.sleep(5)


menuIzvjestaji = driver.find_elements(By.TAG_NAME,"li")
trazenaRijec = "ADMINISTRACIJA KORISNIKA"

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

listaKorisnika = driver.find_elements(By.ID,"wrapper")
trazenaRijec2 = "promijena lozinke"
for x in listaKorisnika:
    korisnici = driver.find_elements(By.CLASS_NAME,"section-two")
    print(korisnici)
    if trazenaRijec2 in korisnici:
        dugmePromjenaLozinke = x.find_element(By.CSS_SELECTOR,"Promjena lozinke")
        dugmePromjenaLozinke[0].click()
        
        break
time.sleep(4)

for item in menuIzvjestaji:
    if item.text.upper() == "ADMINISTRACIJA KORISNIKA":
        item.click()
        break
    time.sleep(4)





# Click on the "Promijena lozinke" link for the user that matches the given criteria

listaKorisnika = driver.find_elements(By.CLASS_NAME, "section-two")
name2 = "promijena lozinke"
target_user = None
for user in listaKorisnika:
    if name2 in user.text.lower():
        target_user = user
        if target_user is not None:
            name2 = target_user.find_element(By.CSS_SELECTOR, "button.button.blue")
            target_user.click()
            break
time.sleep(4)



listaKorisnika = driver.find_elements(By.CLASS_NAME,value = "section-two" )
trazenaRijec2 = "promijena lozinke"

for x in listaKorisnika:
    korisnici = x.find_elements_by_class_name("table users")
    if trazenaRijec2 in x.text:
        dugmePromjenaLozinke = x.find_element_by_link_text("Promijena lozinke")
        dugmePromjenaLozinke.click()
        break

time.sleep(4)





"""
"""
buttons = driver.find_elements_by_css_selector(".button.blue")

for button in buttons:
    button == driver.find_element_by_css_selector ("button.blue" )
    button.click()
    time.sleep(4)
novaLozinka = driver.find_element_by_css_selector("input[type=password]:nth-child(1)")
novaLozinka.send_keys("2222222")

time.sleep(4)

novaLozinka = driver.find_element_by_name("password")
password = "2y$10$N2fizJFyHqRvHsFVNncXeOyaQORy4FyZMpt7N8wfGUmZZtJlikwYm"

for char in password:
    print(char)



for value in novaLozinka:
    value == "2y$10$N2fizJFyHqRvHsFVNncXeOyaQORy4FyZMpt7N8wfGUmZZtJlikwYm"
    print (value.text)
    break
time.sleep(4)
"""