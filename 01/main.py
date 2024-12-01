from collections import defaultdict

INPUT_FILE = 'input.txt'
INPUT_EXAMPLE_FILE = 'input_example.txt'

def print_solution(day, p1, p2):
    print(f"** AoC 2024 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")

def parse_lines(input):
	with open(input, 'r') as f:
		lines = f.read().splitlines()
		left_line = []
		right_line = []
		for line in lines:
			left, right = line.split('   ')
			left_line.append(int(left))
			right_line.append(int(right))
	return left_line, right_line

def create_apperances_map(lines):
	apperances_map = defaultdict(int)
	for line in lines:
		apperances_map[line] += 1

	return apperances_map

def main():
	left_line, right_line = parse_lines(INPUT_FILE)
	left_line.sort()
	right_line.sort()

	right_line_appearances = create_apperances_map(right_line)

	total_distance = 0
	similarity_score = 0

	for i in range(len(left_line)):
		total_distance += (abs(left_line[i] - right_line[i])) # Part 1
		similarity_score += left_line[i] * right_line_appearances[left_line[i]] # Part 2

	print_solution(1, total_distance, similarity_score)

if __name__ == "__main__":
	main()
