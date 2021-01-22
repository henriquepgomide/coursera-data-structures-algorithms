def compute_min_number_refills(d, m, stops):

    num_refills = 0
    current_refill = 0
    stops = [0] + stops + [d]

    if d <= m:
        return 0
    else:
        while current_refill < len(stops) - 1:
            last_refill = current_refill
            while current_refill < len(stops) - 1 and stops[current_refill + 1] - stops[last_refill] <= m:
                current_refill +=1
            if current_refill == last_refill:
                return -1
            if current_refill < len(stops) - 1:
                num_refills += 1

        return num_refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n
    print(compute_min_number_refills(input_d, input_m, input_stops))


