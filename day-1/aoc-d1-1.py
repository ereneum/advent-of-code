# Advent of Code Day 1: Trebuchet?! Part-1 

with open('input.txt', 'r') as f:
    lines = f.readlines()

def calibration(line):
    digits = ''.join(filter(str.isdigit, line))
    fd = digits[0]
    ld = digits[-1]
    return int(fd + ld)

res = sum(calibration(line) for line in lines)

print(res)
