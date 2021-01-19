def last_digit_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n
    else:
        numbers_list = [None] * (n + 1)
        numbers_list[0] = 0
        numbers_list[1] = 1
        for i in range(2, n + 1):
            numbers_list[i] = (numbers_list[i-2] + numbers_list[i-1]) % 10

    return numbers_list[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_fibonacci_number(input_n))
