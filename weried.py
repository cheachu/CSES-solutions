def find_answer(n):
    while n != 1:
        print(n)
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n // 2
    print(1)  # Print the last value 1

n = int(input())
find_answer(n)
