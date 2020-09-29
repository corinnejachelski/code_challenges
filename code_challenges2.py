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
            