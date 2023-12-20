import re
first = []
last = []

#PART 1
with open('sharp.txt') as f:
    lines = f.readlines()

# najdeme prvu a poslednu cislicu. Nie cislo (nap. 53) ale cislicu (napr. 5). A to cez \d. Ak chceme cislo (53), tak cez \d+
def find_first():
    for line in lines:
        match = re.search(r'\d', line)
        first.append(match.group())

find_first()


def find_last():
    for line in lines:
        match = re.search(r'\d', line[::-1])
        last.append(match.group())

find_last()

print(f'first = {first}')
print(f'last = {last}')

# spojime cislice z oboch listov
sumar = [a+b for a, b in zip(first,last)]

# zo str spravime int
sumar_int = [int(i) for i in sumar]
total = (sumar_int)

# vsetko scitame
print(f'sumar = {sumar}')
print(sum(total))


