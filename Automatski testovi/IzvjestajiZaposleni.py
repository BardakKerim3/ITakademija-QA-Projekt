from selenium import webdriver 
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()

option.add_argument("--disable-infobars") # gasi info barove
option.add_argument("start-maximized") # govori Chromu da se pokrene preko cijelog ekrana
option.add_argument("--disable-extensions") # u tom Chromu, isključuje ekstenzije (ako imaš instaliranih)
option.add_argument("--disable-notification") # isključuje i notifikacije

driver = webdriver.Chrome (options = option, executable_path = "C:\\Users\\KBard\\OneDrive\\Radna površina\\GitHub testovi\\ITakademija-QA-Projekt\\GitHub-Automatski-testovi\\chromedriver.exe")


driver.get("https://puppies-closet.com/evidencija/login.php")

time.sleep(5)
usernamePolje = driver.find_element(By.NAME, "username")
passwordPolje = driver.find_element(By.NAME, "password")


usernamePolje.send_keys("kerimbardak")
passwordPolje.send_keys("kerimbardak123")


dugmePrijava = driver.find_element(By.NAME,"login")
dugmePrijava.click()        
time.sleep(5)


menuIzvjestaji = driver.find_element(By.CSS_SELECTOR, "#wrapper > header > nav > ul:nth-child(1) > li:nth-child(3) > a")

menuIzvjestaji.click()

time.sleep(5)


opcija = driver.find_element(By.NAME, "empReport")
opcija.click()


time.sleep(5)