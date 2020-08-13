#0 to 3,999

# 40 = XL
# 50 = L
# 90 = XC
# 100 = C
#500 = D
# 900 = CM
#1000 = M 
#get length of number
#if number is 1- 10, hardcode values
#if number is 10-39 --> 
#if number starts with 4

#never more than 4 chars in a row


#test cases
# 2447 --> MMCDXLVII 2 1000 = MM CD = 400 XLVII = 47
# 49 --> XLIX
# 3999 --> MMMCMXCIX --> 3 1000 = MMM CM = 900 XC = 90 IX = 9
#463 --> CDLXIII 

#1001 

def less_than_10(num):
    
    roman = ""
    
    if num <= 3:
        roman = 'I' * num
    if num == 4:
        roman = 'IV'
    if num >= 5 and num <= 8:
        remainder = num - 5
        roman = 'V' + (remainder * 'I')
    if num == 9:
        roman = 'IX'
            
                
    return roman


def int_to_roman(num):
    
    len_int = len(str(num))
    
    roman = ""
    
    if len_int == 1:
        roman = less_than_10(num)
    elif len_int == 2:
        if num >= 10 and num <= 99:
            base_str = str(num)[0]
            base_num = int(base_str)
            remainder = num % 10
            if base_num <= 3:
                roman = ('X' * base_num) + less_than_10(remainder)
            elif base_num == 4:
                roman = 'XL' + less_than_10(remainder)
            elif base_num >= 5 and base_num <=8:
                base_remainder = base_num - 5
                roman = 'L' + ('X' * base_remainder) + less_than_10(remainder)
            else:
                roman = 'XC' + less_than_10(remainder)
                
    return roman


    
assert int_to_roman(3) == 'III'  
assert int_to_roman(8) == 'VIII'
assert int_to_roman(5) == 'V'
assert int_to_roman(10) == 'X'
assert int_to_roman(39) == "XXXIX"
assert int_to_roman(49) == 'XLIX'
assert int_to_roman(84) == 'LXXXIV'
assert int_to_roman(91) == 'XCI'
    
    