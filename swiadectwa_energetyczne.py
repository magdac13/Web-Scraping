import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your ChromeDriver executable
PATH = "/Users/magda/Desktop/Web-Scraping/chromedriver/chromedriver"
# Create a WebDriver instance by passing the Service object
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://rejestrcheb.mrit.gov.pl/wykaz-swiadectw-charakterystyki-energetycznej-budynkow")
# print(driver.page_source)

try:
    table = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.ID, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list')
    )
                                            )
    tr = table.find_elements(By.CLASS_NAME, 'results-row')
    # print(tr.text)

    for row in tr:
        # Numer swiadectwa
        certificate = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col0'
        )
        # Data wystawienia
        date_issued = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col1'
        )
        # Wazne do
        valid_until = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col2'
        )
        # Miejscowosc of Dane podstawowe
        city = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col3'
        )
        # Ulica of Dane podstawowe
        street = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col4'
        )
        street_number = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col5'
        )
        house_number = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col6'
        )
        # województwo
        province = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col7'
        )
        # powiat
        district = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col8'
        )
        # gmina
        municipality = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col9'
        )
        # Budynek oceniany zapotrzebowanie eu of Charakterystyka energetyczna
        eu_needs = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col10'
        )
        # Budynek oceniany zapotrzebowanie ek of Charakterystyka energetyczna
        ek_needs = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col11'
        )
        # Budynek oceniany zapotrzebowanie ep of Charakterystyka energetyczna
        ep_needs = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col12'
        )
        # Udzial odnawialnych zrodel energii ek of Charakterystyka energetyczna
        renewable_energey_sources_share = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col13'
        )
        # Poziom emisji CO 2 of Charakterystyka energetyczna
        co2_emission_level = row.find_element(
            By.CLASS_NAME, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_col14'
        )

        print(street.text)


finally:
    time.sleep(120)
    driver.quit()
