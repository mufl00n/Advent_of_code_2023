import re

found_first = []
found_last = []

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

with open('test3.txt') as f:
    lines = f.readlines()

def find_last():
    for line in lines:
        last = []
        number = re.search(r'\d',line[::-1])
        found_last.append(int(number.group()))



def find_first():
    for line in lines:
        first = []
        number = re.search(r'\d',line)
        found_first.append(int(number.group()))
    find_last()

find_first()



# found_first = list(map(int, found_first))
# found_last = list(map(int, found_last))
print(f'found first: {found_first}')
print(f'found last: {found_last}')
