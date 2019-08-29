from selenium import webdriver
from bs4 import BeautifulSoup

path = "C:\\Users\\komeh\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://onoffmix.com/')
search_box = driver.find_element_by_name("s")
search_box.send_keys("밋업")
search_box.submit()
driver.find_element_by_xpath('//*[@id="content"]/div/section[2]/div[1]/ul[1]/li[2]/a').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_divs = soup.find_all("h5.title.ellipsis")
print(all_divs)

#notices = soup.select('#content > div > section.event_main_area > ul > li > article.event_area.event_main > a')
#for n in notices:
#    print(n.text)