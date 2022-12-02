EXPECTED_OUTPUT_FROM_DESCRIPTION = 15
OPTIONS = {
    'A': 'r',
    'B': 'p',
    'C': 's',
    'X': 'r',
    'Y': 'p',
    'Z': 's',
}
OPTIONS_2 = {
    'A': 'r',
    'B': 'p',
    'C': 's',
    'X': 'l',
    'Y': 'd',
    'Z': 'w',

}


def process_input(data: list):
    # process input data here
    return [s.split() for s in data]


def cast_hand_type(round):
    return [OPTIONS[i] for i in round]


def cast_hand_type_2(round):
    return [OPTIONS[round[0]], OPTIONS_2[round[1]]]


def calc_score(prev, hand, game):
    scores = {
        'r': 1,
        'p': 2,
        's': 3
    }
    game_points = {
        'w': 6,
        'd': 3,
        'l': 0
    }
    # print(hand, game)
    # print("score "+str(prev + scores[hand] + game_points[game]))

    return prev + scores[hand] + game_points[game]


def part1(input_data):

    # r > s
    # s > p
    # p > r

    p1_score = 0
    p2_score = 0

    for round in input_data:
        round = cast_hand_type(round)
        # print(round)
        p1, p2 = round
        if 'r' in round and 'p' in round:
            if p1 == 'p':
                # p1 won
                p2_score = calc_score(p2_score, p2, 'l')
            else:
                # p2 won
                p2_score = calc_score(p2_score, p2, 'w')
        elif 'r' in round and 's' in round:
            if p1 == 'r':
                # p1 won
                p2_score = calc_score(p2_score, p2, 'l')
            else:
                # p2 won
                p2_score = calc_score(p2_score, p2, 'w')
        elif 'p' in round and 's' in round:
            if p1 == 's':
                # p1 won
                p2_score = calc_score(p2_score, p2, 'l')
            else:
                # p2 won
                p2_score = calc_score(p2_score, p2, 'w')
        else:
            p2_score = calc_score(p2_score, p2, 'd')

    return p2_score


def part2(input_data):
    p2_score = 0
    for round in input_data:
        round = cast_hand_type_2(round)
        p1, p2 = round
        if p2 == 'd':
            p2_score = calc_score(p2_score, p1, 'd')
        elif p2 == 'l':
            if p1 == 'r':
                p2_score = calc_score(p2_score, 's', 'l')
            elif p1 == 'p':
                p2_score = calc_score(p2_score, 'r', 'l')
            else:
                p2_score = calc_score(p2_score, 'p', 'l')
        else:
            if p1 == 'r':
                p2_score = calc_score(p2_score, 'p', 'w')
            elif p1 == 'p':
                p2_score = calc_score(p2_score, 's', 'w')
            else:
                p2_score = calc_score(p2_score, 'r', 'w')

    return p2_score


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
