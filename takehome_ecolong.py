"""Have the function PermutationStep(num) take the num parameter being passed 
and return the next number greater than num using the same digits. 
For example: if num is 123 return 132, if it's 12453 return 12534. 
If a number has no greater permutations, return -1 (ie. 999).
Examples
Input: 11121
Output: 11211
Input: 41352
Output: 41523"""

from itertools import permutations 
from copy import deepcopy

def PermutationStep(num):

  num_permutations = []

  if len(str(num)) <= 1:
    return -1
  else:
    #create set of all permutations
    num_permutations.extend({''.join(p) for p in permutations(str(num))})

  sorted_permutations = sorted(num_permutations)
  
  #start with highest value difference by getting largest value permutation
  min_diff = int(sorted_permutations[-1]) - num
  return_val = -1

  for option in num_permutations:
    if int(option) > num:
      if (int(option) - num) < min_diff:
        return_val = option
        min_diff = int(option) - num

  return return_val


###############################################################################
def MinWindowSubstring(strArr):

  string = strArr[0]
  substr = strArr[1]
  substr_list = []
  output_options = []
 
  for char in substr:
    substr_list.append(char)
  
  start_idx = 0

  while start_idx <= len(string) - len(substr):
    output = ""

    substr_list_copy = deepcopy(substr_list)

    if string[start_idx] not in set(substr):
      break
    else:
      for letter in string[start_idx:]:
        output += letter

        if letter in set(substr_list_copy):
          substr_list_copy.remove(letter)
         
        if not substr_list_copy:
          output_options.append(output)
          break
        
    start_idx += 1
        
  sorted_options = sorted(output_options)
  
  return sorted_options[0]


print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))
assert MinWindowSubstring(["aabdccdbcacd", "aad"]) == "aabd"
assert MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]) == "aksfaje"
