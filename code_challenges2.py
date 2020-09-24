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

            
            
            
            