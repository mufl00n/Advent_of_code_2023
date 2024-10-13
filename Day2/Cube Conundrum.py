####### ART 1 ########
# with open('sharp.txt') as f:
#     lines = f.readlines()
#     total = 0
#     for line in lines:
#         item = {'red': 0, 'green': 0, 'blue': 0}
#         game_id = int(line.strip().split(':')[0].split()[1])
#         game_set = line.replace(f'Game {game_id}:', '').strip().split(';')
#         correct = True
#         for set in game_set:
#             set = set.split(', ')
#             for part in set:
#                 part = part.split()
#                 item[part[1]] = int(part[0])
#             if item['red'] > 12 or item['green'] > 13 or item['blue'] > 14:
#                 correct = False
#                 break
#         if correct == True:
#             total += game_id

# print('solution is: ', total)

####### PART 2 ######
with open('sharp.txt') as f:
    lines = f.readlines()
    red_count = []
    green_count = []
    blue_count = []
    color_total = []
    total = 0
    for line in lines:
        item = {'red': 0, 'green': 0, 'blue': 0}
        game_id = int(line.strip().split(':')[0].split()[1])
        game_set = line.replace(f'Game {game_id}:', '').strip().split(';')
        for part in game_set:
            part = part.split(',')
            for i in part:
                i = i.split()
                item[i[1]] = int((i)[0])

                red_count.append(item['red'])
                blue_count.append(item['blue'])
                green_count.append(item['green'])
        color_total.append(max(red_count))
        color_total.append(max(blue_count))
        color_total.append(max(green_count))
        print(f'color_total obsahuje: {color_total}')
        result = 1
        for i in color_total:
            result *= i
        total += result
        red_count = []
        blue_count = []
        green_count = []
        color_total = []

print(total)


