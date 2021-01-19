def largest_concatenate_problem(numbers):
    def is_better(number, max_number):
        if max_number == float('-inf'):
            return True
        else:
            return number > int(str(max_number)[0])
    largest_number = list()
    while len(numbers) > 0:
        max_number = float('-inf')
        for number in numbers:
            if is_better(number, max_number):
                max_number = number
        largest_number.append(max_number)
        numbers.pop(numbers.index(max_number))
    return largest_number

