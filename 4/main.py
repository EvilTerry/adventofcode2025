def check_roll(rolls: list[list[str]], x: int, y: int) -> bool:
    if x < 0 or y < 0:
        return False
    try:
        return rolls[y][x] == '@'
    except IndexError:
        return False

def count_adjacent(rolls: list[list[str]], x: int, y: int) -> int:
    offsets = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
    return sum(check_roll(rolls, x+dx, y+dy) for dx, dy in offsets)

def task1(rolls: list[list[str]]) -> int:
    accessible_rolls = 0

    for y, row in enumerate(rolls):
        for x, roll in enumerate(row):
            if roll != '@':
                continue

            if count_adjacent(rolls, x, y) < 4:
                accessible_rolls += 1

    return accessible_rolls

def task2(rolls: list[list[str]]) -> int:
    total_accessible_rolls = 0

    while True:
        ref_rolls = [row[:] for row in rolls]
        accessible_rolls = 0

        for y, row in enumerate(ref_rolls):
            for x, roll in enumerate(row):
                if roll != '@':
                    continue

                if count_adjacent(ref_rolls, x, y) < 4:
                    accessible_rolls += 1
                    rolls[y][x] = '.'

        if accessible_rolls == 0:
            break

        total_accessible_rolls += accessible_rolls

    return total_accessible_rolls

if __name__ == '__main__':
    input_file_path = '4/input.txt'

    with open(input_file_path) as file:
        lines = file.read().split('\n')

    rolls = [list(line) for line in lines]

    print(task1(rolls))
    print(task2(rolls))