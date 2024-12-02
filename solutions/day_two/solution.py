def read_data_file():
    list_of_items = []
    with open("solutions/day_two/small.txt") as f:
        for line in f:
            list_of_items.append(line.strip().lower())
    list_of_items = [item for item in list_of_items if item != ""]
    return list_of_items


def check_if_safe(line):
    for idx, item in enumerate(line):
        curr_num = int(item)
        try:
            next_num = int(line[idx + 1])
            diff = abs(next_num - curr_num)
            if 1 < diff <= 3:
                return False
        except IndexError:
            continue
    return True


def day_two():
    safe_reports = 0
    file_data = read_data_file()
    for line in file_data:
        check_result = check_if_safe(line.split())
        if check_result:
            safe_reports += 1
    print(f"number of safe reports: {safe_reports}")
