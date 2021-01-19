def fibonacci_number(n):
    assert 0 <= n <= 45

    numbers_list = [None] * (n + 1)

    if n <= 1:
        return n
    else:
        numbers_list[0] = 0
        numbers_list[1] = 1
        for i in range(2, n+1):
            numbers_list[i] = numbers_list[i-2] + numbers_list[i-1]

    return numbers_list[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
