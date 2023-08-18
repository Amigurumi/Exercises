largest = None
smallest = None

while True:
    num = input ('Enter a number: ')
    if num == 'done':
        print ('Maximum is', largest)
        print ('Minimum is', smallest)
        break
    try:
        num = int(num)
    except:
        print ('Invalid input')
        continue 
    if smallest is None or smallest > num:
        smallest = num
    if largest is None or largest < num:
        largest = num