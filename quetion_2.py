'''
Write a program to extract string elements from a
list based on below conditions, use
in-built functions.
a. First character must capitalize and consonant.
b. String must not contain any number.
'''
VOWEL = "aeiouAEIOU"


def extract_element(string_list):
    '''extract string elements from a list'''
    elm_list = []
    for _ in string_list:
        if _[0].isupper() and _[0] not in VOWEL:
            if not any(c for c in _ if c.isdigit()):
                elm_list.append(_)

    return elm_list


string = list(input().split())
result = extract_element(string)

print(result)
