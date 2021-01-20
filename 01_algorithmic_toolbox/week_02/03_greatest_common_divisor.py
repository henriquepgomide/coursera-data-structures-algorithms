def gcd(a, b):
    '''
    Compute the greatest common divisor
    '''
    if b == 0:
        return a
    else:
        a_p = a % b
        return gcd(b, a_p)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
