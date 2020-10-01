# input: string
# output: substring of input string, which is the longest substring containing unique characters

# "abca" -> "abc"
# "aa" -> "a"
# "aba" -> "ab"
# "aA" -> "aA"
# "abcaaqwerty" -> "qwerty"

def longest_substring(string):

    output = []
    curr_str = ""

    
    for char in string:
        if char not in set(curr_str):
            curr_str += char
        else:
            output.append(curr_str)
            curr_str = char
            
    output.append(curr_str)
    
    max_len = 0
    longest = ""
    

    for word in output:
        if len(word) >= max_len:
            max_len = len(word)
            longest = word
 
    return longest


print(longest_substring("abcabcdef"))         
assert longest_substring("abcaaqwerty") == "aqwerty"
assert longest_substring("aA") == "aA"
assert longest_substring("aa") == "a"
assert longest_substring("abcabcdef") == "abcdef"  

##############################################################################
#given 2 lists [1, 2, 3], [4, 7] return a list of total sum (123 + 47 = 170) [1, 7, 0]
# [ 1, 1, 6] [3, 3] = [1,4,9]

#[1, 2, 7]
#   [4, 7]
#14
#4

def sum_lists(a, b):

    final_sum = []
    check_sum = 0

    while a or b:
        if a and b:
            check_sum += a[-1] + b[-1]
            if check_sum >= 10:
                final_sum.append(check_sum - 10)
                check_sum = 1
            else:
                final_sum.append(check_sum)
                check_sum = 0
            a.pop()
            b.pop()
        elif b:
            final_sum.extend(b)
            b = []
        else: 
            final_sum.extend(a)
            a = []

    final_sum.reverse()
    return final_sum

assert sum_lists([1, 2, 7], [4, 7]) == [1, 7, 4]
assert sum_lists([1, 1, 6,], [3, 3]) == [1, 4, 9]
assert sum_lists([1, 1, 6, 0], [3, 3]) == [1, 1, 9, 3]
###############################################################################
#Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):

    row = 0
    col = 0
    d1 = 0
    d2 = 0

    #get first diagonal
    while row <= len(arr) - 1:
        d1 += arr[row][col]
        row += 1
        col += 1

    row = 0
    col = -1

    #get second diagonal
    while row <= len(arr) - 1:
        d2 += arr[row][col]
        row += 1
        col -= 1

    return abs(d1 - d2)
###############################################################################
#Given a time in 12-hour AM/PM format (hh:mm:ssAM/PM), convert it to military (24-hour) time.

def timeConversion(s):

    pm = 0
    
    if s[-2:] == "PM" and s[0:2] != "12":
        pm = int(s[0:2]) + 12
        return str(pm) + s[2:-2]
    elif s[-2:] == "AM" and s[0:2] == "12":
        return "00" + s[2:-2]
    else:
        return s[:-2]
###############################################################################
# Interview question: version number comparison
# 
# The goal of this question is to write a function, in a language of
# your choice, that will compare two version number strings. Version
# number strings are strings like "0.2.3" or "2.12.4". They are strings
# of digits separated by periods. You may assume that the strings do
# not contain any other characters.
# 
# The comparison function will take 2 such strings as inputs, and
# return an integer as the result. If the input strings are "a" and
# "b", the function should return:
# 
# 1, if a > b
# 0, if a == b
# -1, if a < b
# 
# The comparison needs to be based on the version numbers. This
# comparison is defined by considering each component integer of the
# strings pairwise. Here are some examples:
# 
# 2.12 > 2.2 (because 12 > 2)
# 1.2.3 == 1.2.3
# 1.2.0 == 1.2
# 1.2.0.0 == 1.2
# 1.2.0.1 > 1.2
# 1.2.10 < 1.2.12
# 
# Code below, in a language of your choice
# (something like C, C++, Java, python or JavaScript would be good):


#split strings on .
#loop through items in both lists, check s1[0] < > = s2[0]
# if =, continue to next item
#else return 1 or -1

#check if length of lists is equal
#if one list longer AND remaining values are 0

def normalize_lists(v1_list, v2_list):

    len1 = len(v1_list)
    len2 = len(v2_list)

    if len1 <= len2:
        diff = len2 - len1
        append_zeros(diff, v1_list)

    else:
        diff = len1 - len2
        append_zeros(diff, v2_list)
        

def append_zeros(diff, shorter_list):

    for num in range(diff):
        shorter_list.append('0') 

def compare_versions(v1, v2):

    v1_list = v1.split('.')
    v2_list = v2.split('.')

    normalize_lists(v1_list, v2_list)

    for idx, num in enumerate(v1_list):
        if int(num) > int(v2_list[idx]):
            return 1
        elif int(num) < int(v2_list[idx]):
            return -1

    return 0

print(compare_versions('1.2', '1.2.0.0'))
assert compare_versions('2.12', '2.2') == 1
assert compare_versions('1.2.3', '1.2.3') == 0
assert compare_versions('1.2', '1.2.0.0') == 0
assert compare_versions('1.2.0.1', '1.2') == 1
assert compare_versions('1.2.10', '1.2.12') == -1
###############################################################################

def bracket_match(text):
"""Given a string that consists of brackets, write a function bracketMatch that 
takes a bracket string as an input and returns the minimum number of brackets 
you’d need to add to the input in order to make it correctly matched.

A string of brackets is considered correctly matched if every opening bracket in 
the string can be paired up with a later closing bracket, and vice versa. 
For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. 
For instance, “((” could become correctly matched by adding two closing brackets 
at the end, so you’d return 2."""

    parens = []
    
    for char in text:
    
        if char == ")":
            if parens and parens[-1] == "(":
            parens.pop()
            else:
            parens.append(char)      
    
        elif char == "(":
        parens.append(char)
    
    
    return len(parens)
    
assert bracket_match("(())") == 0
assert bracket_match("(()") == 1
################################################################################