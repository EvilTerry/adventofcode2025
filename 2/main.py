def task1(ids: list[str]) -> str:
    output = 0

    for id in ids:
        id_range = id.split('-')
        for i in range(int(id_range[0]), int(id_range[1]) + 1):
            str_i = str(i)
            if len(str_i) % 2 == 0:
                str_mid = int(len(str_i) / 2)
                first_half = str_i[:str_mid]
                second_half = str_i[str_mid:]

                if first_half == second_half:
                    output += int(str_i)

    return output

def task2(ids: list[str]) -> str:
    pass

if __name__ == '__main__':
    file = open('2/input.txt')
    ids = file.read().split(',')
    file.close()

    print(task1(ids))