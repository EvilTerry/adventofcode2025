def task1(rolls: list[list[chr]]) -> int:
    accesible_rolls = 0

    for y in range(len(rolls)):

        for x in range(len(rolls[y])):
            if rolls[y][x] != '@':
                continue

            adjacent_rolls = 0
            
            # Check top 3
            if y > 0 and x > 0 and rolls[y - 1][x - 1] == '@':
                adjacent_rolls += 1

            if y > 0 and rolls[y - 1][x] == '@':
                adjacent_rolls += 1

            if y > 0 and x < len(rolls[y]) - 1 and rolls[y - 1][x + 1] == '@':
                adjacent_rolls += 1

            # Check left
            if x > 0 and rolls[y][x - 1] == '@':
                adjacent_rolls += 1

            # Check right
            if x < len(rolls[y]) - 1 and rolls[y][x + 1] == '@':
                adjacent_rolls += 1

            # Check bottom 3
            if y < len(rolls) - 1 and x > 0 and rolls[y + 1][x - 1] == '@':
                adjacent_rolls += 1

            if y < len(rolls) - 1 and rolls[y + 1][x] == '@':
                adjacent_rolls += 1

            if y < len(rolls) - 1 and x < len(rolls[y]) - 1 and rolls[y + 1][x + 1] == '@':
                adjacent_rolls += 1

            if adjacent_rolls < 4:
                accesible_rolls += 1

    return accesible_rolls

def task2(rolls: list[list[chr]]) -> int:
    total_accesible_rolls = 0

    while True:
        ref_rolls = rolls.copy()
        accesible_rolls = 0

        for y in range(len(ref_rolls)):
            for x in range(len(ref_rolls[y])):
                if ref_rolls[y][x] != '@':
                    continue

                adjacent_rolls = 0
                
                # Check top 3
                if y > 0 and x > 0 and ref_rolls[y - 1][x - 1] == '@':
                    adjacent_rolls += 1

                if y > 0 and ref_rolls[y - 1][x] == '@':
                    adjacent_rolls += 1

                if y > 0 and x < len(ref_rolls[y]) - 1 and ref_rolls[y - 1][x + 1] == '@':
                    adjacent_rolls += 1

                # Check left
                if x > 0 and ref_rolls[y][x - 1] == '@':
                    adjacent_rolls += 1

                # Check right
                if x < len(ref_rolls[y]) - 1 and ref_rolls[y][x + 1] == '@':
                    adjacent_rolls += 1

                # Check bottom 3
                if y < len(ref_rolls) - 1 and x > 0 and ref_rolls[y + 1][x - 1] == '@':
                    adjacent_rolls += 1

                if y < len(ref_rolls) - 1 and ref_rolls[y + 1][x] == '@':
                    adjacent_rolls += 1

                if y < len(ref_rolls) - 1 and x < len(ref_rolls[y]) - 1 and ref_rolls[y + 1][x + 1] == '@':
                    adjacent_rolls += 1

                if adjacent_rolls < 4:
                    accesible_rolls += 1
                    rolls[y][x] = '.'

        if accesible_rolls > 0:
            total_accesible_rolls += accesible_rolls
        else:
            break

    return total_accesible_rolls

if __name__ == '__main__':
    input_file_path = '4/input.txt'

    with open(input_file_path) as file:
        input = file.read().split('\n')

    rolls = [list(line) for line in input]

    print(task1(rolls))
    print(task2(rolls))