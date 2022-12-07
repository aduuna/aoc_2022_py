EXPECTED_OUTPUT_FROM_DESCRIPTION = 95437

ROOT = None
TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000


class EntityType:
    DIR = "dir"
    FILE = "file"


class Entity:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.size = 0
        self.children = {}
        self.parent = None

    def __str__(self):
        string = ""
        string += '- ' + self.name + ' (' + self.type
        string += ')\n' if self.type == EntityType.DIR else f', size={self.size})\n'
        string += "".join([str(child) for child in self.children.values()])
        return string

    def __lt__(self, other):
        return self.size < other.size

    def add_children(self, children):
        children_entities = []
        for child in children:
            e_type, name = child.split()
            if e_type == EntityType.DIR:
                new_child = Entity(EntityType.DIR, name)
                new_child.parent = self
                children_entities.append(new_child)
            else:
                size = int(e_type)
                new_child = Entity(EntityType.FILE, name)
                new_child.size = size
                new_child.parent = self
                children_entities.append(new_child)
        self.children = \
            {child.name: child for child in children_entities}
        self.update_size(sum([c.size for c in self.children.values()]))

    def update_size(self, size):
        self.size += size
        if self.name != '/':
            self.parent.update_size(size)


def process_input(data: list):
    # process input data here
    command_and_output = []
    for i in range(len(data)):
        if data[i][0] == "$":
            output = []
            for j in range(i+1, len(data)):
                if data[j][0] == "$":
                    break
                output.append(data[j].rstrip("\n"))

            temp = [data[i].rstrip("\n"), output]
            command_and_output.append(temp)
    return command_and_output


def find_candidates(root: Entity):
    candidates = []
    if root.size <= 100_000:
        candidates.append(root)
    for child in root.children.values():
        if child.type == EntityType.DIR:
            candidates += find_candidates(child)
    return candidates


def find_candidates_2(root: Entity, size):
    candidates = []
    if root.size > size:
        candidates.append(root)
    for child in root.children.values():
        if child.type == EntityType.DIR:
            candidates += find_candidates_2(child, size)
    return candidates


def part1(input_data):
    cwd = None
    for command, output in input_data:
        if "$ cd " in command:
            loc = command.split()[-1]
            if loc == '/':
                cwd = Entity(EntityType.DIR, loc)
                global ROOT
                ROOT = cwd
            elif loc == '..':
                cwd = cwd.parent
            else:
                cwd = cwd.children.get(loc)
        else:
            cwd.add_children(output)

    return sum([c.size for c in find_candidates(ROOT)])


def part2(input_data):

    used_space = ROOT.size
    available_space = TOTAL_SPACE - used_space
    deletable_space = REQUIRED_SPACE - available_space

    return min(find_candidates_2(ROOT, deletable_space)).size


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "test_input.txt")) as f:
        data = f.readlines()

    output = part1(process_input(data))
    print(output)
    assert output == EXPECTED_OUTPUT_FROM_DESCRIPTION

    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.readlines()

    input_data = process_input(data)
    print(part1(input_data))
    print(part2(input_data))
