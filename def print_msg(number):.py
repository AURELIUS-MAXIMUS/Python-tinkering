def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        number = 3
        print(number)
    printer()
    print(number)

print_msg(9)