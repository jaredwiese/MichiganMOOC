fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        try :
            print words[1]
            count += 1
        except:
            print 'No Data at Element at index-sub 2'
            continue
        continue
    else:
        continue

print "There were", count, "lines in the file with From as the first word"
