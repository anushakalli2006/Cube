import sys

def cube(num):
    return num ** 3

if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
    except IndexError:
        num = int(input("Enter number: "))
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)

    print("Cube:", cube(num))

