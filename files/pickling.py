import pickle

honda = ('civic', 10000, (1999, 2023), (1, 'John', 2, 'Jane', 3, 'Jack'))

with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)
    pickle.dump(999999, honda_file)
    pickle.dump(['John', 'Jack', 'Jane'], honda_file)


with open('honda.pickle', 'rb') as honda_file:
    honda_from_file = pickle.load(honda_file)
    number = pickle.load(honda_file)
    owner_list = pickle.load(honda_file)

print(honda_from_file)
print(number)
print(owner_list)
