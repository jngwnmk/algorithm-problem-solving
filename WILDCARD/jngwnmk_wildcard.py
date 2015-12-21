import fnmatch

def solve(pattern, input):
    table = [[False for col in range(len(pattern)+1)] for row in range(len(input)+1)]

    table[0][0] = True

    for i in xrange(1,len(input)+1):
        table[i][0] = False

    for j in xrange(1,len(pattern)+1):
        table[0][j] = table[0][j-1] and pattern[j-1]=='*'

    for i in xrange(1,len(input)+1):
        for j in xrange(1,len(pattern)+1):
            if pattern[j-1] == '*':
                table[i][j] = table[i][j-1] or table[i-1][j]
            else:
                table[i][j] = table[i-1][j-1] and (pattern[j-1] == '?' or pattern[j-1] == input[i-1])

    # for row in table:
    #     print row

    return table[len(input)][len(pattern)]


if __name__ == '__main__':
    test_case = int(raw_input())
    for tc in range(test_case):
        pattern = raw_input()
        file_num = int(raw_input())
        matched = []
        for file_idx in range(file_num):
            input_file = raw_input()
            if solve(pattern, input_file):
                matched.append(input_file)
            # if fnmatch.fnmatch(input_file,pattern):
            #      matched.append(input_file)
        for file in sorted(matched):
            print file

# pattern = "*p*"
# inputstr = "help"
#
# print solve(pattern, inputstr)
# print fnmatch.fnmatch(inputstr, pattern)