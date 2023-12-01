import re

total = 0

word_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("aoc1i2.txt", "r") as f:
    for line in f.readlines():
        results = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
        a = results[0]
        b = results[-1]
        if len(a) > 1:
            total += 10 * word_mapping[a]
        else:
            total += 10 * int(a)
        if len(b) > 1:
            total += word_mapping[b]
        else:
            total += int(b)

        

print(total)