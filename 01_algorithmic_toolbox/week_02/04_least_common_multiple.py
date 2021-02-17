# python3

def gcd(a, b):
    if b == 0:
        return a
    else: 
        a_p = a % b
        return gcd(b, a_p)


def lcm(a, b):
    return int((a * b) / gcd(a, b))


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
