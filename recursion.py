
def decodeVariations(S):
    """
    @param S: str
    @return: int


    A letter can be encoded to a number in the following way:

    'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
    A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

    Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

    Examples:

    input:  S = '1262'
    output: 3
    explanation: There are 3 messages that encode to '1262' : 'AZB', 'ABFB', and 'LFB'.
    """
  
    #base case: string is 2 or less chars
    if len(S) == 1:
        return 1
    elif len(S) == 2 and int(S) <= 26:
        return 2
    elif len(S) <= 2:
        #chars over 26 that end in 0 are not valid bc 0 does not translate to letter
        if int(S[-1]) == 0:
            return 0
        else:
            return 1

    #take 1st char in string and 1st 2 chars (check if less than 26 for valid char)
    char1 = S[0]
    char2 = S[0:2]
  
    char1_remain = S[1:]
    char2_remain = S[2:]

    if int(char2) > 26:
        return decodeVariations(char1_remain)
    else:
        return decodeVariations(char1_remain) + decodeVariations(char2_remain)
