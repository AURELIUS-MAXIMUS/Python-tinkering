def main():
    x = int(input("What is x?"))
    if even_num(x):
        print("even")
    else:
        print ("odd")

def even_num(x):
    if x % 2 == 0:
        return True
    else:
        return False

main()