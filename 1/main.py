def task1(rotations: list[str]) -> int:
    dial = 50
    password = 0

    for r in rotations:
        if r[0] == 'R':
            dial += int(r[1:])
        else:
            dial -= int(r[1:])

        if dial < 0 or dial > 99:
            dial %= 100

        if dial == 0:
            password += 1

    return password


if __name__ == '__main__':
    file = open('1/input.txt')
    rotations = file.read().split('\n')
    file.close()

    print(task1(rotations))