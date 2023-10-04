with open('file_bytes', 'bw') as file:
    file.write(bytes(range(21)))

with open("file_bytes", 'br') as file:
    for line in file:
        print(line)
