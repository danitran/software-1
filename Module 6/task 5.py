def remove_uneven(numbers):
    return [num for num in numbers if num % 2 == 0]


def main_remove_uneven():
    original_list = [121, 1232, 143, 15254, 523, 612, 327, 65, 9]
    even_list = remove_uneven(original_list)
    print(f"Original list: {original_list}")
    print(f"List after removing odd numbers: {even_list}")

main_remove_uneven()