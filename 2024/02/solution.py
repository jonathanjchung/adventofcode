import csv
from copy import copy


def read_file_into_list(file_name):
    puzzle_input = []
    with open(file_name, "r") as input_file:
        csv_file = csv.reader(input_file, delimiter=' ')
        for row in csv_file:
            temp = list(map(int, list(row)))
            puzzle_input.append(temp)
    return puzzle_input


def is_increasing(row):
    left, right = 0, 1
    while right < len(row):
        diff = abs(row[right] - row[left])
        if row[left] > row[right]:
            return False
        if diff > 3 or diff < 1:
            return False
        left += 1
        right += 1
    return True


def is_decreasing(row):
    left, right = 0, 1
    while right < len(row):
        diff = abs(row[right] - row[left])
        if row[left] < row[right]:
            return False
        if diff > 3 or diff < 1:
            return False
        left += 1
        right += 1
    return True


def part1_solution(file_name):
    puzzle_input = read_file_into_list(file_name)
    safe = 0
    for row in puzzle_input:
        if is_increasing(row) or is_decreasing(row):
            safe += 1
    return safe


def part2_solution(file_name):
    puzzle_input = read_file_into_list(file_name)
    safe = 0
    for row in puzzle_input:
        if not (is_increasing(row) or is_decreasing(row)):
            for val in range(len(row)):
                temp = copy(row)
                temp.pop(val)
                if is_increasing(temp) or is_decreasing(temp):
                    safe += 1
                    break
    return safe


# print(part1_solution('input.txt'))
# print(part2_solution('input.txt'))
print(part1_solution('input.txt') + part2_solution('input.txt'))
