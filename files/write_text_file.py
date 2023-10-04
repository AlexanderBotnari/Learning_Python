# write
colors = ['blue', 'red', 'green', 'yellow', 'indigo', 'violet']
with open('C:/Users/Alexandru/PycharmProjects/Learning_Python/files/colors.txt', 'w') as file:
    for color in colors:
        print(color, file=file)

# read
colors_from_file = []
with open('C:/Users/Alexandru/PycharmProjects/Learning_Python/files/colors.txt', 'r') as file:
    for line in file:
        colors_from_file.append(line.strip('\n'))
print(colors_from_file)

# append
with open('C:/Users/Alexandru/PycharmProjects/Learning_Python/files/colors.txt', 'a') as file:
    print('dark green', file=file)
    print('dark blue', file=file)
