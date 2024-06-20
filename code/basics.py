# Variables declaration
a = ['a', 1, 'b']
first = a[0]
last = a[-1]
print("initial",a)
# print out list info
print("only first element",a[0])
a[0] = last # a[0] -> 'b'
a[-1] = first
print("final",a)
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
print(list_of_fours2)
