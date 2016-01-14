name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
lst = []

for line in handle:
    words = line.split()
    if len(words) !=0 and words[0] == 'From':
        try :
            hour = words[5].split(':')
            lst.append(hour[0])
        except:
            continue
        continue
    else:
        continue
        
for hour in lst:
    count[hour] = count.get(hour,0) + 1

    
tmp = list()
for k, v in count.items():
    tmp.append( (k,v) )
    
tmp = sorted( [ (v,k) for v,k in tmp ] )

for v,k in tmp:
    print v,k
