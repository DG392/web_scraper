import requestst__
from bs4 import BeautifulSoup

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')

for link in links:
    print(link['href'])