# problem:
# Please follow the steps in this document - don’t worry about solving the problem by yourself - we don’t expect you to solve it by yourself!
# Time commitment: Min - 30 min, Max - 60 min


# Prompt
# Given a column title as appears in an Excel sheet, return its corresponding column number.

# Examples:
# A -> 1
    
# B -> 2
    
# C -> 3
    
#     ...
    
# Z -> 26
    
# AA -> 27
    
# AB -> 28 


# solution: 
def excel_column_to_number(column):
  ans = 0
  power = len(column)-1
  for index in range(0, len(column)):
      ans += (ord(column[index])-64) * (26**(power-index))
  return ans


# process: 
# start with a answer variable

# create a power variable to and set to the length of the column -1

# loop through the length of the column 

# add to the answer variable the column equivalence of each character and multiply by how many full rotations columns have been created (like tenths, hundredths, thousandths)

# return answer at the end
	