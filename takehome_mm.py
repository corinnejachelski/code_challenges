'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys

stdin = []

for line in sys.stdin:
    stdin.append(line)

#remove white space from strings
r1 = stdin[0].replace(" ", "")
r2 = stdin[1].replace(" ", "")


def get_coordinates(r1, r2):
    """returns (x1, y1, x2, y2) for each rectangle where lower left = (x1, y1) upper right = (x2, y2)"""
    #get lower left coordinates (x,y) for each rect
    ll1_x = int(r1[0])
    ll1_y = int(r1[1])
    ll2_x = int(r2[0])
    ll2_y = int(r2[1])

    #width for each rect
    w1 = int(r1[2])
    w2 = int(r2[2])

    #height for each rect
    h1 = int(r1[3])
    h2 = int(r2[2])

    #get upper right coordinates
    ur1_x = ll1_x + w1
    ur1_y = ll1_y + h1
    ur2_x = ll2_x + w2
    ur2_y = ll2_y + h2

    #create tuples of xmin ymin xmax ymax --> lower left x, lower left y, upper right x, upper right y
    rect1 = (ll1_x, ll1_y, ur1_x, ur1_y)
    rect2 = (ll2_x, ll2_y, ur2_x, ur2_y)

    return (rect1, rect2)

def calc_area(a, b): 
    """Returns overlapping area of 2 rectangles"""
    dx = max(a[0], b[0]) - min(a[2], b[2])
    dy = max(a[1], b[1]) - min(a[3], b[3])
    if dx!=0 and dy!=0:
        return dx*dy
    if dx == 0 or dy == 0:
        return 0

rect1, rect2 = get_coordinates(r1, r2)
print(calc_area(rect1, rect2))

#Runtime: Reading from stdin uses a for loop at O(n) time. Accessing indices in a list is O(1). Max and min methods check every element at O(n) time - this occurs 4 total times. Overall runtime is ~5 O(n), which is O(n)


###############################################################################
#return max product of 3 integers in a list
import sys

nums = []

for line in sys.stdin:
    nums.append(int(line.rstrip('\n')))

#first item in list is number of values to be assessed, should be ignored
if len(nums) >= 4:
    sorted_nums = sorted(nums[1:])
    #multiply 3 largest numbers from sorted list (last 3 in list)
    max_prod = sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3]
else:
    max_prod = "Too few numbers"

print(max_prod)

#Runtime: looping over lines in stdin is O(n). Built in sorting method runs in O(n log n). Accessing indices in a list is O(1) 