from mergesort import merge_sort


def read_two_column_file(file_name):
    col1 = []
    col2 = []
    with open(file_name, "r") as input_file:
        for line in input_file:
            row = line.split('   ')
            col1.append(row[0])
            col2.append(row[1].rstrip('\n'))
    return col1, col2


def part1_solution(file_name):
    total_distance = 0
    col1, col2 = read_two_column_file(file_name)
    col1 = merge_sort(col1)
    col2 = merge_sort(col2)
    for i in range(len(col1)):
        total_distance += abs(int(col2[i]) - int(col1[i]))
    return total_distance


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

# print(part1_solution('input.txt'))
