import json
import urllib

serviceurl = 'http://python-data.dr-chuck.net/comments_168902.json'

print 'Retrieving', serviceurl

uh = urllib.urlopen(serviceurl)
data = uh.read()

print 'Retrieved',len(data),'characters'
info = json.loads(data)
print 'Count:', len(info['comments'])
total = 0
for item in info['comments']:
    total += item['count']

print 'Sum:', total
