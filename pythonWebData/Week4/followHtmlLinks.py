from bs4 import BeautifulSoup
import urllib
import ssl

#url = raw_input('Input URL: ')
url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Ekhlass.html'

#position = int(raw_input('What link do you want me to follow? '))
position = 18
#count = int(raw_input('How many times do I follow this link? '))
count = 7

name = ''

# This function grabs the Nth link object from the requested url.
# To be safe, I should be making sure the Nth link exists (I didn't here)
def getNthLink(url, n):
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup('a')
    return tags[n - 1]

# This iterates 'count' times, each time grabbing the 'position' 
# link object. For clarity, it prints the url each time.
for i in range(count):
    tag = getNthLink(url, position)
    url = tag.get('href')
    print 'Retrieving ', url
    
# Finally after 'count' times we grab the content from the last tag
name = tag.contents[0]
print name
