def majority_element(elements):
    assert len(elements) <= 10 ** 5

    n = len(elements)
    maximum = elements[0]
    amount = 1

    for i in elements[1:]:
        if not maximum == i:
            if amount >= 1:
                amount -= 1
            else:
                maximum = i
                amount = 1
        else:
            amount += 1

    output = elements.count(maximum)

    if output // 2:
        return 1
    
    return 0


if __name__  == "__main__":
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
