INPUT_FILE = 'input.txt'
INPUT_EXAMPLE_FILE = 'input_example.txt'


def print_solution(day, p1, p2):
    print(f"** AoC 2024 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def parse_input(input):
    with open(input, 'r') as f:
        lines = f.read().splitlines()
        reports = []
        for line in lines:
            reports.append([int(s) for s in line.split()])
        return reports


def is_report_safe(report):
    increase = report[0] < report[1]
    decrease = report[0] > report[1]
    if report[0] == report[1]:
        return False

    allowed_decrease = [1, 2, 3]
    allowed_increase = [-1, -2, -3]

    for i in range(len(report) - 1):
        if ((report[i] - report[i+1]) not in allowed_decrease) and decrease:
            return False
        if ((report[i] - report[i+1]) not in allowed_increase) and increase:
            return False
    return True


def is_report_safe_damp(report):
    if is_report_safe(report):
        return True

    for i in range(len(report)):
        if is_report_safe(report[:i] + report[i+1:]):
            return True
    return False


def main():
    reports = parse_input(INPUT_FILE)
    safe_report_count = 0
    safe_report_damp_count = 0

    for report in reports:
        if is_report_safe(report):
            safe_report_count += 1
        if is_report_safe_damp(report):
            safe_report_damp_count += 1

    print_solution(2, safe_report_count, safe_report_damp_count)


if __name__ == "__main__":
    main()
