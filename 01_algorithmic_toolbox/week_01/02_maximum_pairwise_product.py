def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    list_of_numbers = list(sorted(numbers, reverse=True))

    return list_of_numbers[0] * list_of_numbers[1]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
