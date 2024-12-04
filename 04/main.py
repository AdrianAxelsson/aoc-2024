INPUT_FILE = 'input.txt'
INPUT_EXAMPLE_FILE = 'input_example.txt'


def print_solution(day, p1, p2):
    print(f"** AoC 2024 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def parse_input(input):
    with open(input, 'r') as f:
        grid = []
        for line in f.read().splitlines():
            temp = []
            for char in line:
                temp.append(char)
            grid.append(temp)
        return grid


def get_grid_value(grid, x, y):
    default_val = '.'
    if x < 0 or y < 0:
        return default_val
    if x > len(grid[0]) - 1:
        return default_val
    if y > len(grid) - 1:
        return default_val
    return grid[y][x]


def get_word_from_direction(direction, x, y, grid, word_length):
    directions = {
        'up': {'x': 0, 'y': -1},
        'down': {'x': 0, 'y': 1},
        'left': {'x': -1, 'y': 0},
        'right': {'x': 1, 'y': 0},
        'up_left': {'x': -1, 'y': -1},
        'up_right': {'x': 1, 'y': -1},
        'down_left': {'x': -1, 'y': 1},
        'down_right': {'x': 1, 'y': 1}
    }
    return_string = get_grid_value(grid, x, y)
    for i in range(word_length - 1):
        x += directions[direction]['x']
        y += directions[direction]['y']
        return_string += get_grid_value(grid, x, y)

    return return_string


def main():
    grid = parse_input(INPUT_FILE)
    directions = [
        'up',
        'down',
        'left',
        'right',
        'up_left',
        'up_right',
        'down_left',
        'down_right'
    ]
    keyword = "XMAS"
    p1_count = 0
    p2_count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Part 1
            if get_grid_value(grid, j, i) == keyword[0]:
                for direction in directions:
                    if get_word_from_direction(direction, j, i, grid, len(keyword)) == keyword:
                        p1_count += 1
            # Part 2
            elif get_grid_value(grid, j, i) == 'A':
                if ((get_grid_value(grid, j+1, i+1) == 'M' and get_grid_value(grid, j-1, i-1) == 'S') or (get_grid_value(grid, j+1, i+1) == 'S' and get_grid_value(grid, j-1, i-1) == 'M')) and ((get_grid_value(grid, j-1, i+1) == 'M' and get_grid_value(grid, j+1, i-1) == 'S' or get_grid_value(grid, j-1, i+1) == 'S' and get_grid_value(grid, j+1, i-1) == 'M')):
                    p2_count += 1

    print_solution(4, p1_count, p2_count)


if __name__ == "__main__":
    main()
