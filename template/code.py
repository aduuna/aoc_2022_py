EXPECTED_OUTPUT_FROM_DESCRIPTION = None


def process_input(data: list):
    # process input data here
    return data


def part1(input_data):
    pass


def part2(input_data):
    pass


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
