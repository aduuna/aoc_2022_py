EXPECTED_OUTPUT_FROM_DESCRIPTION = 2


def process_input(data: list):
    # process input data here
    # [''] => [[(), ()], ...]
    processed_data = []
    for line in data:
        part_a, part_b = line.strip().split(",")
        processed_data.append(
            [[int(x) for x in part_a.split('-')], [int(x) for x in part_b.split('-')]])
    return processed_data


def is_contained(child, parent):
    return child[0] >= parent[0] and child[1] <= parent[1]


def partial_overlap(part_a, part_b):
    if part_b[0] <= part_a[0] <= part_b[1]:
        return True
    elif part_b[0] <= part_a[1] <= part_b[1]:
        return True
    return False


def part1(input_data):
    count = 0
    for pair in input_data:
        part_a, part_b = pair
        if is_contained(part_a, part_b) or is_contained(part_b, part_a):
            count += 1
    return count


def part2(input_data):
    count = 0
    for pair in input_data:
        part_a, part_b = pair
        if partial_overlap(part_a, part_b) or partial_overlap(part_b, part_a):
            count += 1
    return count


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "test_input.txt")) as f:
        data = f.readlines()

    # output = part1(process_input(data))
    # print(output)
    # assert output == EXPECTED_OUTPUT_FROM_DESCRIPTION

    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.readlines()

    # print(part1(process_input(data)))
    print(part2(process_input(data)))
