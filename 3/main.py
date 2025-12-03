def task1(banks: list[str]) -> str:
    total_joltage = 0

    for bank in banks:
        pointer_1 = 0
        pointer_2 = 0

        for i in range(len(bank)):
            joltage = int(bank[i])

            if i < len(bank) - 1 and joltage > pointer_1:
                pointer_1 = joltage
                pointer_2 = int(bank[i + 1])

            elif joltage > pointer_2:
                pointer_2 = joltage
        
        total_joltage += pointer_1 * 10 + pointer_2

    return total_joltage


def task2(banks: list[str]) -> str:
    total_joltage = 0

    for bank in banks:
        # Convert string into list of chars
        bank = list(bank)
        joltage = ''

        for i in range(12):
            # Define the searching range
            search_array = bank[:len(bank) - (11 - i)]

            # Find highest number from the search range
            highest_number = sorted(search_array, reverse=True)[0]

            # Remove joltages until the highest number
            bank = bank[bank.index(highest_number) + 1:]

            joltage += highest_number

        total_joltage += int(joltage)

    return total_joltage

if __name__ == '__main__':
    file = open('3/input.txt')
    banks = file.read().split('\n')
    file.close()

    print(task1(banks))
    print(task2(banks))