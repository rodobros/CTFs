import sys

letter = sys.argv[1]
number = sys.argv[2]
final_char = sys.argv[3]

answer = letter * int(number) + final_char
print answer