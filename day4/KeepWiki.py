import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://en.wikipedia.org/w/index.php?search="
url1 = "&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
wiki = "https://en.wikipedia.org/wiki/"

input = "guitar"
input = input.replace(' ', '+')
page = url + input + url1
html = urllib.request.urlopen(page, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
headings = soup.find(id="mw-content-text")
results = headings.find_all("div", class_="mw-search-result-heading")
link = results[0]('a')[0].text.strip()
link = wiki + link.replace(' ', '_')

html = urllib.request.urlopen(link, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
pages = soup.find_all("div", class_="hatnote")
lables = soup.find_all("th", class_="infobox-label")
data = soup.find_all("td", class_="infobox-data")

for l, d in zip(lables, data):
  print(l.text + ": " + d.text)

para = soup.find_all("p")

num = 0
for p in para:
  print (p.text)
  num = num + 1
  if num == 5:
    break

see_also = soup.find(id='See_also')
see_also = see_also.parent.next_sibling.next('li')
print("More Detailed search will include: ")
for sa in see_also:
  print(sa.text)
print("\n")

for page in pages:
  page = page('a')[0].text.strip().replace(' ', '_')
  page = wiki + page
  print(page)
