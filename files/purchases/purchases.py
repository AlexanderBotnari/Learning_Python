def write_products():
    products = input('Introduceti lista produse prin virgula: ').split(',')
    with open('list_cumparaturi.txt', 'w') as products_file:
        for product in products:
            print(product, file=products_file)


def read_products():
    with open('list_cumparaturi.txt', 'r') as products_file:
        for line in products_file:
            print(line, end='')


def update_products():
    product_to_append = input('Introduceti un nume de produs: ')
    with open('list_cumparaturi.txt', 'a') as products_file:
        print(product_to_append, file=products_file)


while True:
    print("############ Purchases Menu ############")
    print("Input '1' - for write products list\n" +
          "Input '2' - for read products list\n" +
          "Input '3' - for update products list\n" +
          "Input '0' - to stop program")
    option = int(input("Enter a option: "))
    if option == 1:
        write_products()
        continue
    elif option == 2:
        read_products()
        continue
    elif option == 3:
        update_products()
        continue
    elif option == 0:
        break
    else:
        print("Error for this input!")
        break
