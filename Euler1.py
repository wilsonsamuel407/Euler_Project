# Find the sum of all the multiples of 3 or 5 below 1000.
# Create the list of numbers below 1000
x1 = 1
x2 = 1000
tons = list(range(x1,x2,1))
# List the multiples we are checking for
n = 3
m = 5
# Make a list of the multiples of 3 or 5
multi_3_5 = []
for i in tons:
	if i % n == 0:
		multi_3_5.append(i)
	elif i % m ==0:
		multi_3_5.append(i)
#Sum the new list
total = sum(multi_3_5)
print(total)





