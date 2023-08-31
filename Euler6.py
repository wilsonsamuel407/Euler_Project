# Euler_6
# Find the difference between the sum of the squares of the first hundred 
# numbers and square of the sum

numbers = range(1,101)
squares = []
for n in numbers:
    squares.append(n**2)

sum_of_squares = sum(squares)
square_of_the_sum = sum(numbers)**2
answer = square_of_the_sum - sum_of_squares
print(answer)
