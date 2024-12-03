import re


def mul(x, y):
    return x * y


def part1_solution(file_name):
    with open(file_name, "r") as file:
        content = file.read()
    instructions = re.findall(r'mul\([0-9]+,[0-9]+\)', content)
    ans = 0
    for func in instructions:
        mult = eval(func)
        ans += mult
    return ans

def part2_solution(file_name):
    with open(file_name, "r") as file:
        content = file.read()
    instructions = re.findall(r"(mul\(\d+,\d+\)|don't\(\)|do\(\))", content)
    ans = 0
    do = True
    for func in instructions:
        if func == 'do()':
            do = True
            continue
        if func == "don't()":
            do = False
            continue
        if do:
            mult = eval(func)
            ans += mult
    return ans


print(part1_solution('input.txt'))
print(part2_solution('input.txt'))
