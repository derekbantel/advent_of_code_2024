def read_data_file():
    list_of_items = []
    with open("solutions/day_one/data.txt") as f:
        for line in f:
            list_of_items.append(line.strip().lower())
    list_of_items = [item for item in list_of_items if item != ""]
    return list_of_items


def split_lines_into_lists(lines):
    first_list = []
    second_list = []
    for line in lines:
        one, two = line.split()
        first_list.append(int(one))
        second_list.append(int(two))
    sorted_first = sorted(first_list)
    sorted_second = sorted(second_list)
    return sorted_first, sorted_second


def sum_difference(first, second):
    total_diff = 0
    for idx, item in enumerate(first):
        total_diff += abs(item - second[idx])
    return total_diff


def calculate_similarity_scores(first, second):
    similarity_scores = []
    for item in first:
        item_occurrences = 0
        for thing in second:
            if item == thing:
                item_occurrences += 1
        similarity_scores.append(item * item_occurrences)
    return sum(similarity_scores)


def day_one():
    list_of_items = read_data_file()
    first_list, second_list = split_lines_into_lists(list_of_items)
    print(f"day one part one answer: {sum_difference(first_list, second_list)}")
    print(f"day one part two answer: {calculate_similarity_scores(first_list, second_list)}")
