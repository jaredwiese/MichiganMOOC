import re
#fname = 'regex_sum_168896.txt'
fname = 'regex_sum_42.txt'
fh = open(fname, 'r')
x = []
count = 0

for line in fh:
    x = re.findall('[0-9]+', line)
    nums = [x]
    if x == []:
        continue
    count += sum([int(i) for i in x])
print count
