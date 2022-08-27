# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

productlist = []
numlist1 = range(100,999,1)
numlist2 = range(100,999,1)
for n in numlist1:
	for u in numlist2:
		a = n*u 
		productlist.append(a)
	
listofpalindromes = []
# a function for checking for a palindrome
def isPalindrome(s):
# a slice has syntax list[<start>:<stop>:<step>]
	return s == s[::-1]

for x in productlist:
	s = str(x)
	ans = isPalindrome(s)

	if ans:
		listofpalindromes.append(x)
	else:
		pass


print(max(listofpalindromes))
