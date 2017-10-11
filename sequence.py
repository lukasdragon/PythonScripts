y = int(raw_input('Please enter first number:'))
x = int(raw_input('Please enter last number:'))

total = 0
print sum(range(1,x+1))

for i in range(y,x+1,):
    total = total + i
print total


