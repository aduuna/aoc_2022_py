EXPECTED_OUTPUT_FROM_DESCRIPTION = 157


def process_input(data: list):
    # process input data here
    return [s.rstrip('\n')for s in data]


def calc_priority(char):
    common_char = ord(char)
    # print((common_char - 96) if common_char > 96 else (common_char - 64 + 26))
    return (common_char - 96) if common_char > 96 else (common_char - 64 + 26)


def part1(input_data):
    # for each rucksack
    # split into 2 set
    # for each character from set_a check contained in set_b and store as common_char
    # to find the priority, range 1-52
    # sum priorities

    input_data = [[set(s[:int(len(s)/2)]), set(s[int(len(s)/2):])]
                  for s in input_data]
    priority = 0
    for rucksack in input_data:
        set_a, set_b = rucksack
        for i in set_a:
            if i in set_b:
                priority += calc_priority(i)
                break

    return priority


def part2(input_data):
    # group of 3 rucksack, cyclic loop of 3
    # set_a, set_b, set_c
    # for each char in set_a find common set_b, and c
    # calculate the priority for that

    priority = 0
    looper = 0
    elf_grp = []
    for i in map(set, input_data):
        looper += 1
        elf_grp.append(i)
        if looper % 3 == 0:
            set_a, set_b, set_c = elf_grp
            for char in set_a:
                if char in set_b and char in set_c:
                    priority += calc_priority(char)
                    elf_grp = []
                    break

    return priority


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
