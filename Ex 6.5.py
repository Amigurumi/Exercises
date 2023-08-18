text = "X-DSPAM-Confidence:    0.8475"
tlist = text.split(':')
num = float (tlist[1].lstrip())
print (num)  
