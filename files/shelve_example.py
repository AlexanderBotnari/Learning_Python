import shelve

with shelve.open('shelve_file') as file:
    # file['John'] = 13000
    # file['Alex'] = 10000
    # file['Jane'] = 8000

    # for key, value in file.items():
    #     print(key, value)

    while True:
        key = input("Please input the name: ")
        if key == "quit":
            break
        print(file.get(key))
