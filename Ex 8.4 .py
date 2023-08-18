fname = input ('Enter file name:')
fhandle = open (fname)

wlist = []

for line in fhandle:
    words = line.split()
    for word in words:
        if word not in wlist : 
            wlist.append(word)

wlist.sort()
print (wlist)
