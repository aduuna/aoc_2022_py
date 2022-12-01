EXPECTED_OUTPUT_FROM_DESCRIPTION = 45000


def process_input(data: list):
    # process input data here
    processed_data = []
    temp = []
    for i in data:
        if i == "\n":
            processed_data.append(temp)
            temp = []
        else:
            temp.append(int(i.rstrip("\n")))
    processed_data.append(temp)
    return processed_data


def part1(input_data):
    weights = map(sum, input_data)
    return max(weights)


def part2(input_data):
    weights = map(sum, input_data)
    return sum(sorted(list(weights))[-3:])


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "test_input.txt")) as f:
        data = f.readlines()

    output = part1(process_input(data))
    print(output)
    assert output == EXPECTED_OUTPUT_FROM_DESCRIPTION

    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.readlines()

    print(part1(process_input(data)))
    print(part2(process_input(data)))
