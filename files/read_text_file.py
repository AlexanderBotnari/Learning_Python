# with open('C:/Users/Alexandru/PycharmProjects/Learning_Python/files/001 sample.txt') as file:
#     text = file.readline()
#     while text:
#         print(text, end='')
#         text = file.readline()

with open('C:/Users/Alexandru/PycharmProjects/Learning_Python/files/001 sample.txt', 'r') as file:
    text = file.readlines()
for line in text:
    if 'let' in line.lower():
        print(line, end='')

# file = open('C:/Users/Alexandru/PycharmProjects/Learning_Python/files/001 sample.txt', 'r')
# for line in file:
#     print(line, end='')
# file.close()
