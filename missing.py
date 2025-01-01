
from typing import List

def find_missing_number(n: int, numbers: List[int]) -> int:
    sum_n = n * (n + 1) // 2
    sum_given = sum(numbers)
    return sum_n - sum_given


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(find_missing_number(n, numbers))


if __name__ == '__main__':
    main()