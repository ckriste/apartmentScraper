import urllib.request
from bs4 import BeautifulSoup


url = "http://www.maac.com/texas/dallas"

request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()

fo = open("urls.txt", "w+")


#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(html, "lxml")
#get the HTML of the table called site Table where all the links are displayed
main_table = soup.find("div",attrs={'class':'filtered-results'})
#Now we go into main_table and get every a element in it which has a class "title"
results = main_table.find_all('h5')

for h5 in results:
    fo.write(h5.find('a').attrs['href'])
    fo.write("\n")

fo.close()
