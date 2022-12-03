outcomes = {
    'A': {
        'X': 3,
        'Y': 4,
        'Z': 8
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9
    },
    'C': {
        'X': 2,
        'Y': 6,
        'Z': 7
    },
}

with open('data.txt', 'r') as file:
    print(sum([outcomes[line.split()[0]][line.split()[1]]
          for line in file.readlines()]))
