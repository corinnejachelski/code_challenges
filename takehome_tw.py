#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#
#given an input list of codes such as 'FLWR' or 'CODE' and a list of phone numbers (+12345678900), find if the code
#matches any given segment of the number on a T9 keypad
#ie CODE = 2633
# number = +14102263356 -> add number to output list
def vanity(codes, numbers):
    # print(codes)
    # print(numbers)
     
    keypad = {2: {'A', 'B', 'C'}, 3: {'D', 'E', 'F'}, 4: {'G', 'H', 'I'}, 5: {'J', 'K', 'L'}, 6: {'M', 'N', 'O'}, 7: {'P', 'Q', 'R', 'S'}, 8: {'T', 'U', 'V'}, 9: {'W', 'X', 'Y', 'Z'}}
    vanity_nums = []
    
    #create letter to number vanity code translation
    for code in codes:
        translate = ""
        for letter in code:
            for key, vals in keypad.items():
                if letter in vals:
                    translate += str(key)
                if len(translate) == len(code):
                    break
            #translate to numbers
        
        vanity_nums.append(translate)   
        print(vanity_nums)
        
    code_matches = []   
    for vanity in vanity_nums:
        #skip + sign at beginning (idx 0) of number string
        
        
        for number in numbers:
            start_idx = 1
            end_idx = len(vanity) + 1
            while end_idx <= len(number):
                #print(number[start_idx:end_idx])
                if number[start_idx:end_idx] == vanity and number not in code_matches:
                    code_matches.append(number)
                    break
                else:
                    start_idx += 1
                    end_idx += 1
                
    return(code_matches)
                    
        
#
# Complete the 'segments' function below.
#return SMS messages where the message is less than or equal to 160 chars, including a suffix (1/5)
#where 1 is the current segement count and 5 is total segments sent
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING message as parameter.
#
 
#if len message <= 160, return message
#else segment = message[start_idx:end_idx] + (1/count)
#append segment to list of segments -> print each item

def segments(message):
    
    segments = []
    
    if len(message) <= 160:
        segments.append(message)
    else:
        start_idx = 0
        #subtract suffix length of 5
        end_idx = 155
        
        #num segment
        count = 1
        total_segs = math.ceil(len(message)/160)
        
        while end_idx <= len(message):
            suffix = f'(' + str(count) + '/'+ str(total_segs) + ')'
            segments.append(message[start_idx:end_idx] + suffix)
            start_idx += 155
            end_idx += 155
            count += 1
            if end_idx >= len(message):
                suffix = f'(' + str(count) + '/'+ str(total_segs) + ')'
                segments.append(message[start_idx:len(message)] + suffix)
            
    return segments