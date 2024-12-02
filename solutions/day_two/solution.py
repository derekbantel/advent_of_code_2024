def read_data_file():
    list_of_items = []
    with open("solutions/day_two/data.txt") as f:
        for line in f:
            list_of_items.append(line.strip().lower())
    list_of_items = [item for item in list_of_items if item != ""]
    return list_of_items


def check_if_safe(line):
    levels = list(map(int, line.split()))
    if levels[0] < levels[1]:
        line_status = "increased"
    elif levels[0] > levels[1]:
        line_status = "decreased"
    else:
        return False
    for i in range(len(levels) - 1):
        curr_num = levels[i]
        next_num = levels[i + 1]
        diff = abs(curr_num - next_num)
        if not (1 <= diff <= 3):
            return False
        if line_status == "increased" and curr_num >= next_num:
            return False
        if line_status == "decreased" and curr_num <= next_num:
            return False
    return True



def day_two():
    safe_reports = 0
    file_data = read_data_file()
    for idx, line in enumerate(file_data):
        check_result = check_if_safe(line)
        if check_result:
            safe_reports += 1
    print(f"number of safe reports: {safe_reports}")
