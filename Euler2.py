def Fibonacci(n):
	initsequence = [0,1]

	for i in range(2,n+1):
		next_num = initsequence[-1] + initsequence[-2]

		initsequence.append(next_num)
	return initsequence

sequence = Fibonacci(10)
print(sequence)
