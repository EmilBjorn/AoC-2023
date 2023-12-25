#%%
from aocd import get_data


# %%
def parse_numbers(input: str):
    for char in input:
        if char in [str(i) for i in range(10)]:
            first_number = char
            break
    for char in input[::-1]:
        if char in [str(i) for i in range(10)]:
            last_number = char
            break
    return first_number, last_number


#%%
def convert_text_number(entry: str):
    text_numbers_list = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine'
    ]

    for index, val in enumerate(text_numbers_list):
        entry = entry.replace(val, str(index))

    return entry


#%%
def combine_numbers(num1: int, num2: int):
    return int(str(num1) + str(num2))


#%%


def main():
    data = get_data(
        year=2023,
        day=1)  # importerer data som str of gemmer til variablen 'data'
    test_data = '1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet'
    test_data_2 = 'two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen'

    def part_1(data: str):
        data_list = data.split('\n')
        sum = 0
        for entry in data_list:
            num1, num2 = parse_numbers(entry)
            number = combine_numbers(num1, num2)
            sum += number
        return sum

    print(part_1(data))

    def part_2(data: str):
        data_list = data.split('\n')
        sum = 0
        for entry in data_list:
            print(f'entry = {entry}')
            entry = convert_text_number(entry)
            num1, num2 = parse_numbers(entry)
            number = combine_numbers(num1, num2)
            sum += number
            print(f'number = {number}, sum = {sum}')
        return sum

    print('Part 2: ', part_2(test_data_2))


if __name__ == '__main__':
    main()

# %%
