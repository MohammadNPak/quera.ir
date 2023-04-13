def compare(string1, string2):

    while True:
        if len(string1) == 0 and len(string2) == 0:
            return "Both strings are empty!"
        elif len(string1) == 0:
            return string2
        elif len(string2) == 0:
            return string1
        else:
            if string1[0] < string2[0]:
                string1, string2 = string1[1:], string2
            elif string2[0] < string1[0]:
                string1, string2 = string1, string2[1:]
            else:
                string1, string2 = string1[1:], string2[1:]
            if len(string1) == 0 and len(string2) > 0:
                return string2
            elif len(string1) > 0 and len(string2) == 0:
                return string1
            elif len(string1) == 0 and len(string2) == 0:
                return "Both strings are empty!"
            else:
                string1 = string1[::-1]
                string2 = string2[::-1]


# print(compare('amin', 'nima'))
