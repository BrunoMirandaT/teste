from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")

    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    results = driver.find_elements(By.TAG_NAME, 'cite')

    for result in results:
        if "https://www.python.org" in result.text:
            print("Teste passou: A página oficial do Python foi encontrada nos resultados de pesquisa.")
            break
        else:
            print("A página oficial do Python não foi encontrada nos resultados de pesquisa.")

finally:
    driver.quit()