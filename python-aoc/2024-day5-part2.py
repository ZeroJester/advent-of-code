input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

input2="""75,47,61,53,29
97,61,53,29,13
75,29,13"""



lines = input.splitlines()


rules = input.split("\n")
page_numbers = input2.split("\n")
value_map = {}

for rule in rules:
    key, value = rule.split("|")

    if key not in value_map:
        value_map[key] = []

    value_map[key].append(value)

# print("Map:")
# for key, values in value_map.items():
#     print(f"{key}: {values}")



is_valid = True
total=0
valid_pages = []
invalid_pages = []
for page in page_numbers:
    values = page.split(",")

    is_valid = True
    for i in range(len(values)):

        current = values[i]

        previous_values = values[:i]

        if current in value_map:

            if any(prev in value_map[current] for prev in previous_values):
                is_valid = False
                break

    if is_valid:
        valid_pages.append(page)
    else:
        invalid_pages.append(page)


def is_valid(page):
    values = page.split(",")
    for i in range(len(values)):
        current = values[i]
        previous_values = values[:i]
        if current in value_map:
            if any(prev in value_map[current] for prev in previous_values):
                return False
    return True



def find_invalid_char(page):
    values = page.split(",")

    print("new page:")
    for i in range(len(values)):
        print("new instance")
        next_value = values[:i]

        for val in next_value:
            if (val in value_map and values[i] in value_map[val]):
                print(val)



for page in page_numbers:
    find_invalid_char(page)

# def reorder_page(arr, value_map):
#
#     for x in range (10):
#         for i in range (len(values)-1):
#             current = int(arr[i])
#             next = int(arr[i+1])
#             if next in value_map:
#                 if current in value_map[next]:
#                     # not valid
#                     arr[i] = next
#                     arr[i + 1] = current
#
#     return arr
#
# new_valid_pages = []
# for page in invalid_pages:
#     values = page.split(",")
#     arr = []
#     for val in values:
#         arr.append(val)
#
#     reordered_page = reorder_page(arr, value_map)
#     if reordered_page != "":
#         new_valid_pages.append(reordered_page)

#
# print(new_valid_pages)
# # Calculate total
# # total = 0
# # for page in new_valid_pages:
# #     values = page.split(",")
# #     if values:  # Add check to prevent empty list error
# #         index = len(values) // 2
# #         total += int(values[index])
#
# print(new_valid_pages)
# print(total)

