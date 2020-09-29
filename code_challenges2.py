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