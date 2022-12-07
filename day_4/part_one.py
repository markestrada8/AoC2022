count = 0
lines_list = []

with open('data.txt', 'r') as file:
    for line in file.readlines():
        lines_list.append([[int(num) for num in line.split(',')[0].split(
            '-')], [int(num) for num in line.split(',')[1].split('-')]])
    for pair in lines_list:
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]):
            count += 1

print(count)
