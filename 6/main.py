def task1(line: list[list[str]]) -> int:
    total = 0

    for i in range(len(line[0])):
        digit_1 = int(line[0][i])
        digit_2 = int(line[1][i])
        digit_3 = int(line[2][i])
        digit_4 = int(line[3][i])

        if line[4][i] == '*':
            total += digit_1 * digit_2 * digit_3 * digit_4
        else:
            total += digit_1 + digit_2 + digit_3 + digit_4

    return total

def task2(line: list[list[str]]) -> int:
    ...

if __name__ == '__main__':
    input_file_path = '6/input.txt'

    with open(input_file_path) as file:
        lines = file.read().split('\n')

    for i in range(5):
        lines[i] = ' '.join(lines[i].split()).split(' ')

    print(task1(lines))