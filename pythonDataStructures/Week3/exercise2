# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1
    #print count
    pos = line.find(":")
    num = line[pos + 1:]
    total += float(num.strip())
    #print total

avg = float(total / count)
    
print "Average spam confidence:", avg
