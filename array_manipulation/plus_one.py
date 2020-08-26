Problem:
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.




Solution:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits)-1, -1, -1):
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                return digits
        digits.insert(0, 1)
        return digits




Process:
we solve this just like adding numbers on paper horizontally like: 123
																   + 1
																   ___
																   124
we start from the back of the array given and check if adding one to the number will create a carry of 1 or not


for loop starting from the back of the digits list

	if digit is 9 then we change the current digit to 0 and go on to the next number because it results as a carry 

	else then adding 1 isnt a carry so just add 1 to the current number 

return the array 