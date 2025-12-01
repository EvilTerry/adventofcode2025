import math

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

def task2(rotations: list[str]) -> int:
    dial = 50
    password = 0

    for r in rotations:
        rotation_direction = r[0] == 'R'
        rotation_count = int(r[1:])

        for _ in range(rotation_count):
            if rotation_direction:
                dial += 1
            else:
                dial -= 1

            if dial == 100:
                dial = 0
            elif dial == -1:
                dial = 99
            
            if dial == 0:
                password += 1

    return password

if __name__ == '__main__':
    file = open('1/input.txt')
    rotations = file.read().split('\n')
    file.close()

    print(task1(rotations))
    print(task2(rotations))