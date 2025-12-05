def task1(fresh_ids: list[str], available_ids: list[str]) -> int:
    total_count = 0

    for available_id in available_ids:
        for fresh_id_range in fresh_ids:
            start = fresh_id_range.split('-')[0]
            end = fresh_id_range.split('-')[1]

            if int(available_id) >= int(start) and int(available_id) <= int(end):
                total_count += 1
                break

    return total_count

def task2(fresh_ids: list[str], available_ids: list[str]) -> int:
    ...

if __name__ == '__main__':
    input_file_path = '5/input.txt'

    with open(input_file_path) as file:
        lines = file.read().split('\n')

    fresh_ids = lines[:lines.index('')]
    available_ids = lines[lines.index('') + 1:]

    print(task1(fresh_ids, available_ids))