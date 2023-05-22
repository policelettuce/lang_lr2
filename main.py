matrix = [
    # A     E     B     C     D     +     -     *     /     a     (     )     #
    [None, None, None, None, None,  0,    0,   None, None, None, None,  0,    1  ],  # A
    [None, None, None, None, None,  1,    1,   None, None, None, None,  1,    1  ],  # E
    [None, None, None, None, None,  1,    1,    0,    0,   None, None,  1,    1  ],  # B
    [None, None, None, None, None,  1,    1,    1,    1,   None, None,  1,    1  ],  # C
    [None, None, None, None, None,  1,    1,    1,    1,   None, None,  1,    1  ],  # D
    [None,  0,   -1,   -1,   None, None, None, None, None, -1,   -1,   None,  1  ],  # +
    [None,  0,   -1,   -1,   None, None, None, None, None, -1,   -1,   None,  1  ],  # -
    [None, None, None,  0,   None, None, None, None, None, -1,   -1,   None,  1  ],  # *
    [None, None, None,  0,   None, None, None, None, None, -1,   -1,   None,  1  ],  # /
    [None, None, None, None, None,  1,    1,    1,    1,   None, None,  1,    1  ],  # a
    [-1,   -1,   -1,   -1,    0,   None, None, None, None, -1,   -1,   None,  1  ],  # (
    [None, None, None, None, None,  1,    1,    1,    1,   None, None,  1,    1  ],  # )
    [-1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   None]   # #
]

grammar = {
    "A": ["A+E", "A-E", "E"],
    "E": ["B"],
    "B": ["B*C", "B/C", "C"],
    "C": ["a", "(D"],
    "D": ["A)"]
}

symbol = {
    "A": 0,
    "E": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "+": 5,
    "-": 6,
    "*": 7,
    "/": 8,
    "a": 9,
    "(": 10,
    ")": 11,
    "#": 12
}


def get_relation(left, right):
    res = matrix[symbol[left]][symbol[right]]
    print("Getting relation between [" + left + "] and [" + right + "]. Equals: " + str(res))
    return res


def main():
    print("Enter a line")
    str1 = input() + "#"
    stack = ['#']
    pointer = 0
    while pointer < len(str1):
        char = str1[pointer]
        if stack == ['#', 'A'] and char == '#':        # Line convolved to #A# i.e. successful recognition
            return True
        if (char not in symbol):
            print('ERROR: Such symbol does not exist in this grammar...')
            return False
        relation = get_relation(stack[-1], char)
        if relation == None:
            print('ERROR: No relation between two adjacent symbols...')
            return False
        elif relation <= 0:
            stack.append(char)
            print('Adding [' + char + '] to stack. \nCurrent stack: ' + str(stack) + '\n')
            pointer += 1
        else:
            print('Starting stack convolution:')
            print(stack)

            single_char = stack.pop()
            try:
                double_char = stack[-1] + single_char
            except Exception as e:
                double_char = "whatever"
            try:
                triple_char = stack[-2] + double_char
            except Exception as e:
                triple_char = "clueless"

            flag = 0

            for key in grammar:
                if triple_char in grammar[key]:
                    print('Convolving substring [' + triple_char + '] to [' + key + ']')
                    stack.pop()
                    stack.pop()
                    stack.append(key)
                    print(stack)
                    flag = 1
                    print('Current stack: ' + str(stack) + "\n")
                    break
            if flag == 1:
                continue
            for key in grammar:
                if double_char in grammar[key]:
                    print('Convolving substring [' + double_char + '] to [' + key + ']')
                    stack.pop()
                    stack.append(key)
                    print(stack)
                    flag = 1
                    print('Current stack: ' + str(stack) + "\n")
                    break
            if flag == 1:
                continue
            for key in grammar:
                if single_char in grammar[key]:
                    print('Convolving substring [' + single_char + '] to [' + key + ']')
                    stack.append(key)
                    print(stack)
                    flag = 1
                    print('Current stack: ' + str(stack) + "\n")
                    break
            if flag == 0:
                print('ERROR: No suitable rule in grammar for convolution...')
                return False


if __name__ == "__main__":
    res = main()
    if res == False:
        print("Line is NOT a part of the grammar")
    else:
        print("Line IS a part of the grammar")
