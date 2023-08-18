score = input('Enter Score:')   
#test score as numeric input

try:
    s = float(score)
except: 
    s = -1

if 0 <= s <= 1:
    if s >= 0.9:
        print ('A') 
    elif s >= 0.8:
        print ('B')
    elif s >= 0.7:
        print ('C')
    elif s >= 0.6:
        print ('D')
    elif 0 < s < 0.6:
        print ('F')
else:
    print ('Error. Score needs to be between 0.0 and 1.0.')
