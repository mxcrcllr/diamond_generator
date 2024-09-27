def print_diamond(n):
    if n % 2 == 0:
        print("Please provide an odd integer.")
        return
    
    for i in range(n // 2 + 1):
        stars = "*" * (2 * i + 1)
        spaces = " " * (n // 2 - i)
        print(spaces + stars)

    for i in range(n // 2 - 1, -1, -1):
        stars = "*" * (2 * i + 1)
        spaces = " " * (n // 2 - i)
        print(spaces + stars)

n = int(input("Enter an odd number: "))
print_diamond(n)