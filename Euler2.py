# Even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# A Fibonacci Function
def Fibonacci(n):
	initsequence = [0,1]

	for i in range(2,n+1):
		next_num = initsequence[-1] + initsequence[-2]

		initsequence.append(next_num)
	return initsequence

# Create a list of values up to 4 million
for a in range(1,40,1):
	m = max(Fibonacci(a))
	if m < 4000000:
		continue
	else:
		break

sequence = Fibonacci(a)

# Create the subset of even numbers
even_sequence = []
for seq in sequence:
	if seq % 2 == 0:
		even_sequence.append(seq)
	else:
		pass
# Sum the list of even Fibonnaci numbers less than 4 million
answer = sum(even_sequence)
print(answer)
