EXPECTED_OUTPUT_FROM_DESCRIPTION = 10


def process_input(data: list):
    # process input data here
    return data[0]


def compute(input_data, size):
    # random signals received
    # series of 4 unique characters marks the end of a marker

    # loop through the string with a ptr
    # using sliding window of size 4
    # check if all chars in window is unique

    for i in range(len(input_data)-size):
        if len(set(input_data[i:i+size])) == size:
            return i + size


def part1(input_data):
    return compute(input_data, 4)


def part2(input_data):
    return compute(input_data, 14)


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "test_input.txt")) as f:
        data = f.readlines()

    output = part1(process_input(data))
    print(output)
    assert output == EXPECTED_OUTPUT_FROM_DESCRIPTION

    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.readlines()

    # print(part1(process_input(data)))
    print(part2(process_input(data)))
