
from pprint import pprint
EXPECTED_OUTPUT_FROM_DESCRIPTION = 'CMZ'


def process_input(data: list):
    # process input data here
    stacks = [[] for i in range(len(data[0])//4)]
    instructions = []
    done_collecting_stacks = False
    for i in data:
        i = i.rstrip('\n')
        if i == '':
            done_collecting_stacks = True
            continue
        if done_collecting_stacks:
            strings = i.split()
            inst = []
            for j in range(len(strings)):
                if j % 2 == 0:
                    continue
                inst.append(int(strings[j]))
            instructions.append(inst)
        else:
            string = i.replace("    ", "  ").replace('[', "").replace(']', "")
            for j in range(len(string)):
                if j % 2 != 0:
                    continue
                if string[j] != ' ':
                    stacks[j//2].append(string[j])
    return (stacks, instructions)


def part1(input_data):
    stacks, instructions = input_data
    for instruction in instructions:
        quantity, form_stack, to_stack = instruction
        for i in range(quantity):
            val = stacks[form_stack-1].pop(0)
            stacks[to_stack-1].insert(0, val)
    return ''.join([stack.pop(0) for stack in stacks])


def part2(input_data):
    stacks, instructions = input_data
    for instruction in instructions:
        quantity, form_stack, to_stack = instruction
        temp_vals = stacks[form_stack-1][:quantity]
        stacks[form_stack-1] = stacks[form_stack-1][quantity:]
        stacks[to_stack-1] = temp_vals + stacks[to_stack-1]
    return ''.join([stack.pop(0) for stack in stacks])


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
