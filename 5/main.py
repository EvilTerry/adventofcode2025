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

def task2(fresh_ids: list[str]) -> int:
    fresh_ids = [[int(fresh_id.split('-')[0]), int(fresh_id.split('-')[1])] for fresh_id in fresh_ids]

    fresh_ids.sort(key = lambda x: x[0])
    merged = []
    start, end = fresh_ids[0]

    for s, e in fresh_ids[1:]:
        if s <= end:  
            end = max(end, e)
        else:
            merged.append((start, end))
            start, end = s, e

    merged.append((start, end))

    return sum((start - end + 1) for start, end in merged)

if __name__ == '__main__':
    input_file_path = '5/input.txt'

    with open(input_file_path) as file:
        lines = file.read().split('\n')

    fresh_ids = lines[:lines.index('')]
    available_ids = lines[lines.index('') + 1:]

    # print(task1(fresh_ids, available_ids))
    print(task2(fresh_ids))