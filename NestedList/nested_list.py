nested_list = [[1, 2, 3], [True, 2, 3], [6, 7, 8], ["hello", 9, 10], [4, 6, 7]]

# for inner_list in nested_list:
#     print(inner_list)

# for inner_list in nested_list:
#     for number in inner_list:
#         print(number)

[[print(number) for number in inner_list] for inner_list in nested_list]
