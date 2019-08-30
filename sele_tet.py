from selenium import webdriver
from bs4 import BeautifulSoup

path = "C:\\Users\\komeh\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://m.onoffmix.com/event/main?s=%EB%B0%8B%EC%97%85')

html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')
all_divs = soup.find_all('h1', {"class": "event_title"})
for title in all_divs:
    print(title.get_text())
