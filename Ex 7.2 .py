file = input ('Enter file name:')
fname = open(file)

total = 0 
count = 0

for line in fname:
    if line.startswith('X-DSPAM-Confidence:'):
        sws = line.split(':')
        num = float(sws[1].lstrip())
        total = total + num
        count = count + 1
    
print ('Average spam confidence:', total/count)