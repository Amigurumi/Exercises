fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    ul = line.upper(). rstrip()
    print (ul)