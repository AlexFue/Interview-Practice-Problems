Problem:
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a[1] >= a[2] <= a[3] >= a[4] <= a[5] ...


Example
Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 




Solution:
def wave_array(integers):
  integers.sort()
  for index in range(0, len(integers)-1, 2):
    temp = integers[index]
    integers[index] = integers[index+1]
    integers[index+1] = temp
  return integers




Process:
to make it to a wave we first have to sort the list from least to greatest and then to how the example wants. 
an easy way to do that is to just switch the positions of every 2 numbers to create the wave effected that is asked.
this way, the numbers will always be greater, less than, greater, less than, greater, and so on

sort the list of integers

for loop through the integers incrementing by two

	swap the positions of the two numbers

return the integers list




Teacher Solution:
def wave_array(integers):
  integers.sort()
  lst = []
  back = len(integers)-1
  front = 0
  while front <= back:
    lst.append(integers[back])
    lst.append(integers[front])
    back -= 1
    front += 1
  if len(integers) % 2 != 0:
    lst.pop(len(integers)-1)
  return lst




Teacher Process:
sort the integers list

make a new list where the answer will be put

make a counter for both the back and front of the list

while the front is less than or equal to the back

	append the number from the back and front of integers list

	incement the front counter and decrement the back counter

if the length of the integers list is odd then delete the last number









