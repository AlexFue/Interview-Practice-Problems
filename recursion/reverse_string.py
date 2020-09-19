Problem:
This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.

Again, make sure you use recursion to accomplish this. Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.

Fill out your solution below

reverse('hello world')
answer: 'dlrow olleh'



Solution:
def reverse(s):
  if s == '':
    return ''
  else:
    return s[-1] + reverse(s[:len(s)-1])
print(reverse("my name is alex"))




Process:
There are many different ways to solve this problem but we are going to do it by continuously adding the last element of the string,

since we want to reverse the string, we can keep on getting the last element in the string with indexing
we can then add this last element recursivly by calling the fucntion again for the rest of the string, without the last element we took off (make sure to add the element before the resursive function).
we can keep on doing this until we do not have a string and so all the substrings get added together