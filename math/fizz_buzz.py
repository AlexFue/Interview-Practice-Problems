# Problem: 
	# Given an input, print all numbers up to and including that input, unless they are divisible by 3, then print "fizz" instead, or if they are divisible by 5, print "buzz". If the number is divisible by both, print "fizzbuzz".

	# For example, given 5:

	# 1
	# 2
	# fizz
	# 4
	# buzz


	# Given 10:
	# 1
	# 2
	# fizz
	# 4
	# buzz
	# fizz
	# 7
	# 8
	# fizz
	# buzz

	# Given 15:
	# 1
	# 2
	# fizz
	# 4
	# buzz
	# fizz
	# 7
	# 8
	# fizz
	# buzz
	# 11
	# fizz
	# 13
	# 14
	# fizzbuzz


# Solution: 
def fizzbuzz(n):
    for x in range(1, n+1):
      if x % 3 == 0 and x % 5 == 0:
        print('fizzbuzz')
      elif x % 3 == 0:
        print('fizz')
      elif x % 5 == 0:
        print('buzz')
      else:
        print(x)

# process: 
	#input: 15
	#start at 1 and go all the way to 15
	#1 - not div by 3, 5, or both, so print : 1
	#2 - not div by 3, 5, or both, so print : 2
	#3 - not div by 5, both, but div by 3 so print: fizz
	#4 - not div by 3, 5, or both, so print : 4
	#5 - not div by 3, both, but div by 5 so print : buzz
	#15 - div by 3, 5, and both so print : fizzbuzz











