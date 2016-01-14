# Use words.txt as the file name
fname = raw_input("Enter file name: ")

try:
    fhand= open(fname) # handling the file
except:
    print "Invalid filename"
    exit()
    
phand = fhand.read().strip()

print phand.upper()
