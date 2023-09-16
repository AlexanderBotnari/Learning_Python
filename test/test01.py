# movies = ['Spider Man', 'super man', 'iron man']
#
# print(movies[1])

# person = {
#     "name": "John",
#     "surname": "Snow",
#     "age": 35,
#     "skills": ["arc", "spada", "knife"],
#     "childrens": {"son": "Matteo", "daughter": "Madalena"},
#     "isKing": True
# }
#
# print(f"{person['name']} {person['surname']} have a skills: {person['skills']}")

# new_set = set()
# print(type(new_set))

# var_int = 1
# var_float = 2.5
# var_str = "Python"
# var_bool = True
# var_list = [1, 2, 3, 4]
# var_hello = "Hello " + var_str
#
# print(float(var_int))
# print(int(var_float))
# print("Hi " + var_hello.split(" ")[1])

# number = int(input("Introduceti un numar: "))
#
# if number % 2 == 0:
#     print("Numarul este par")
# else:
#     print("Numarul este impar")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("-")

# number = int(input("Introduceti un numar: "))
#
# for i in range(2, number):
#     if number % i == 0:
#         print(i)

# number = int(input("Introduceti numarul: "))
# count = 0
# sum_of_numbers = 0
#
# if number > 0:
#     while count < number:
#         sum_of_numbers += count
#         count += 1
#
# print(sum_of_numbers)

# numbers_list = [3, 2, 5, 10, 4, 1, 6, 9, 7, 8]
# numbers_list.sort()
# print(numbers_list)
# numbers_list.sort(reverse=True)
# print(numbers_list)

# matrix = [[2, 1, 3], [5, 6, 4], [9, 7, 6]]
# ordered_list = []
# for i in matrix:
#     for k in i:
#         ordered_list.append(k)
#
# ordered_list.sort()
# print(ordered_list)

# numbers_tuple = (1, 2, 3)
# numbers_tuple[0] = 4
# print(numbers_tuple[0])

# def sum_of_numbers(x, y):
#     return x+y
#
#
# print(sum_of_numbers(2, 4))


# def get_average(list_of_numbers):
#     sum_of_numbers = sum(list_of_numbers)
#     return sum_of_numbers / len(list_of_numbers)
#
#
# print(get_average([1, 2, 3, 4]))

# def get_max_word(words):
#     max_word = 0
#     for word in words:
#         if len(word) > max_word:
#             max_word = len(word)
#     return max_word
#
#
# print(get_max_word(["Hi", "Hello", "Hola", "Hello2"]))

# def is_palindrom(word):
#     word.lower()
#     return word == word[::-1]
#
#
# print(is_palindrom("radar"))

# print("Python".startswith("P"))
# print("Java".endswith("o"))

name = "John"
age = 45

print("{} are {} old years".format(name, age))
