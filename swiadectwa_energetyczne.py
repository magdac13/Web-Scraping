import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Set the path to your ChromeDriver executable
PATH = "/Users/magda/Desktop/Web-Scraping/chromedriver/chromedriver"
# Create a WebDriver instance by passing the Service object
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://rejestrcheb.mrit.gov.pl/wykaz-swiadectw-charakterystyki-energetycznej-budynkow")
# print(driver.page_source)
certificate = driver.find_element(By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__tipable')
print(certificate.text)

time.sleep(100000000)
driver.quit()
