from calculator1 import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared is not 4")
    if square (3) != 9:
        print ("3 squared is not 9")
    if square(4) != 16:
        print("4 squared is not 16")

if __name__ =="__main__":
    main()
