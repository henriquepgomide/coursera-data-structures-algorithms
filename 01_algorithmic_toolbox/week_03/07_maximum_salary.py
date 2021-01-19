def largest_concatenate_problem(numbers):

    def is_better(number, max_number):
        return int(str(number) + str(max_number)) >= int(str(max_number)+ str(number))

    largest_number = list()

    while len(numbers) > 0:
        max_number = 0
        for number in numbers:
            if is_better(number, max_number):
                max_number = number
        largest_number.append(max_number)
        numbers.remove(max_number)

    return int("".join(map(str, largest_number)))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_concatenate_problem(input_numbers))
