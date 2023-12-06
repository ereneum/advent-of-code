# Advent of Code Day 1: Trebuchet?! Part-2

w2d = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

with open('input.txt', 'r') as f:
    c = f.read()
    for w, d in w2d.items():
        c = c.replace(w, d)

    lines = c.splitlines()    

def calibration(line):
    digits = ''.join(filter(str.isdigit, line))
    fd = digits[0]
    ld = digits[-1]
    return int(fd + ld)

res = sum(calibration(line) for line in lines)

print(res)
