import requests
from bs4 import BeautifulSoup

r = requests.get('https://dvdprime.com/g2/bbs/board.php?bo_table=comm&r=ok')
html = r.content

soup = BeautifulSoup(html, 'html.parser')
titles_html = soup.select('.list_subject_span_pc')

for i in range(len(titles_html)):
    print(i+1, titles_html[i].text)

