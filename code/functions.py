
def calculate_character_occurence(character: str, text: str) -> int:
    assert type(character) == str
    assert type(text) == str
    count = 0
    for stelle in text:
        if stelle == character:
            count += 1
    return count

# print(calculate_character_occurence("a", "aaa"))
# print(calculate_character_occurence("a", "bbb"))
# print(calculate_character_occurence("a", "aaa1234"))
# print(calculate_character_occurence("a", 1234))
# print(calculate_character_occurence(None, None))
# print(calculate_character_occurence(None, "aaaa"))
# print(calculate_character_occurence("a", None))
# print(calculate_character_occurence(" ", "aaa1234"))
# print(calculate_character_occurence("b", {}))
# test_cases = [
#     {"values": calculate_character_occurence("a", "aaa"), "expected_result":}
# ]


print(calculate_character_occurence("a", 1234))
