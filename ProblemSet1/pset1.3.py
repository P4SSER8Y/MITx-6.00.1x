""" Problem Set 1.3 ALPHABETICAL SUBSTRINGS """

""" Predefine """
s = 'abc'

""" Source code """

def get_longest_increasing_substring(s):
    length = len(s)
    k = 0
    max_length = 0
    max_position = 0
    while k < length:
        i = k + 1
        while (i < length) and (s[i-1] <= s[i]):
            i += 1
        if (i - k > max_length):
            max_length = i - k
            max_position = k
        k = i
    return s[max_position:max_position + max_length]
    
print get_longest_increasing_substring(s)