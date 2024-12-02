from part1 import read_two_column_file


def part2_solution(file_name):
    similarity_score = 0
    col1, col2 = read_two_column_file(file_name)

    counter = dict()
    for i in col2:
        counter[i] = counter.get(i, 0) + 1
    for val in col1:
        if counter.get(val) is not None:
            similarity_score += (int(val) * int(counter.get(val)))
    return similarity_score


# print(part2_solution('input.txt'))
