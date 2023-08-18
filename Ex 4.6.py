def computepay (r, h):
    if 0 < h <= 40:
        pay = r * h
    elif h > 40: 
        pay = r * 40 + (r * 1.5) * (h - 40)
    return pay

rate = input('Enter pay rate:')
hrs = input('Enter hour worked:')

try: 
    r = float(rate)
    h = float(hrs)
except: 
    print ('Please enter only valid positive numbers')

print ('Pay', computepay(r, h)) 

symbol1 = input (rate, ', please choose your symbol'),