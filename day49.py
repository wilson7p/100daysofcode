#Write a program to find the longest common prefix of a list of strings.
print ("\nWilson - Day 49 of #100DaysOfCode\n") 
print("\nprogram to find the longest common prefix of a list of strings\n")

def longest_common_prefix(strings):
    if not strings:
        return ""
    strings.sort()
    first_str, last_str = strings[0], strings[-1]
    common_prefix = ""
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common_prefix += first_str[i]
        else:
            break
    return common_prefix

input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print("Longest Common Prefix:", result)
