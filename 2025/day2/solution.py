import math

filename = "input"

def get_divisors(n, divisors_dict):
    if n not in divisors_dict:
        divisors_dict[n] = []
        for i in range(2, n+1):
            if n % i == 0:
                divisors_dict[n].append(i)
    return divisors_dict[n], divisors_dict


with open(filename) as f:
    data = f.read()
    data = data.split(",")

invalid_sum = 0
invalid_sum_2 = 0

divisors_dict = {2: [2]}

for order_range in data:
    order_min, order_max = order_range.split("-")
    order_min = int(order_min)
    order_max = int(order_max)
    for order in range(order_min, order_max+1):
        n_digit = math.ceil(math.log10(order))
        # First part
        if n_digit % 2 == 0:
            n_split = int(n_digit/2)
            first = str(order)[:n_split]
            second = str(order)[n_split:]
            if first == second:
                print(f"Found invalid order id (part 1) {order}")
                invalid_sum += order
        # Second part
        # Find all divisors of the digit
        divisors, divisors_dict = get_divisors(n_digit, divisors_dict)
        for divisor in divisors:
            len_substrings = n_digit // divisor 
            substrings = set()
            for i in range(divisor):
                substring = str(order)[i*len_substrings:(i+1)*len_substrings] 
                substrings.add(substring)
            if len(substrings) == 1:
                print(f"Found invalid ID (part 2) {order}")
                invalid_sum_2 += order
                break

print(invalid_sum, invalid_sum_2)