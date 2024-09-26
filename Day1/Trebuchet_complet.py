numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
total = []

with open("sharp.txt") as f:
    lines = f.readlines()


def find_numbers_and_words():
    for line in lines:
        digits = []
        for a, b in enumerate(line):
            if b.isdigit():
                digits.append(b)
            else:
                for aa, bb in enumerate(numbers):
                    if line[a:].startswith(bb):
                        digits.append(str(aa + 1))
        total.append(digits[0] + digits[-1])


find_numbers_and_words()

total = list(map(int, total))
print(f'Coordinates are: {sum(total)}')