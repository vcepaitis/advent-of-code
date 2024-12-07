def try_iteratively(inputs, current, output):

    next_input = inputs[0]

    if current * next_input == output:
        return True

    elif current + next_input == output:
        return True

    elif len(inputs) == 1:
        return False
    
    else:
        if try_iteratively(inputs[1:], current * next_input, output):
            return True
        if try_iteratively(inputs[1:], current + next_input, output):
            return True
    return False


def try_iteratively_concat(inputs, current, output):
    next_input = inputs[0]
    joined = int(f"{current}{next_input}")
    if len(inputs) == 1:
        if current * next_input == output:
            return True
        if current + next_input == output:
            return True
        if joined == output:
            return True

    else:
        if try_iteratively_concat(inputs[1:], current * next_input, output):
            return True
        if try_iteratively_concat(inputs[1:], current + next_input, output):
            return True
        if try_iteratively_concat(inputs[1:], joined, output):
            return True
    return False

with open("input") as f:
    # sum = 0
    sum2 = 0
    for i, line in enumerate(f):
        output, inputs = line.strip().split(":")
        output = int(output)
        inputs = inputs.lstrip().split(" ")
        inputs = [int(x) for x in inputs]

        # if try_iteratively(inputs[1:], inputs[0], output):
        #     sum += output

        if try_iteratively_concat(inputs[1:], inputs[0], output):
            sum2 += output

    # print(sum)
    print(sum2)
