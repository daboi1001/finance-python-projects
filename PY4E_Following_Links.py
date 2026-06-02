from bs4 import BeautifulSoup
import re
import urllib.request, urllib.parse, urllib.error
position = int(input("what position:"))
iteration = int(input("how many times:"))-1
url = "http://py4e-data.dr-chuck.net/known_by_Queenie.html"
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
tags = soup('a')
#print(tags)
x=tags[position-1]
print(x)
url = (x.get('href', None))
match = (re.search(r">([a-z]+)<", str(x)))
if match:
    print(match.group(1))


while iteration > 0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    x=tags[position-1]
    print(x)
    url = (x.get('href', None))
    match = (re.search(r">([^<>]+)<", str(x)))
    if match:
        print(match.group(1))
    if iteration == 1:
        lastName = match.group(1)
    iteration = iteration - 1


print("Your last name is: " + lastName)

