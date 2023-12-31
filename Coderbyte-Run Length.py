# Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string
# using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character
# and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would
# return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.

def RunLength(s):
    if not s:
        return ""

    compressed = ""
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:                           # executed when the current character s[i] is different from the previous character 
            compressed += str(count) + current_char
            current_char = s[i]
            count = 1

    compressed += str(count) + current_char

    return compressed

# Example usage:
input_str = "wwwggopp"
result = RunLength(input_str)
print(result)  # Output: "3w2g1o2p"
