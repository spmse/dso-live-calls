# Variables declaration
from typing import List
a = ['a', 1, 'b']
first = a[0]
last = a[-1]
# print("initial", a)
# print out list info
# print("only first element", a[0])
a[0] = last  # a[0] -> 'b'
a[-1] = first
# print("final", a)
# Generating Lists
# generate a list of 1000 number elements --> 0 - 1000
numbers_to_thousand = [y for y in range(1001)]
# print("------------------------")
# print(numbers_to_thousand)

even_numbers = numbers_to_thousand[0:-1:2]
# print("------------------------")
# print(even_numbers)
odd_numbers = numbers_to_thousand[1:-2:2]
# print("------------------------")
# print(odd_numbers)
# print("------------------------")
reverse_numbers_thousand_to_one = numbers_to_thousand[-1:0:-1]
# print(reverse_numbers_thousand_to_one)
# print("------------------------")

list_of_twos_and_fours = []
for x in numbers_to_thousand:
    if x % 2 == 0 and x % 4 == 0:
        list_of_twos_and_fours.append(x)

# print(list_of_twos_and_fours)
# print("------------------------")
list_of_fours = [x for x in numbers_to_thousand if x % 2 == 0 and x % 4 == 0]
# print(list_of_fours)


def filter_for_fours(number_list):
    result = []
    for x in number_list:
        if x % 2 == 0 and x % 4 == 0:
            result.append(x)
    return result


list_of_fours2 = filter_for_fours(range(250000, 6000000))
# print(list_of_fours2)

# region: filter list for numbers that can be divided by 3


def filter_for_threes(number_list: List[int]) -> List[int]:
    """
    Create a function that receives a list of numbers and only returns
    a list that contains numbers that are divisible by 3.

    :param number_list: the input list of numbers that should be filtered
    :returns List[int]: a list of numbers that are divisible by 3
    """
    temp_list = []
    for number in number_list:
        if number % 3 == 0:
            temp_list.append(number)
    return temp_list


def filter_for_threes_alt(number_list: List[int]) -> List[int]:
    """
    alternative version to iterative approach  
    """
    return list(filter(lambda x: x % 3 == 0, number_list))


def filter_for_threes_alt2(number_list: List[int]) -> List[int]:
    """
    second alternative approach to solve the challenge
    """
    return [x for x in number_list if x % 3 == 0]


# region: testing for 3-filter
a = filter_for_threes(range(0, 10))
b = filter_for_threes_alt(range(0, 10))
c = filter_for_threes_alt2(range(0, 10))

# print(a, b, c)
# endregion
# endregion

# generator function for number lists


def generate_number_list_in_interval(upper_bound: int, lower_bound: int = 0) -> List[int]:
    try:
        lower_bound = int(lower_bound)
        upper_bound = int(upper_bound)
    except:
        raise Exception("you fucked up")

    if type(upper_bound) == int and type(lower_bound) == int:
        step = 1
        try:
            if upper_bound <= lower_bound:
                raise ValueError(
                    "invalid values provided. upper_bound cannot be <= lower_bound")
        except ValueError:
            step = -1

        return list(range(lower_bound, upper_bound, step))
    raise TypeError("Given parameters is no int")


# -> [0,9]
print(generate_number_list_in_interval(lower_bound=900, upper_bound=100))
print(generate_number_list_in_interval(lower_bound=9, upper_bound=True))
