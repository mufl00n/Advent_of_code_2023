with open('sharp.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        item = {'red': 0, 'green': 0, 'blue': 0}
        game_id = int(line.strip().split(':')[0].split()[1])
        game_set = line.replace(f'Game {game_id}:', '').strip().split(';')
        correct = True
        for set in game_set:
            set = set.split(', ')
            for part in set:
                part = part.split()
                item[part[1]] = int(part[0])
            if item['red'] > 12 or item['green'] > 13 or item['blue'] > 14:
                correct = False
                break
        if correct == True:
            total += game_id

print('solution is: ', total)


