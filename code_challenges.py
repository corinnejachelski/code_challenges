def word_lengths(sentence):
    """Get dictionary of word-length: {words}.
    word_lengths("cute cats chase fuzzy rats")
    returns {4: {'cute', 'cats', 'rats'}, 5: {'"""

    sentence = sentence.split()

    word_lengths = {}

    for word in sentence:
        word_lengths[len(word)] = word_lengths.get(len(word), []) + [word]

    return word_lengths

print(word_lengths("cute cats chase fuzzy rats"))



def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""
    count = 0

    for char in phrase:
        if char == "(":
            count += 1
        if char == ")":
            count -= 1

    return count == 0

print(has_balanced_parens("() ) hi ("))


# def compress_string(sentence):
#     """'Hello, world! Cows go moooo...' => 'Hel2o, world! Cows go mo4.3'"""

#     new_str = ""
#     count = 1

#     for idx in range(len(sentence) -1):
#         if new_str[-1] == sentence[idx]:
#             count +=1
#             new_str += count
#         else:
#             new_str += sentence[idx]

#     return new_str

# print(compress_string('Hello, world! Cows go moooo...'))


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes.
    [
    ...    ['A', 'B', 'C', 'D'],
    ...    ['E', 'F',  0 , 'H'],
    ...    ['I', 'J', 'K', 'L']
    ...    ] 
   return [['A', 'B', 0, 'D'], [0, 0, 0, 0], ['I', 'J', 0, 'L']]"""

    col_idx_to_change = []
    row_to_change = []

    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            if val == 0:
                col_idx_to_change.append(col_idx)
                row_to_change.append(row_idx)

    for row in row_to_change:
        for item in matrix[row]:
            item = 0
        for col in col_idx_to_change:
            matrix[row][col] = 0

    return matrix

print(zero_matrix([['A', 'B', 'C', 'D'], ['E', 'F',  0 , 'H'], ['I', 'J', 'K', 'L']]))


def fit_to_width(sentence, break_num):
    """fit_to_width('Hello, world! I love Python and Hackbright', 10) --> 
    Hello,
    world! I
    love
    Python and
    Hackbright"""

    sentence = sentence.split()
    return_sentence = []

    length = break_num

    for word in sentence:
        if length == 0:
            return_sentence.append("\n")
            length = break_num
        if len(word) < length:
            return_sentence.append(word)
            length -= len(word)

    return "".join(return_sentence)

print(fit_to_width('Hello, world! I love Python and Hackbright', 10))





