# Ask user for a number n 
# then print n asterisks


def print_asterisks(n):
    for i in range(n):
        print('*', end=' ')
    print()


if __name__ == "__main__":
    x = input("Give a number: ")
    x = int(x)
    print_asterisks(x)
