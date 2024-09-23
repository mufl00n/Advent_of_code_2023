import re

found_first = []
found_last = []
first_sorted = []
first_number = []
last_number = []
total = []
numbers_dir = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']



# PART 2
####################################### ZIP FIRST AND LAST ######################################




####################################### FIND FIRST NUMBER ######################################
with open('sharp.txt') as f:
    lines = f.readlines()


def translate_number_to_string_first():
    for word in found_first:
        if word in numbers_dir.values():
            first_number.append(list(numbers_dir.keys())[list(numbers_dir.values()).index(word)])




def find_first():
    for line in lines:
        first = []
        for key, value in numbers_dir.items():
            match = re.search(value, line)
            if match:
                first.append((match.start(), value))
                first.sort()
                print(first)
        if first[0][1]:
            found_first.append(first[0][1])
        else:
            found_first.append(first[0][0])


find_first()
translate_number_to_string_first()


####################################### FIND LAST NUMBER ######################################
def translate_number_to_string_last():
    for word in found_last:
        if word in numbers_dir.values():
            last_number.append(list(numbers_dir.keys())[list(numbers_dir.values()).index(word)])



def find_last():
    for line in lines:
        last = []
        for key, value in numbers_dir.items():
            match = re.search(value, line)
            if match:
                last.append((match.start(), value))
                last.sort()
        found_last.append(last[-1][1])


def zipping():
    for a, b in zip(first_number, last_number):
        total.append(int(a) *10 + int(b))





find_last()
translate_number_to_string_last()
zipping()
print(sum(total))


