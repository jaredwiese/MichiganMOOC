import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_168898.xml'

url = serviceurl
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
   
tree = ET.fromstring(data)

results = tree.findall('.//count')

counts = len(results)
total = 0
for n in results:
    total += int(n.text)
print 'Count: ', counts
print 'Sum: ', total
