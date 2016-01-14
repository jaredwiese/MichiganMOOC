fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = dict()
list = []
for line in fh:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        try :
            list.append(words[1])
        except:
            continue
        continue
    else:
        continue
#print list
for name in list:
    count[name] = count.get(name,0) + 1
#print count
maxval = None
maxkee = None
for kee,val in count.items():
    if maxval == None : maxval = val
    if maxval < val :
        maxval = val
        maxkee = kee
        
print maxkee, maxval
