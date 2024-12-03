import re

INPUT_FILE = 'input.txt'
INPUT_EXAMPLE_FILE = 'input_example.txt'


def print_solution(day, p1, p2):
    print(f"** AoC 2024 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def parse_input(input):
    with open(input, 'r') as f:
        return f.read().replace("\n", "")


def find_instructions(corrupted_data):
    pattern = r"mul\((\d*,\d*)\)"
    return (match.split(',') for match in re.findall(pattern, corrupted_data))


def remove_dont_instructions(corrupted_data):
    pattern = r"(don't\(\).+?(?=do\(\)))"
    return re.sub(pattern, '', corrupted_data)


def calculate_result(instructions):
    return sum(int(x) * int(y) for x, y in instructions)


def main():
    memory_input = parse_input(INPUT_FILE)
    p1_instructions = find_instructions(memory_input)
    p2_instructions = find_instructions(remove_dont_instructions(memory_input))

    p1_result = calculate_result(p1_instructions)
    p2_result = calculate_result(p2_instructions)

    print_solution(3, p1_result, p2_result)


if __name__ == "__main__":
    main()
