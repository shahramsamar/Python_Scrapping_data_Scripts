from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.com")

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("علی بیگدلی")
elem.send_keys(Keys.ENTER)

result = driver.find_element(By.ID, "search")
html_src = driver.page_source

soup = BeautifulSoup(html_src, "html.parser")

links = soup.find_all("a")
cites = soup.find_all("cite")

for tag in cites:
    if tag.text == "https://thealibigdeli.ir":
        print(tag)

target = driver.find_element(
    By.XPATH, '//*[@id="rso"]/div[3]/div/div/div/div[1]/div/div/span/a/h3/span'
)
target.click()

full_name_elem = driver.find_element(By.NAME, "name").send_keys("str")
driver.find_element(
    By.XPATH, '//*[@id="rso"]/div[3]/div/div/div/div[1]/div/div/span/a/h3/span'
).click()
